from mastodon import Mastodon
import os

# Register app - run this script just one to get your credentiels (that's the file pytooter_clientcred.txt)


Mastodon.create_app(
     'MastodonDistantReading',
     scopes = ['read'],
      to_file = 'pytooter_clientcred.txt'
)

#Create the directory to store the json files

if not os.path.exists("mastodon_corpus"):
    os.makedirs("mastodon_corpus")