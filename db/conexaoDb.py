import redis
from pymongo import MongoClient
from pymongo.server_api import ServerApi

redis_client = redis.StrictRedis(host='redis-18603.c244.us-east-1-2.ec2.redns.redis-cloud.com', port=18603, db=0, password="UMATpkRDSPKbmLfSCdhwMYaElmnp9xaF")

url = "mongodb+srv://Erika:erika@cluster0.1ghhl.mongodb.net/"
client = MongoClient(url, server_api=ServerApi("1"))
db = client.MercadoLivre