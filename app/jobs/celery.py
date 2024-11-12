from celery import Celery

app = Celery('app', broker='redis:localhost:6379/0')
timezone = 'UTC'

@app.on_after_configure.connect
def setup_schedule(sender, **kwargs):
    sender.add_periodic_task(
        crontab("0", "0", "*", "*", "*"), #каждый день 
        parse_sulpak.s()
    )

@app.task
def parse_sulpak():
    return True