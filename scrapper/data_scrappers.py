import requests

from models.result import Result
from models.result_builder import ResultBuilder


def get_data(url: str) -> Result:
    try:
        response = requests.get(url)
        if response.status_code >= 300:
            return ResultBuilder.error(response.text).build()
        return ResultBuilder.data(response.json()).build()
    except Exception as e:
        print(e)
        return ResultBuilder.error(f"Error {e} occurred while making request to {url}").build()
