import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# AUTH
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# input year
acc = 0
year = int(input("What year would you like to go back to: "))
while (year >= 2024 or year < 1930):
    print("We got a funny guy here")
    year = int(input("Acutally what year: "))
    acc = acc + 1
    if (acc == 5):
        print("dam bro you good?")

# suggest genres and input genre
with open('genres.txt') as f:
    genres = f.readlines()
genres = [i.strip() for i in genres if i.strip()]
num_of_genres = 7
random_genres = [i.title() for i in random.sample(genres, num_of_genres)]
print("Here are some random generes: ")
for i in random_genres:
    print(i)
genre = input("What genre would you like: ")


# search for most popular songs in year and genre
results = sp.search(q='genre:"{}" year:{}'.format(genre, year), type='track', limit=50)
tracks = results['tracks']['items']

if (len(tracks) == 0):
    print("Dam I guess they didn't make " + genre + " in " + str(year))

else:
    # sort tracks by pop
    sorted_tracks = sorted(tracks, key=lambda x: x['popularity'], reverse=True)

    # create a new playlist
    playlist_name = str(year) + "s " + genre + "s Greatest Hits"
    playlist_description = "greatest hits from " + genre + " in " + str(year) 
    user_id = sp.me()["id"]
    new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, collaborative = False, description=playlist_description)

    # add the tracks to the playlist
    track_uris = [track['uri'] for track in sorted_tracks]
    sp.playlist_add_items(new_playlist['id'], track_uris)

    print("Done")






