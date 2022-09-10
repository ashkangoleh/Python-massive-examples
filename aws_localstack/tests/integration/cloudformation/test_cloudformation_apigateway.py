import json
import os.path

import pytest
import requests

from localstack import constants
from localstack.utils.common import short_uid
from localstack.utils.run import to_str
from tests.integration.apigateway_fixtures import api_invoke_url

TEST_TEMPLATE_1 = """
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Parameters:
  ApiName:
    Type: String
  IntegrationUri:
    Type: String
Resources:
  Api:
    Type: AWS::Serverless::Api
    Properties:
      StageName: dev
      Name: !Ref ApiName
      DefinitionBody:
        swagger: 2.0
        info:
          version: "1.0"
          title: "Public API"
        basePath: /base
        schemes:
        - "https"
        x-amazon-apigateway-binary-media-types:
        - "*/*"
        paths:
          /test:
            post:
              responses: {}
              x-amazon-apigateway-integration:
                uri: !Ref IntegrationUri
                httpMethod: "POST"
                type: "http_proxy"
"""


def test_cfn_apigateway_aws_integration(
    apigateway_client, s3_client, iam_client, deploy_cfn_template
):
    api_name = f"rest-api-{short_uid()}"
    custom_id = short_uid()

    deploy_cfn_template(
        template_path=os.path.join(
            os.path.dirname(__file__), "../templates/apigw-awsintegration-request-parameters.yaml"
        ),
        parameters={
            "ApiName": api_name,
            "CustomTagKey": "_custom_id_",
            "CustomTagValue": custom_id,
        },
    )

    # check resources creation
    apis = [api for api in apigateway_client.get_rest_apis()["items"] if api["name"] == api_name]
    assert len(apis) == 1
    api_id = apis[0]["id"]

    # check resources creation
    resources = apigateway_client.get_resources(restApiId=api_id)["items"]
    assert (
        resources[0]["resourceMethods"]["GET"]["requestParameters"]["method.request.path.id"]
        is False
    )
    assert (
        resources[0]["resourceMethods"]["GET"]["methodIntegration"]["requestParameters"][
            "integration.request.path.object"
        ]
        == "method.request.path.id"
    )

    # check domains creation
    domain_names = [
        domain["domainName"] for domain in apigateway_client.get_domain_names()["items"]
    ]
    expected_domain = "cfn5632.localstack.cloud"  # hardcoded value from template yaml file
    assert expected_domain in domain_names

    # check basepath mappings creation
    mappings = [
        mapping["basePath"]
        for mapping in apigateway_client.get_base_path_mappings(domainName=expected_domain)["items"]
    ]
    assert len(mappings) == 1
    assert mappings[0] == "(none)"


@pytest.mark.skip_offline
@pytest.mark.aws_validated
def test_cfn_apigateway_swagger_import(deploy_cfn_template, apigateway_client):
    api_name = f"rest-api-{short_uid()}"
    int_uri = "http://httpbin.org/post"
    deploy_cfn_template(
        template=TEST_TEMPLATE_1,
        parameters={"ApiName": api_name, "IntegrationUri": int_uri},
    )

    # get API details
    apis = [api for api in apigateway_client.get_rest_apis()["items"] if api["name"] == api_name]
    assert len(apis) == 1
    api_id = apis[0]["id"]

    # construct API endpoint URL
    url = api_invoke_url(api_id, stage="dev", path="/test")

    # invoke API endpoint, assert results
    result = requests.post(url, data="test 123")
    assert result.ok
    content = json.loads(to_str(result.content))
    assert content["data"] == "test 123"
    assert content["url"].endswith("/post")


@pytest.mark.only_localstack
def test_url_output(apigateway_client, tmp_http_server, deploy_cfn_template):
    test_port, invocations, proxy = tmp_http_server
    integration_uri = f"http://localhost:{test_port}/{{proxy}}"
    api_name = f"rest-api-{short_uid()}"

    stack = deploy_cfn_template(
        template_path=os.path.join(
            os.path.dirname(__file__), "../templates/apigateway-url-output.yaml"
        ),
        template_mapping={
            "api_name": api_name,
            "integration_uri": integration_uri,
        },
    )

    assert len(stack.outputs) == 2
    api_id = stack.outputs["ApiV1IdOutput"]
    api_url = stack.outputs["ApiV1UrlOutput"]
    assert api_id
    assert api_url
    assert api_id in api_url

    assert f"https://{api_id}.execute-api.{constants.LOCALHOST_HOSTNAME}:4566" in api_url
