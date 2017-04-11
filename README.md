# MastodonCulturalGenesis

This repository stores the text, file and data of a small data mining project on the public timeline of Mastodon (see http://vintagedata.org/mastodon/cultural_genesis_1.html)

cultural_genesis_1.Rmd is the R notebook file that served to generate the main text.

Three python files has served to import the data from the Mastodon API and can easily be reused for similar projects: create_mastodon_app.py (to get the credentials to access the API and to initiate a directory for the Mastodon corpus), mastodon_retrieve_API.py (to launch a descending loop through the public timeline) and mastodon_extract_json.py (to parse the json files in the directory corpus).

mastodon_interactions.csv is the dataset used for the R notebook. It includes only some key information to document the interactions between users. Besides, the name of the users have been replaced by ids.
