from data.api_mappings import MAPPING, ESPN
from models.result import Result
from scrapper.data_scrappers import get_data


def query(item: ESPN) -> (Result, Result):
    return get_data(item.teams), get_data(item.scores)


def main():
    for key, value in MAPPING._asdict().items():
        print(f"TEAMS for {key} resulted in {query(value)[0].success()}")
        print(f"SCORES for {key} resulted in {query(value)[1].success()}")


if __name__ == "__main__":
    main()
