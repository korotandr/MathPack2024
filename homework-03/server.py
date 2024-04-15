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

    t = time.time()
    dt = datetime.fromtimestamp(t)
    message = {
        'text': text,
        'name': name,
        'time': dt.strftime('%Y-%m-%d %H:%M:%S')
    }
    db.append(message)
    return {'ok': True}

@app.route("/messages")
def get_messages():
    context = {}
    context['messages'] = db
    return flask.render_template('messages.html', context = context)

@app.route("/status")
def print_status():
    t = time.time()
    dt = datetime.fromtimestamp(t)
    info = {

       "messagesCount": len(db),
       "date": dt.strftime('%Y-%m-%d %H:%M:%S'),
       "uniqueUsers": len(uniqueUsers)
    }
    return flask.render_template('status.html', info = info)

app.run()