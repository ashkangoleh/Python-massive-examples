import logging
import random
import time

from locust import HttpUser, task, between
from locust.exception import RescheduleTask


test_email_host = 'my-local-test.test'

def unique_str():
    return '{:.10f}.{}'.format(time.time(), random.randint(1000, 9999))

def unique_email():
    return 'e.' + unique_str() + '@' + test_email_host

def unique_city_name():
    return 'c.' + unique_str()


class WebsiteTestUser(HttpUser):
    network_timeout = 30.0
    connection_timeout = 30.0
    #wait_time = between(0.5, 3.0)

    def on_start(self):

        base_url = 'http://127.0.0.1:8020/api/v1'

        # set up urls
        register_url = base_url + '/auth/register'
        get_token_url = base_url + '/auth/token'
        # urls used in task
        self.cities_create_url = base_url + '/cities'
        self.cities_get_by_id_url = base_url + '/cities/'

        # get unique email
        email = unique_email()
        password = 'abcdefghi'

        # register
        response = self.client.post(
            register_url,
            json={'email': email, 'password': password},
        )
        if response.status_code != 201:
            error_msg = 'register: response.status_code = {}, expected 201'.format(response.status_code)
            logging.error(error_msg)

        # get_token
        # - username instead of email
        # - x-www-form-urlencoded (instead of json)
        response = self.client.post(
            get_token_url,
            data={'username': email, 'password': password},
        )
        access_token = response.json()['access_token']
        logging.debug('get_token: for email = {}, access_token = {}'.format(email, access_token))

        # set headers with access token
        self.headers = {'Authorization': 'Bearer ' + access_token}

    def on_stop(self):
        pass

    # enable this dummy task to develop 'on_start'
    #@task
    def dummy(self):
        pass

    @task
    def cities_write_read_check(self):
        # add city to api
        city_name = unique_city_name()
        logging.debug('cities_create: city_name = {}'.format(city_name))
        with self.client.post(
            self.cities_create_url,
            json={'name': city_name},
            headers=self.headers,
            catch_response=True,
        ) as response:

            if response.status_code != 201:
                error_msg = 'cities_create: response.status_code = {}, expected 201, city_name = {}'.format(response.status_code, city_name)
                logging.error(error_msg)
                response.failure(error_msg)
                raise RescheduleTask()

            response_dict = response.json()
            if 'data' not in response_dict:
                error_msg = 'cities_create: data not in response_dict, city_name = {}'.format(city_name)
                logging.error(error_msg)
                response.failure(error_msg)
                raise RescheduleTask()

            city_id = response_dict['data']['id']
            logging.debug('cities_create: for city_name = {}, city_id = {}'.format(city_name, city_id))

        # get city from api and check
        with self.client.get(
            self.cities_get_by_id_url + city_id,
            headers=self.headers,
            name=self.cities_get_by_id_url + 'uuid', 
            catch_response=True,
        ) as response:

            if response.status_code != 200:
                error_msg = 'cities_get_by_id: response.status_code = {}, expected 200, city_name = {}'.format(response.status_code, city_name)
                logging.error(error_msg)
                response.failure(error_msg)
                raise RescheduleTask()

            if 'data' not in response_dict:
                error_msg = 'cities_get_by_id: data not in response_dict, city_name = {}'.format(city_name)
                logging.error(error_msg)
                response.failure(error_msg)
                raise RescheduleTask()

            city_name_returned = response_dict['data']['name']
            logging.debug('cities_get_by_id: for city_id = {}, city_name_returned = {}'.format(city_id, city_name_returned))
            
            if city_name_returned != city_name:
                error_msg = 'cities_get_by_id: city_name_returned = {} not equal city_name = {}'.format(city_name_returned, city_name)
                logging.error(error_msg)
                response.failure(error_msg)
                raise RescheduleTask()