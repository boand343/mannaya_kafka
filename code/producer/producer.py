from aiokafka import AIOKafkaProducer
import asyncio
import time
import pandas as pd

async def send_one(message):
    producer = AIOKafkaProducer(
        bootstrap_servers='kafka:9092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait("my_topic", message.encode())
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

df = pd.DataFrame({'as': [12,23],
              'fsd': [32, 12]
              })

message = df.to_json(orient="index")

asyncio.run(send_one(message))