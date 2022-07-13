from gpt import gpt_prompt
import os
from flask import Flask, session, request, redirect
from flask_session import Session
from dotenv import load_dotenv
from musixmatch import Musixmatch

# # load environment variables 
load_dotenv()

# musixmatch API key
KEY = os.get_env('KEY')

def get_lyrics(artist, song):
    """
    Get lyrics from musixmatch API
    """
    musixmatch = Musixmatch(KEY)
    result = musixmatch.track_search(q_track=song, q_artist=artist, s_track_rating='desc', page_size=10, page=1)
    song_id = result['message']['body']['track_list'][0]['track']['track_id']
    lyrics = musixmatch.track_lyrics_get(song_id)['message']['body']['lyrics']['lyrics_body']
    return lyrics

app = Flask(__name__)

app.route('/')
def index():
    get_lyrics('The Beatles', 'Sgt. Pepper\'s Lonely Hearts Club Band')




