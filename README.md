# SpotifyBaysTop40Importer
Import Bay's top 40 list

This application scrapes the bay's Top 40 list and adds them to a spotify playlist of your choice

You will need to install:
* pip install spotipy  (Client that accesses spotify)
* pipi nstall bs4       (HTML scaper)

#Setup
Replace these variables:
* client_id       = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
* client_secret   = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
* redirect_uri    = 'http://localhost:8080'
* playlistName    = 'Top 40'

Remember to get the client_id and client_secret you will need to register here:
	https://developer.spotify.com/dashboard/applications