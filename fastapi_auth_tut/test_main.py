from fastapi.testclient import TestClient
from main import app
from unittest.mock import MagicMock

client = TestClient(app)


def test_read_test_route():
    response = client.get('/test')
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "status": "success",
        "message": "response returned successfully",
        "data": [[
            1391040000,
            "٨۰٢.٨٥١٤٣٦٩٩۰٢٢٢٢"
        ],
            [
            1390953600,
            "٧٩٤.٦٩٤٩٤٢٥٣٧٣٣٣٣"
        ]]
    }
    assert response.status_code == 200
    assert response.json()['status'] == mock_response.json.return_value['status']
    assert response.json()['message'] == mock_response.json.return_value['message']
    assert response.json()['data'][0] in mock_response.json.return_value['data']
