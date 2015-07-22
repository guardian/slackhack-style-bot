import json

from flask import Flask

import views

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: 'Stylebot HQ'))

application.add_url_rule('/stylebot', 'stylebot',
    view_func=views.stylebot_chat,
    methods=['GET', 'POST'])

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
