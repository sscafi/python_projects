import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Prompt the user to authenticate with their Spotify account
scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Get the user's saved tracks
tracks = sp.current_user_saved_tracks(limit=50)  # Adjust the limit as needed

# Create a list to hold track details
track_details = []

# Retrieve details for each track
for item in tracks["items"]:
    track = item["track"]
    track_id = track["id"]
    track_name = track["name"]
    
    # Get audio features for the track
    audio_features = sp.audio_features([track_id])
    bpm = audio_features[0]["tempo"]
    
    # Append track details to the list
    track_details.append((track_name, bpm))

# Sort tracks based on BPM
sorted_tracks = sorted(track_details, key=lambda item: item[1])

# Print the sorted tracks
print("Sorted tracks based on BPM:")
for i, track in enumerate(sorted_tracks):
    print(f"{i+1}. {track[0]} (BPM: {track[1]})")
