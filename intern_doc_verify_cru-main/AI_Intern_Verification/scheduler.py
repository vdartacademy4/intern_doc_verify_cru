from apscheduler.schedulers.background import BackgroundScheduler
import time

from email_fetcher import fetch_emails
import app

def job():

    print("\n[ SCHEDULER ] Checking emails...")

    files = fetch_emails()

    if files:

        print("New files found:", files)

        try:

            app.run_pipeline()

        except Exception as e:

            print("\nPipeline Error:")
            print(e)

    else:

        print("No new emails")

# -------------------------
# START SCHEDULER
# -------------------------
scheduler = BackgroundScheduler()

scheduler.add_job(
    job,
    'interval',
    minutes=2,
    max_instances=1
)

scheduler.start()

print("Scheduler started...")

try:

    while True:
        time.sleep(5)

except KeyboardInterrupt:

    print("\nStopping Scheduler...")

    scheduler.shutdown()

    print("Scheduler Stopped.") 