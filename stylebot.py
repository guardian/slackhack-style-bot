import re

import styleguide

def style(chat_text):
	for key_text, message_key in [
		(r'picture credit', 'picture_credit'),
	]:
		if re.search(key_text, chat_text):
			return styleguide.messages[message_key]

	return 'Hello from the Stylebot!'