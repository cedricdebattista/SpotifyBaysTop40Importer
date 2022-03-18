import spotipy
from spotipy.oauth2 import SpotifyOAuth

import bs4
from bs4 import BeautifulSoup

import requests

#Variables
bay_top_40_url  = 'https://bay.com.mt/top40/'

client_id       = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client_secret   = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
redirect_uri    = 'http://localhost:8080'

playlistName    = 'Top 40'


#Connect to Bay's Top 40 and get the list
response = requests.get(bay_top_40_url)
print (response.status_code)
html = response.content

soup = BeautifulSoup(html)

repElemList  = soup.find_all('iframe')

my_list = []

for repElem in repElemList:
    repElemID = repElem.get('src')

    if(repElemID != 'about:blank'):
        re = repElemID.replace("https://open.spotify.com/embed/track/", "").replace("?utm_source=generator", "")
        print("Attribute src = %s" % re)
        my_list.append(re)
    


#Authenticate to spotify
scope = "user-library-read"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,client_secret,redirect_uri,None, 'playlist-modify-private,playlist-read-private,playlist-read-collaborative,playlist-modify-public'))


#Find the playlist id
playlistId = ''

playlists = spotify.current_user_playlists()

while playlists:
    for i, playlist in enumerate(playlists['items']):
        if( playlist['name']==playlistName):
            playlistId= playlist['uri']

    if playlists['next']:
        playlists = spotify.next(playlists)
    else:
        playlists = None



#Add the tracks to the playlist
currentuser = spotify.current_user()

spotify.user_playlist_remove_all_occurrences_of_tracks(currentuser, playlistId,my_list)
spotify.user_playlist_add_tracks(currentuser['id'], playlist_id=playlistId, tracks=my_list)



#Read the playlist tracks
playlist = spotify.playlist(playlistId)

for i, playlist in enumerate(playlist['tracks']["items"]):
        print("%s %s %s" % (playlist['track']["track_number"], playlist['track']["id"],  playlist['track']["name"]))


