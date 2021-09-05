from flask import Flask

app=Flask(__name__)

print('Who use me: ',__name__)

from app import routes
