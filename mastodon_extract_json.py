import json, os
from pprint import pprint 
import xml.etree
from bs4 import BeautifulSoup
import re

toot_csv_header = '"toot_id";"content";"created_at";"toot_in_reply_to_account_id";"toot_in_reply_to_id";"toot_favourites_count";"toot_reblogs_count";"toot_sensitive";"toot_spoiler_text";"account";"account_created_at";"account_followers";"account_follows";"account_status";"account_note";"account_id";"toot_mentions_id";"toot_mentions_account"\n'

toot_content_csv = []


def remove_tags(text):
	text = BeautifulSoup(text, "html5lib")
	text = text.get_text()
	text = re.sub(r'"', r'', text)
	text = re.sub(r'\n', r' ', text)
	return(text)

for dirs, subdirs, files in os.walk("mastodon_corpus"):
	for file in files:
		file = "mastodon_corpus/" + file
		print(file)
		with open(file) as json_data:
			d = json.load(json_data)
			for toot in d:
				account = toot['account']['acct']
				account_created_at = toot['account']['created_at']
				account_followers = toot['account']['followers_count']
				account_follows = toot['account']['following_count']
				account_status = toot['account']['statuses_count']
				account_note = toot['account']['note']
				account_note = remove_tags(account_note)
				account_id = toot['account']['id']
				content = toot['content']
				content = remove_tags(content)
				created_at = toot["created_at"]
				toot_id = toot["id"]
				toot_in_reply_to_account_id = toot["in_reply_to_account_id"]
				toot_in_reply_to_id = toot["in_reply_to_account_id"]
				toot_favourites_count = toot["favourites_count"]
				toot_reblogs_count = toot["reblogs_count"]
				toot_sensitive = toot["sensitive"]
				toot_spoiler_text = toot["spoiler_text"]
				toot_spoiler_text = remove_tags(toot_spoiler_text)
				if not toot["mentions"]:
					toot_mentions_id = "None"
					toot_mentions_account = "None"
				else:
					toot_mentions_id = []
					toot_mentions_account = []
					for element in toot["mentions"]:
						toot_mentions_id.append(str(element["id"]))
						toot_mentions_account.append(str(element["acct"]))
					toot_mentions_id = ", ".join(toot_mentions_id)
					toot_mentions_account = ", ".join(toot_mentions_account)
				toot_full = '"' + str(toot_id) + '";"' + str(content) + '";"' + str(created_at) + '";"' + str(toot_in_reply_to_account_id) + '";"' + str(toot_in_reply_to_id) + '";"' + str(toot_favourites_count) + '";"' + str(toot_reblogs_count) + '";"' + str(toot_sensitive) + '";"' + str(toot_spoiler_text) + '";"' + str(account) + '";"' + str(account_created_at) + '";"' + str(account_followers) + '";"' + str(account_follows) + '";"' + str(account_status) + '";"' + str(account_note) + '";"' + str(account_id) + '";"' + str(toot_mentions_id) + '";"' + str(toot_mentions_account) + '"'
				toot_content_csv.append(toot_full)


toot_csv = toot_csv_header + "\n".join(toot_content_csv)

toot_csv_file = open("toot_complete.csv", 'w')

toot_csv_file.write(toot_csv)
