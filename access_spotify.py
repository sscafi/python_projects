import spotipy
from spotipy.oauth2 import SpotifyOAuth

# set up authorization flow
auth_manager = SpotifyOAuth(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    redirect_uri='http://localhost:8000/callback',
    scope='user-library-read'
)

# create a Spotipy client using the authorization flow
sp = spotipy.Spotify(auth_manager=auth_manager)

# use the Spotipy client to retrieve information about the user's library
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(f"{idx+1}. {track['name']} by {track['artists'][0]['name']}")
