import requests
import json


curr_token = "BQCTV2XY3FgntKRJ4SGcC_X2PCyJUHq_ocXQJcV9XVCotgnHnflLFXip52r7AQjjNR7uNTaVr-QL31mkI9oFMF6i2F9SbvenzxyArsyGDShT7Jw1uhXxyz44P5topiwMk4awIifNIpmyP66JojkF5Sc4qNuAT3hY1cClyc4u8RNewVKJLCuZywlpCnt-04pB-qhy2xR13eDVLewVwQBgjqjPZZSDQg"


# get users playlists
user = "snoykbalfniff2voe2xv8f16o"
up_endpoint = "https://api.spotify.com/v1/users/%s/playlists"% user

r = requests.get(up_endpoint, headers={'Authorization':f'Bearer {curr_token}'})
format = json.loads(r.content)
output = json.dumps(format, indent=2)
# print(output)


# getting liked songs (in the works)
uls_endpoint = "https://api.spotify.com/v1/me/tracks?limit=50"

r = requests.get(uls_endpoint, headers={'Authorization':f'Bearer {curr_token}'})
format = json.loads(r.content)
output = json.dumps(format, indent=2)
# print(output)

# get playlist items
upi_endpoint = "https://api.spotify.com/v1/playlists/1JR6170N1MBG3riDlMUEZl/tracks"

r = requests.get(upi_endpoint, headers={'Authorization':f'Bearer {curr_token}'})

format = json.loads(r.content)

print(format['items'][2]['track']['artists'])

for i in range(len(format['items'])):
    pass
    # print(format['items'][i]['track']['artists'][0]['name'])