# save this as app.py
import time
from datetime import datetime

import flask
from flask import Flask, abort
from pydantic import BaseModel, Field

class Message(BaseModel):
    name: str = Field(min_length=1)
    text: str = Field(min_length=1)

app = Flask(__name__)
db = []
uniqueUsers = set()

for i in range(3):
    db.append({
        'name': 'Anton',
        'time': 12343,
        'text': 'text01923097'
    })

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/send", methods= ['POST'])
def send_message():
    '''
    функция для отправки нового сообщения пользователем
    :return:
    '''
    # TODO
    # проверить, является ли присланное пользователем правильным json-объектом
    # проверить, есть ли там имя и текст

    data = flask.request.json
    try:
        Message(**data)
    except ValueError:    
        return abort(400)


    text = data['text']
    name = data['name']

    if name not in uniqueUsers:
        uniqueUsers.add(name)

    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)
    return {'ok': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        abort(400)
    db_after = []
    for message in db:
        if message['time'] > after:
            db_after.append(message)
    return {'messages': db_after}

@app.route("/status")
def print_status():
    t = time.time()
    dt = datetime.fromtimestamp(t)
    return {

       "messagesCount": len(db),
       "date": dt.strftime('%Y-%m-%d %H:%M:%S'),
       "uniqueUsers": len(uniqueUsers)
    }

@app.route('/index')
def lionel(): 
    return flask.render_template('index.html')

app.run()