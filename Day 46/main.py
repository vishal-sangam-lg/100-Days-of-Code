from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Example of a playlist that was created using this project
# https://open.spotify.com/playlist/2lKg9c2TuRcYxjXjP1TZnn?si=UtALQESySM2aVFa3eH8d-Q


# ---------------------------Authenticating spotify account---------------------------#


SPOTIPY_CLIENT_ID = "CLIENT_ID"
SPOTIPY_CLIENT_SECRET = "CLIENT_SECRET"
SPOTIPY_REDIRECT_URI = "REDIRECT_URL"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


# -------------------Getting billboard top100 from a specified year----------------#


# ask the user what year we are going to scrape from
year_requested = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = "https://www.billboard.com/charts/hot-100/" + year_requested

# get the site contents based on input date and store as text
response = requests.get(url=url)
html_content = response.text

# make soup from site contents
soup = BeautifulSoup(html_content, "html.parser")

# extract the top 100 song titles and put them in a list
# check site in Chrome dev tools to see fields
titles = soup.find_all(name="h3", class_="a-no-trucate")
top100 = [title.getText().strip() for title in titles]
# print(top100)


# -----------------------------Creating URIs using spotipy---------------------------#


song_uris = []
year = year_requested.split("-")[0]
for song in top100:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# -------------------------Creating Playlist with uris-------------------------------#


playlist = sp.user_playlist_create(user=user_id, name=f"{year_requested} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
