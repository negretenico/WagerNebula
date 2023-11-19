from typing import Final, NamedTuple

BASE_URL: Final[str] = "http://site.api.espn.com/apis/site/v2/sports"
SCORES: Final[str] = "scoreboard"
TEAMS: Final[str] = "teams"


class ESPN(NamedTuple):
    scores: str
    teams: str


class ESPNMapping(NamedTuple):
    NBA: ESPN
    NCAA_FOOTBALL: ESPN
    NFL: ESPN


MAPPING: Final[ESPNMapping] = ESPNMapping(
    NBA=ESPN(scores=f"{BASE_URL}/basketball/nba/{SCORES}", teams=f"{BASE_URL}/basketball/nba/{TEAMS}"),
    NCAA_FOOTBALL=ESPN(scores=f"{BASE_URL}/football/college-football/{SCORES}",
                       teams=f"{BASE_URL}/football/college-football/{TEAMS}"),
    # TODO: fix the fact that we are limiting the response to 10 teams here only
    NFL=ESPN(scores=f"{BASE_URL}/football/nfl/{SCORES}",
             teams=f"{BASE_URL}/football/nfl/{TEAMS}?limit=10"),
)
