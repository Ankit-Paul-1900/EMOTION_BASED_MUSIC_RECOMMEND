import pandas as pd
import numpy as np
data=pd.read_csv("songs_mood.csv")
data.shape
data.head()
def song_id(song_name):
    p=np.array(data[data['track_name'] == song_name]["id"])
    #c=p[0]
    return p
def song_name(song_id):
    p=np.array(data[data['id'] == song_id]["track_name"])
    c=p[0]
    return c
def song_features(song_id):
    p=np.array(data[data['id'] == song_id][['length','danceability','acousticness','energy','instrumentalness','liveness','valence',
                                'loudness','speechiness','tempo']])
    return p
def artist_name(song_id):
    a=np.array(data[data['id']==song_id]['artist_name'])
    return a

