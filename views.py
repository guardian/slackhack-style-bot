import json
import logging

from flask import request, Response

import stylebot

def stylebot_chat():
    logging.debug(request.form)
    logging.debug(request.form['text'])
    
    chat_text = request.form['text']
    payload = json.dumps({'text': stylebot.style(chat_text)})

    return Response(response=payload,
        status=200,
        mimetype='application/json')