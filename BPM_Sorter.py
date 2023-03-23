import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# set up credentials
client_credentials_manager = SpotifyClientCredentials(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# search for tracks
results = sp.search(q='year:2022', type='track', limit=50)

# create list of tuples containing track ID and BPM
tracks = []
for item in results['tracks']['items']:
    track_id = item['id']
    track_features = sp.audio_features(track_id)[0]
    track_bpm = track_features['tempo']
    tracks.append((track_id, track_bpm))

# sort tracks by BPM
sorted_tracks = sorted(tracks, key=lambda x: x[1])

# print out sorted track IDs and their BPMs
for track in sorted_tracks:
    print(track[0], track[1])
