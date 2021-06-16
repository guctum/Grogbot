import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

def checkTrackExists(track: str):
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    track_id = re.search('\/\w+\?', track)[0]
    track_id = track_id[1:-1]
    pl_id = 'spotify:playlist:20Cvl99Nqn9yTF2dMyOawr'
    offset = 0

    while True:
        response = sp.playlist_items(pl_id,
                                     offset=offset,
                                     fields='items.track.id,total',
                                     additional_types=['track'])

        if len(response['items']) == 0:
            break

        offset = offset + len(response['items'])
        track_ids = []
        for tracks in response['items']:
            track_ids.append(tracks['track']['id'])

        if track_id in track_ids:
            print("its already here")
        else:
            addTracktoPlaylist(track_id)

scope = "playlist-modify-public"
def addTracktoPlaylist(track: str):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    sp.playlist_add_items("20Cvl99Nqn9yTF2dMyOawr", [track])