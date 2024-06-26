from apscheduler.schedulers.background import BackgroundScheduler 
from motivate import send_whatsapp_text, client, quote
import time

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()

job = scheduler.add_job(send_whatsapp_text, 'cron', [client,quote], hour="17", minute="25")
print(job)

while True:
    time.sleep(1)

