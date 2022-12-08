import pytest as pytest
import requests

from tests.consts import API_URL
from utils.api_models import Brewery, Breweries


class TestEndpoint:
    def test_single_brewery_positive(self):
        request_id = "madtree-brewing-cincinnati"
        uri = f"{API_URL}/{request_id}"
        response = requests.get(uri)
        assert response.status_code == 200
        parsed_response = Brewery.parse_obj(requests.get(uri).json())
        response_id = parsed_response.id
        assert response_id == request_id

    def test_single_brewery_negative(self):
        request_id = "non-existing-id"
        uri = f"{API_URL}/{request_id}"
        response = requests.get(uri)
        assert response.status_code == 404
        parsed_response = response.json()
        assert parsed_response.get("message") == "Couldn't find Brewery"

    @pytest.mark.parametrize("request_length", [1, 2, 50, 51])
    def test_list_breweries_positive(self, request_length):
        max_per_page = 50
        uri = f"{API_URL}?per_page={request_length}"
        response = requests.get(uri)
        assert response.status_code == 200
        parsed_response = Breweries.parse_obj(requests.get(uri).json())
        response_length = len(parsed_response.__root__)
        if request_length < max_per_page + 1:
            assert response_length == request_length
        else:
            assert response_length == max_per_page

    @pytest.mark.parametrize("convert_string", ["san_diego"], indirect=True)
    def test_list_breweries_by_city_positive(self, convert_string):
        request_city = convert_string["orig"]
        expected_city = convert_string["converted"]
        uri = f"{API_URL}?by_city={request_city}"
        response = requests.get(uri)
        assert response.status_code == 200
        parsed_response = Breweries.parse_obj(requests.get(uri).json())
        assert len(parsed_response.__root__) > 0
        for brewery in parsed_response.__root__:
            assert brewery.city == expected_city

    @pytest.mark.parametrize("convert_string", ["new_york"], indirect=True)
    def test_list_breweries_by_state_positive(self, convert_string):
        request_state = convert_string["orig"]
        expected_state = convert_string["converted"]
        uri = f"{API_URL}?by_city={request_state}"
        response = requests.get(uri)
        assert response.status_code == 200
        parsed_response = Breweries.parse_obj(requests.get(uri).json())
        assert len(parsed_response.__root__) > 0
        for brewery in parsed_response.__root__:
            assert brewery.state == expected_state

    def test_list_breweries_negative(self):
        request_length = 0
        uri = f"{API_URL}?per_page={request_length}"
        response = requests.get(uri)
        assert response.status_code == 200
        parsed_response = Breweries.parse_obj(requests.get(uri).json())
        response_length = len(parsed_response.__root__)
        assert response_length == 0

    def test_random_brewery_positive(self):
        uri = f"{API_URL}/random"
        response = requests.get(uri)
        assert response.status_code == 200
        parsed_response = Breweries.parse_obj(requests.get(uri).json())
        response_length = len(parsed_response.__root__)
        assert response_length == 1

    def test_random_brewery_negative(self):
        request_id = "madtree-brewing-cincinnati"
        uri = f"{API_URL}/random/{request_id}"
        assert requests.get(uri).status_code == 404

    def test_search_breweries_positive(self):
        query = "Brewery"
        uri = f"{API_URL}/search?query={query}"
        response = requests.get(uri)
        assert response.status_code == 200
        parsed_response = Breweries.parse_obj(requests.get(uri).json())
        assert len(parsed_response.__root__) > 0
        for brewery in parsed_response.__root__:
            assert query in brewery.name

    def test_search_breweries_negative(self):
        query = "non-existing-name"
        uri = f"{API_URL}/search?query={query}"
        response = requests.get(uri)
        assert response.status_code == 200
        parsed_response = Breweries.parse_obj(requests.get(uri).json())
        assert len(parsed_response.__root__) == 0
