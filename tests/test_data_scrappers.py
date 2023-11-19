import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock

from models.result import Result
from scrapper.data_scrappers import get_data


def check_equality(error, data, result: Result) -> bool:
    return result.data() == data and result.error() == error


class Test(TestCase):

    @patch('requests.get', side_effect=Exception("Simulated error"))
    def test_when_request_throws_error_then_I_get_that_error_has_a_result(self, _):
        result = get_data("someUrl")
        self.assertTrue(check_equality("Error Simulated error occurred while making request to someUrl", None, result),
                        "Matches")
        self.assertTrue(result.failed())

    @patch('requests.get')
    def test_when_request_gives_a_bad_status_code_then_I_should_get_an_error(self, mock_request_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "some error message"
        mock_request_get.return_value = mock_response
        result = get_data("someUrl")
        self.assertTrue(check_equality("some error message", None, result),
                        f"Could not find match\nerror =>{result.error()}:some error message\ndata=> {result.data()}:None")
        self.assertTrue(result.failed())

    @patch("requests.get")
    def test_when_request_is_successful_then_I_get_a_proper_result(self, mock_request_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = "foo"
        mock_request_get.return_value = mock_response
        result = get_data("someUrl")
        self.assertTrue(check_equality(None, "foo", result))
        self.assertTrue(result.success())


if __name__ == "__main__":
    unittest.main()
