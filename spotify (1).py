import spotipy
from spotipy.oauth2 import SpotifyClientCredentials  #With Spotipy you get full access to all of the music data provided by the Spotify platform.
from sklearn.feature_extraction.text import CountVectorizer   #to convert text to vectors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  #comparing different vectors


pip install spotipy


client_credential_manager= SpotifyClientCredentials(client_id="5e6baf323c064de989d2cd675262b7d2",client_secret="219d76ac5abc4edc8f0b0b5e7a698a51")

sp = spotipy.Spotify(client_credentials_manager = client_credential_manager)


playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"


playlist_URI = playlist_link.split("/")[-1].split("?")[0]


track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]#value of one playlist


#top 50 global songs
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy


client_credentials_manager = SpotifyClientCredentials(client_id="5e6baf323c064de989d2cd675262b7d2",client_secret="219d76ac5abc4edc8f0b0b5e7a698a51")

playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]

# Create empty lists to store the extracted information
track_uris = []
track_names = []
artist_names = []
artist_popularities = []
artist_genres = []
albums = []
track_popularities = []
danceabilities = []  # Fixed variable name
tempos = []    

# Fetch and process information about each track in the playlist
for track in sp.playlist_tracks(playlist_URI)["items"]:
    # URI
    track_uri = track["track"]["uri"]
    track_uris.append(track_uri)
    
    # Track name
    track_name = track["track"]["name"]
    track_names.append(track_name)
    
    # Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    
    # Name, Popularity, and Genres of the main artist
    artist_name = track["track"]["artists"][0]["name"]
    artist_names.append(artist_name)
    artist_popularity = artist_info["popularity"]
    artist_popularities.append(artist_popularity)
    artist_genre = ", ".join(artist_info["genres"])
    artist_genres.append(artist_genre)
    
    # Album
    album = track["track"]["album"]["name"]
    albums.append(album)
    
    # Popularity of the track
    track_popularity = track["track"]["popularity"]
    track_popularities.append(track_popularity)
    
    # Fetch audio features for the track
    audio_features = sp.audio_features(track_uri)[0]
    
    # Audio features
    danceability = audio_features["danceability"]
    tempo = audio_features["tempo"]  # Fixed variable name
    danceabilities.append(danceability)
    tempos.append(tempo)             # Fixed variable name


data = {
    "Track_URI": track_uris,
    "Track_Name": track_names,
    "Artist_Name": artist_names,
    "Artist_Popularity": artist_popularities,
    "Artist_Genres": artist_genres,
    "Album": albums,
    "Track_Popularity": track_popularities,
    "Danceability": danceabilities,
    "Tempo": tempos
}

df = pd.DataFrame(data)


df

#User playlist
# Initialize the Spotify client credentials manager
client_credentials_manager = SpotifyClientCredentials(client_id="5e6baf323c064de989d2cd675262b7d2",client_secret="219d76ac5abc4edc8f0b0b5e7a698a51")


playlist_link1 = "https://open.spotify.com/playlist/72lj6JXZE72TfECeRQbNri?si=mbdsIT6YTbay8XvGjjABJQ"
playlist_URI1 = playlist_link1.split("/")[-1].split("?")[0]

# Create empty lists to store the extracted information
track_uris = []
track_names = []
artist_names = []
artist_popularities = []
artist_genres = []
albums = []
track_popularities = []
danceabilities = []  # Fixed variable name
tempos = []   

import requests

connect_timeout = 6
read_timeout = 10
response = requests.get("https://scrapingbee.com/", timeout=(connect_timeout, read_timeout))

# Fetch and process information about each track in the playlist
for track in sp.playlist_tracks(playlist_URI1)["items"]:
    # URI
    track_uri = track["track"]["uri"]
    track_uris.append(track_uri)
    
    # Track name
    track_name = track["track"]["name"]
    track_names.append(track_name)
    
    # Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    
    # Name, Popularity, and Genres of the main artist
    artist_name = track["track"]["artists"][0]["name"]
    artist_names.append(artist_name)
    artist_popularity = artist_info["popularity"]
    artist_popularities.append(artist_popularity)
    artist_genre = ", ".join(artist_info["genres"])
    artist_genres.append(artist_genre)
    
    # Album
    album = track["track"]["album"]["name"]
    albums.append(album)
    
    # Popularity of the track
    track_popularity = track["track"]["popularity"]
    track_popularities.append(track_popularity)
    
    # Fetch audio features for the track
    audio_features = sp.audio_features(track_uri)[0]
    
    # Audio features
    danceability = audio_features["danceability"]
    tempo = audio_features["tempo"]  # Fixed variable name
    danceabilities.append(danceability)
    tempos.append(tempo)     

data = {
    "Track_URI": track_uris,
    "Track_Name": track_names,
    "Artist_Name": artist_names,
    "Artist_Popularity": artist_popularities,
    "Artist_Genres": artist_genres,
    "Album": albums,
    "Track_Popularity": track_popularities,
    "Danceability": danceabilities,
    "Tempo": tempos
}

df1 = pd.DataFrame(data)


df1

features=['Artist_Name','Artist_Genres']


def combined_features(row):
  return row['Artist_Name']+" "+ row["Artist_Genres"]#combine the data


#have selected two features i.e artist name and genre and combining them and forming a new column for both user as well as top 50 global playlist
df['combined_features']=df.apply(combined_features,axis=1)
df1['combined_features']=df1.apply(combined_features,axis=1)

df1

df['combined_features'].iloc[1]


#testing the recomendation system on top 50 global playlist
cv=CountVectorizer()
df['combined_features']

count_matrix=cv.fit_transform(df['combined_features'])


count_matrix.toarray


count_matrix.shape


cosine_sim=cosine_similarity(count_matrix)
cosine_sim

cosine_sim.shape


#function for extracting the index number/ID based on the given title of the user track 
# also to combine all the duplicate values
#isnt required here as all the songs are unique in the list
def get_id_from_music(title):
  return df[df.Track_Name==title].index[0]


music_index=get_id_from_music("Cruel Summer")#user input


music_index


#forming a list of the cosine similar data ints based on the index number extracted before 

similar_music=list(enumerate(cosine_sim[music_index]))


#sorting the aforesaid list

sorted_sim_music=sorted(similar_music,key=lambda x:x[1],reverse=True)



print(sorted_sim_music)


#extracting the index number of the track name 
def get_title(index):
  return df[df.index==index]['Track_Name'].values[0]


# displaying the top 10 cosine similar track to the user inputted track
i=0  #This line initializes a variable i with a value of 0. i will be used to keep track of the number of music tracks printed.
for music in sorted_sim_music:
  print(get_title(music[0]))
  i=i+1
  if i>10:
    break


## if we wanna combine two playlists, 
##here we are now comining wit6h the favourite playlist of the users
combined_df= pd.concat([df,df1],axis=0)
combined_df.reset_index(drop=True, inplace=True)
combined_df['combined_features']
a=len(df)

cv2=CountVectorizer()


count_matrix2=cv2.fit_transform(combined_df['combined_features'])


count_matrix2.toarray


count_matrix2.shape


cosine_sim2=cosine_similarity(count_matrix2)
cosine_sim2

cosine_sim2.shape


def get_id_from_music2(title):
  return combined_df[combined_df.Track_Name==title].index[0]

music_index2=get_id_from_music2("Karma Chameleon")#user input


music_index2

similar_music2=list(enumerate(cosine_sim2[music_index2]))


val1=similar_music2[:a]
sorted_sim_music2=sorted(val1,key=lambda x:x[1],reverse=True)
print(sorted_sim_music2)

def get_title(index):
  return combined_df[combined_df.index==index]['Track_Name'].values[0]


i=0
for music in sorted_sim_music2:
  print(get_title(music[0]))
  i=i+1
  if i>10:
    break

