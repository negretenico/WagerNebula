from logging import info, basicConfig, INFO

from data.api_mappings import MAPPING
from models.timed_event import TimedEvent
from scrapper.data_scrappers import get_data
from utils.scheduler import Scheduler

basicConfig(level=INFO)


def main():
    scheduler_instance = Scheduler()
    for key, item in MAPPING._asdict().items():
        info(f"Adding org {key} to the schedule")
        scheduler_instance.schedule_jobs(TimedEvent(get_data, item.teams))
        scheduler_instance.schedule_jobs(TimedEvent(get_data, item.scores))
    scheduler_instance.start_scheduler()

    try:
        while True:
            pass

    except (KeyboardInterrupt, SystemExit):
        # Shut down the scheduler gracefully when the program is interrupted
        scheduler_instance.stop_scheduler()


if __name__ == "__main__":
    main()
