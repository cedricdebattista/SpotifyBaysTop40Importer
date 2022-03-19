import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyBuilder:
    def authenticate(self,client_id, client_secret, redirect_uri):
        #Authenticate to spotify
        scope = "user-library-read"
        self.spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(client_id,client_secret,redirect_uri,None, 
            'playlist-modify-private,playlist-read-private,playlist-read-collaborative,playlist-modify-public'))

        return self

    def import_tracks_to_playlist(self,playlist_name, tracks):
        #Find the playlist id
        playlistId = ''

        playlists = self.spotify.current_user_playlists()

        while playlists:
            for i, playlist in enumerate(playlists['items']):
                if( playlist['name']==playlist_name):
                    playlistId= playlist['uri']

            if playlists['next']:
                playlists = self.spotify.next(playlists)
            else:
                playlists = None



        #Add the tracks to the playlist
        currentuser = self.spotify.current_user()

        #Read the playlist tracks
        current_track_list = []
        playlist = self.spotify.playlist(playlistId)
        for i, playlist in enumerate(playlist['tracks']["items"]):
            current_track_list.append(playlist['track']["id"])



        self.spotify.user_playlist_remove_all_occurrences_of_tracks(currentuser, playlistId,current_track_list)
        self.spotify.user_playlist_add_tracks(currentuser['id'], playlist_id=playlistId, tracks=tracks)



        #Read the playlist tracks
        playlist = self.spotify.playlist(playlistId)

        for i, playlist in enumerate(playlist['tracks']["items"]):
            print("%s %s" % (playlist['track']["id"],  playlist['track']["name"]))

        return self

