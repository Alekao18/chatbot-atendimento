import redis
import os
from dotenv import load_dotenv

load_dotenv()

r = redis.Redis(
    host= 'redis-12006.c345.samerica-east1-1.gce.redns.redis-cloud.com',
    port=12006,
    decode_responses=True,
    username='default',
    password='fs78GWzQYCeVVG9jMUYjiqXnPprjJAfb',
)






