import datetime
from bs4 import BeautifulSoup
import lxml  # provides a parser that may be necessary for some websites
import requests
import datetime as dt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

SPOTIPY_CLIENT_ID = ""
CLIENT_SECRET = "a"
SPOTIPY_REDIRECT_URI = "http://example.com"


def prompt_user():
    prompt = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ").strip()

    analysis = prompt.split("-")

    if not (analysis[0].isnumeric() and analysis[1].isnumeric() and analysis[2].isnumeric()): # checks to ensure each
        # character is numeric
        print("NON-NUMERICAL CHARACTER ENTERED; TRY AGAIN.")
        prompt = prompt_user()
    elif not (len(analysis[0]) == 4 and len(analysis[1]) == 2 and len(analysis[2]) == 2): # checks that the format of
        # each character is correct
        print("INCORRECT FORMAT ENTERED; ENTER IN THE FOLLOWING FORMAT: YYYY-MM-DD; TRY AGAIN.")
        prompt = prompt_user()
    elif not (int(analysis[0]) <= int(dt.datetime.now().year)) or not (12 >= int(analysis[1]) >= 1) or not (
            31 >= int(analysis[2]) >= 1): # checks that the date is a real date
        print("DATE DOES NOT EXIST; TRY AGAIN.")
        prompt = prompt_user()
    return prompt


# prompts the user for time travel date
time_travel_date = prompt_user()

# sets a custom time travel date for testing purposes
# time_travel_date = "2012-05-25"

time_travel_year = time_travel_date[0:4:]

# procures billboard.com hot 100 from time travel date
response = requests.get(f"https://www.billboard.com/charts/hot-100/{time_travel_date}/")
billboard_webpage = response.text

# created beautiful soup object
soup = BeautifulSoup(billboard_webpage, "html.parser")

# creates list of 100 songs from time travel date
songs = soup.find_all(name="h3",
                      class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                             "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                             "u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 "
                             "u-max-width-230@tablet-only")
songs = [song.get_text().strip() for song in
         songs]  # creates a list of songs after stripping '/n' and '/t' characters from the text

# creates spotipy object for Authorization Code Flow
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=CLIENT_SECRET))

# queries results from spotipy

spotify_song_uris = []

for song in songs:
    result = sp.search(q=f"track: {song} year: {time_travel_year}", type="track")
    if len(result["tracks"]["items"]) == 0:  # if the song doesn't exist in spotify, the request will return an empty
        # list of items
        spotify_song_uris.append("NO URI FOUND")
    else:
        spotify_song_uris.append(result["tracks"]['items'][2]['id'])

# creates playlist
scope = "playlist-modify-private"  # see https://developer.spotify.com/documentation/general/guides/authorization/scopes/

sp1 = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=CLIENT_SECRET,
                                                redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope))
new_playlist = sp1.user_playlist_create(user="1222352633", name=f"{time_travel_date} Billboard 100",
                                        public=False,
                                        description=f"A playlist containing the hot "
                                                    f"100 songs in the week of {time_travel_date}")  # the username is NOT the same as the client ID; it can be found in the desktop app under "Account"
# obtains the ID of the new playlist
new_playlist_id = new_playlist["id"]

# adds items to the playlist
sp1.playlist_add_items(playlist_id=new_playlist_id, items=spotify_song_uris,
                       position=None)  # adds the spotify URIS of the songs obtained from Billboard.com to the playlist
