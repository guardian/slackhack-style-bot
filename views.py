import json

from flask import request, Response

import stylebot

def stylebot_chat():
    chat_text = request.form['text']
    payload = json.dumps({'text': stylebot.style(chat_text)})

    return Response(response=payload,
        status=200,
        mimetype='application/json')