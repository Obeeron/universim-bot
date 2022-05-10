import asyncio

loop = asyncio.get_event_loop()

async def periodic(period, fun):
    while True:
        try:
            await fun()
        except Exception as e:
            print(e)
        await asyncio.sleep(period)

def addPeriodic(period, fun):
    loop.create_task(periodic(period, fun))
    print("Periodic task added with period " + str(period)+ "s")