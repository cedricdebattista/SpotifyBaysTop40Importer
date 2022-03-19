import bs4
from bs4 import BeautifulSoup

import requests

class BayRadio:
    def extract_bay_top_40_tracks(self, bay_top_40_url):
        # Get the hrml contents of the bay top 40 page
        response = requests.get(bay_top_40_url)
        
        if(response.status_code != 200):
            print("Failed accessing page %s with status_code %s" % (bay_top_40_url, response.status_code))

        html = response.content

        # Beutify the contents and generate an object for parsing 
        soup_html_parser = BeautifulSoup(html, features="html.parser")

        # List all the frames
        iframe_element_list  = soup_html_parser.find_all('iframe')

        trackList = []

        for iframe_element in iframe_element_list:
            iframe_src = iframe_element.get('src')

            if(iframe_src != 'about:blank'):
                clean_track_id = iframe_src.replace("https://open.spotify.com/embed/track/", "").replace("?utm_source=generator", "") 
                print("adding track: %s" % (clean_track_id))             
                trackList.append(clean_track_id)

        return trackList
