# Create a New Playlist Featuring the Biggest Songs from Every Artist in a User-Selected Playlist.
This Python script takes in a user's playlist and creates a new playlist with every artist in the given playlist, adding their top 3 songs to the new playlist.

## Prerequisites
Python 3.x

Spotipy Module

Spotify Account with Developer Access

### Setup
1. Clone the repository and navigate to the python-testing directory.

2. Install the spotipy module using the following command: ```pip install spotipy --upgrade```

3. Follow the instructions in the Spotify Developer Dashboard to create a new app and retrieve a client ID and client secret. In your settings for your app you can add this to your redirect url: ```https://localhost:8000/callback```

4. In the python-testing directory, create a new file called .env and add the following lines, replacing CLIENT_ID and CLIENT_SECRET with your actual client ID and secret.

```python
SPOTIPY_CLIENT_ID=CLIENT_ID
SPOTIPY_CLIENT_SECRET=CLIENT_SECRET
SPOTIPY_REDIRECT_URI=https://localhost:8000/callback
```

5. Run the script using the following command: ```python topsongs.py```

### Usage
1. Enter the name of the playlist you want to use as input when prompted.

2. Enter the number of top tracks you want to add for each artist when prompted.

3. A new playlist will be created in your Spotify account with the name of your inputed playlist V2, containing the top tracks for all the artists in the original playlist.

# Create a Spotify Playlist of Top 50 Most Popular Songs from a slected Year and Genre
This Python script takes in a certain year and genre, and creates a playlist based on the top songs in the given year and genre

## Prerequisites
Python 3.x

Spotipy Module

Spotify Account with Developer Access

### Setup
1. Clone the repository and navigate to the python-testing directory.

2. Install the spotipy module using the following command: ```pip install spotipy --upgrade```

3. Follow the instructions in the Spotify Developer Dashboard to create a new app and retrieve a client ID and client secret. In your settings for your app you can add this to your redirect url: ```https://localhost:8000/callback```

4. In the python-testing directory, create a new file called .env and add the following lines, replacing CLIENT_ID and CLIENT_SECRET with your actual client ID and secret. (Skip this step if already done)

```python
SPOTIPY_CLIENT_ID=CLIENT_ID
SPOTIPY_CLIENT_SECRET=CLIENT_SECRET
SPOTIPY_REDIRECT_URI=https://localhost:8000/callback
```

5. Run the script using the following command: ```python yearandgenre.py```

### Usage
1. Enter the year and genre you want to use when prompted. (It will reccomend random ones if you can't think of any)

2. A new playlist will be created in your Spotify account with the name Genre Year Playlist, containing the top songs in the given genre for the given year.

# Create a New Playlist Featuring Related Artists Top Songs.
This Python script takes in a artist of your choice and makes a playlsit around similar artists, using their top songs.

## Prerequisites
Python 3.x

Spotipy Module

Spotify Account with Developer Access

### Setup
1. Clone the repository and navigate to the python-testing directory.

2. Install the spotipy module using the following command: ```pip install spotipy --upgrade```

3. Follow the instructions in the Spotify Developer Dashboard to create a new app and retrieve a client ID and client secret. In your settings for your app you can add this to your redirect url: ```https://localhost:8000/callback```

4. In the python-testing directory, create a new file called .env and add the following lines, replacing CLIENT_ID and CLIENT_SECRET with your actual client ID and secret.

```python
SPOTIPY_CLIENT_ID=CLIENT_ID
SPOTIPY_CLIENT_SECRET=CLIENT_SECRET
SPOTIPY_REDIRECT_URI=https://localhost:8000/callback
```

5. Run the script using the following command: ```python similar.py```

### Usage
1. Enter the name of the artist you want to use when prompted.

2. Enter the number of top tracks you want to add for each artist when prompted.

3. A new playlist will be created in your Spotify account with the name Similar Artists to whatever you entered, containing the top tracks for all the similar artists.
