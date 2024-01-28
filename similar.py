import spotipy
from spotipy.oauth2 import SpotifyOAuth

# AUTH
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# get artist
print("This will create a playlist of similar artists top songs")
artist = input("Pick an artist: ")
get_artist = sp.search(q=artist, type='artist', limit=1)
artist_id = get_artist['artists']['items']

# check if artist exists
if (len(artist_id) == 0):
    print("They do not exist")

else:

    # how many tracks and make sure its a valid amount
    amount_tracks = int(input("How many tracks from each artist would you like: "))
    while(amount_tracks < 1 or amount_tracks > 5):
        if (amount_tracks > 5):
            print("The limit is 5")
            amount_tracks = int(input("How many tracks from each artist would you like: "))
        else:
            print("Funny guy eh")
            amount_tracks = int(input("How many tracks from each artist would you like: "))

    # create a new playlist
    playlist_name = "Similar Artists to " + artist
    playlist_description = "playlist of similar artists top songs related to " + artist
    user_id = sp.me()["id"]
    new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, collaborative = False, description=playlist_description)

    # get id of artist
    artist_id = artist_id[0]['id']

    # get related artists
    related_artists = sp.artist_related_artists(artist_id)

    # find related artists top tracks and add them to new playlist
    for i in related_artists['artists']:
        top_tracks = sp.artist_top_tracks(i['id'])['tracks'][: + int(amount_tracks)]
        for t in top_tracks:
            sp.playlist_add_items(new_playlist['id'], [t['uri']])

    print("Done")
        
    

