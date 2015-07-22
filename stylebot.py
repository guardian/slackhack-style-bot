import re

import styleguide

def style(chat_text):
	if re.search(r'picture credit', chat_text):
		return styleguide.p.messages['picture_credit']

	return 'Hello from the Stylebot!'