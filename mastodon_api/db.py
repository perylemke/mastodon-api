# pylint: disable=invalid-name
import motor.motor_asyncio
from decouple import config


MONGO_URI = config('DB_URI', default='localhost', cast=str)
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
mastodondb = client.mastodondb
