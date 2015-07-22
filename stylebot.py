import re

import styleguide

def style(chat_text):
	for key_text, message_key in [
		(r'picture credit', 'picture_credit'),
		(r'about$', 'about'),
	]:
		if re.search(key_text, chat_text):
			return styleguide.messages.get(message_key, "I'm afraid I don't know about that (but I should)")

	return "Hi there! I didn't understand you, sorry!"