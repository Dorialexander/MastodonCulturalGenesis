from mastodon import Mastodon
import json
import time

# You have to run first the create_mastodon_app.py script once to create your credentials.

mastodon = Mastodon(client_id = 'pytooter_clientcred.txt', ratelimit_method='pace')

last_id = "1746946"

for passing in range(0,100):
	try:
		print("getting the mastodon timeline json")
		timeline_mastodon = mastodon.timeline_public(max_id = last_id)
		json_mastodon = json.dumps(timeline_mastodon)
		last_id = timeline_mastodon[len(timeline_mastodon)-1]["id"]
		print("last stop at toot id " + str(last_id))
		json_title = "mastodon_corpus/" + str(last_id) + ".json"
		json_save_mastodon = open(json_title, 'w')
		json_save_mastodon.write(json_mastodon)
	except:
		print("API error, waiting a bit to see what happens")
		time.sleep(10)
'''