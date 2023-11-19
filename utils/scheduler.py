from apscheduler.schedulers.background import BackgroundScheduler

from models.event import Event


class Scheduler:
    def __init__(self):
        self.time_between_cycles = 5
        self.scheduler = BackgroundScheduler()

    def schedule_jobs(self, event: Event):
        self.scheduler.add_job(event.trigger, 'cron', minute='*')

    def start_scheduler(self):
        # Start the scheduler in the background
        self.scheduler.start()

    def stop_scheduler(self):
        # Shut down the scheduler gracefully when needed
        self.scheduler.shutdown()
