from flask import Flask
from config import Config

app=Flask(__name__)
app.config.from_object(Config)

#print('Who use me: ',__name__)

from app import routes
