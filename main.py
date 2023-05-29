import asyncio
from datetime import date
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

birthday = date(2023, 6, 29)

async def send_special_notification():
    print("с днем рождения!")

def check_special_day():
    today = date.today()
    return today == birthday

@scheduler.scheduled_job('cron', day='*', hour=0, minute=0, second=0)
async def check_and_send_notification():
    if check_special_day():
        await send_special_notification()

scheduler.start()

loop = asyncio.get_event_loop()
loop.run_forever()
