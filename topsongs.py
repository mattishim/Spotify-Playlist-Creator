import spotipy
from spotipy.oauth2 import SpotifyOAuth

# AUTH
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Get inputted playlist data
print("THIS CREATE A NEW PLAYLIST OF ARTISTS TOP SONGS")
input_playlist = input("Enter your playlist: ")
amount_tracks = input("How many tracks from each artists: ")
get_playlist_id = sp.search(q=input_playlist, type='playlist')
playlist_found = get_playlist_id['playlists']['items'][0]['id']
playlist_tracks = sp.playlist_tracks(playlist_found, fields='items(track(artists(name,id)))')

# append all artist top tracks to a list
artists_names = []
top_tracks = []
for tracks in playlist_tracks['items']:
    for artist in tracks['track']['artists']:
        artist_name = artist['name']
        if artist_name not in artists_names:
            artist_id = artist['id']
            artists_names.append(artist_name)
            top_tracks.append(sp.artist_top_tracks(artist_id)['tracks'][: + int(amount_tracks)])


# Create a new playlist
playlist = input_playlist
playlist_name = playlist + " V2"
playlist_description = "these are the top 3 songs from all of the artists in the playlist " + playlist
user_id = sp.me()["id"]
new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, collaborative = False, description=playlist_description)

# add tracks
added_tracks = set()
for tracks in top_tracks:
    track_uris = [track['uri'] for track in tracks if track['uri'] not in added_tracks]
    added_tracks.update([t['uri'] for t in tracks])
    sp.playlist_add_items(new_playlist['id'], track_uris)

print("Done")