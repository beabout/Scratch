#!/usr/local/bin/python3
# install: `pip3 install spotipy`

import spotipy
import json
import os 
from spotipy.oauth2 import SpotifyOAuth
from albums.models import Album
from artists.models import Artist

CLIENT_ID="fed1c759d0d140f591fddf0ba2689b1b"
APP_CLIENT_SECRET="f6f6949144314e42922272839a6370fb"
APP_REDIRECT_URI="http://localhost:3000/discography"

def run(*args):
  offset = 0
  sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                  client_secret=APP_CLIENT_SECRET,
                                                  redirect_uri=APP_REDIRECT_URI,
                                                  scope="user-library-read"))

  print("running spotify script. creating albums")

  while True:
    print("fetching albums")
    result = sp.current_user_saved_albums(limit=50, offset=offset)
    
    for album in map(lambda x: x['album'], result['items']):
      a = Album( 
        title=album['name'],
        spotify_id=album['id'],
        cover_url=album['images'][0]['url'],
        total_tracks=album['total_tracks'],
        release_date=album['release_date']
      )
      a.save()

    offset += 50

    if len(result['items']) < 50:
      break
