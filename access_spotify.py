import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify authorization flow using SpotifyOAuth
auth_manager = SpotifyOAuth(
    client_id='YOUR_CLIENT_ID',             # Replace with your Spotify client ID
    client_secret='YOUR_CLIENT_SECRET',     # Replace with your Spotify client secret
    redirect_uri='http://localhost:8000/callback',  # Redirect URI after authorization
    scope='user-library-read'               # Scope of access required (read user's library)
)

# Create a Spotipy client using the authorization flow
sp = spotipy.Spotify(auth_manager=auth_manager)

# Use the Spotipy client to retrieve information about the user's library
results = sp.current_user_saved_tracks()

# Print out tracks in the user's library
for idx, item in enumerate(results['items']):
    track = item['track']
    print(f"{idx+1}. {track['name']} by {track['artists'][0]['name']}")
