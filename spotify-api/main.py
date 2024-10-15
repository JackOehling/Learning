import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

curr_token = os.getenv("KEY")

# print(curr_token)

# get users playlists
def get_user_playlists(user):
    user = "snoykbalfniff2voe2xv8f16o"
    up_endpoint = "https://api.spotify.com/v1/users/%s/playlists"% user

    r = requests.get(up_endpoint, headers={'Authorization':f'Bearer {curr_token}'})
    format = json.loads(r.content)
    output = json.dumps(format, indent=2)
    # print(output)

# getting liked songs (in the works)
def get_liked_songs(limit):
    uls_endpoint = "https://api.spotify.com/v1/me/tracks?limit=50"

    r = requests.get(uls_endpoint, headers={'Authorization':f'Bearer {curr_token}'})
    format = json.loads(r.content)
    output = json.dumps(format, indent=2)
    # print(output)

# get playlist items
def get_playlist_items(playlist_id):
    upi_endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    r = requests.get(upi_endpoint, headers={'Authorization':f'Bearer {curr_token}'})
    format = json.loads(r.content)
    return format

# create a playlist
def create_playlist(name, description, public):
    user_id = ""
    endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    content = """{
    "name": "%s",
    "description": "%s",
    "public": "%s"
    }
    """ % (name, description, public)
    r = requests.post(endpoint, headers={'Authorization':f'Bearer {curr_token}', 'Content-Type': 'application/json'}, data=content)
    return r

# adds songs to playlist
def add_items(playlist_id, uris, position):
    endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    content = """{
    "uris" : %s,
    position : %s
    }""" (uris, position)
    r = requests.post(endpoint, headers={'Authorization':f'Bearer {curr_token}', 'Content-Type': 'application/json'}, data=content)


# adds songs to playlist
def delete_playlist(playlist_id):
    endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/followers"
    r = requests.delete(endpoint, headers={'Authorization':f'Bearer {curr_token}'})


# # add items to playlist
# playlist_id = ""
# aitp_endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

# content = """{
# "uris" : [spotify:track:4iV5W9uYEdYUVa79Axb7Rh, spotify:track:1301WleyT98MSxVHPZCA6M, spotify:episode:512ojhOuo1ktJprKbVcKyQ],
# position : 0
# }
# """
# r = r = requests.post(upi_endpoint, headers={'Authorization':f'Bearer {curr_token}', 'Content-Type': 'application/json'}, data=content)

playlist_id = "1JR6170N1MBG3riDlMUEZl"
format = get_playlist_items(playlist_id)

songs_by_artist = {}
for i in range(len(format['items'])):
    song_artists = format['items'][i]['track']['artists']
    song_id = format['items'][i]['track']['id']
    
    artist_amount = len(format['items'][i]['track']['artists'])
    for j in range(artist_amount):
        artist = song_artists[j]['name']
        songs_by_artist[artist] = song_id

print(songs_by_artist)

artist_to_playlist = {}
for artist in songs_by_artist:
    # create playlist from artist name
    playlist_response_json = create_playlist(artist, f"{artist} playlist")
    playlist_response = json.loads(playlist_response_json)
    playlist_id = playlist_response['id']
    artist_to_playlist['artist'] = playlist_id
    # add to playlist
    uris = []
    for songs in songs_by_artist[artist]:
        uri = "spotify:track:" + songs
        uris.append(uri)
    add_items(playlist_id, uris, 0)

should_delete = input("delete?")



    
        



