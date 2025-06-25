import redis 


import redis

r = redis.Redis(
    host='redis-12006.c345.southamerica-east1-1.gce.redns.redis-cloud.com',
    port=12006,
    username='usrchatbot',  # ou o que estiver configurado
    password='Usrchatbot25@',  # substitua pela senha criada
    ssl=True
)


