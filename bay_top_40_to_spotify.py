from classes.bay_radio import BayRadio
from classes.spotify_builder import SpotifyBuilder
import sys
    
SpotifyBuilder().authenticate(sys.argv[0], sys.argv[1],'http://localhost:8080').import_tracks_to_playlist('Top 40', BayRadio().extract_bay_top_40_tracks('https://bay.com.mt/top40/'))




