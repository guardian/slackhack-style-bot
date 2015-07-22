import re

import styleguide

def style(chat_text):
	if re.match(r'picture credit', chat_text):
		return styleguide.p.messages['picture_credit']

	return 'Hello from the Stylebot!'