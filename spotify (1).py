#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[2]:


pip install spotipy


# In[3]:


client_credential_manager= SpotifyClientCredentials(client_id="5e6baf323c064de989d2cd675262b7d2",client_secret="219d76ac5abc4edc8f0b0b5e7a698a51")


# In[4]:


sp = spotipy.Spotify(client_credentials_manager = client_credential_manager)


# In[11]:


playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"


# In[6]:


playlist_URI = playlist_link.split("/")[-1].split("?")[0]


# In[7]:


track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]#value of one playlist


# In[8]:


#top 50 global songs
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Initialize the Spotify client credentials manager
client_credentials_manager = SpotifyClientCredentials(client_id="5e6baf323c064de989d2cd675262b7d2",client_secret="219d76ac5abc4edc8f0b0b5e7a698a51")

# Playlist link
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
tempos = []           # Fixed variable name

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

# Create a DataFrame
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

# Print the DataFrame
df


# In[13]:


#User playlist
# Initialize the Spotify client credentials manager
client_credentials_manager = SpotifyClientCredentials(client_id="5e6baf323c064de989d2cd675262b7d2",client_secret="219d76ac5abc4edc8f0b0b5e7a698a51")

# Playlist link
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
tempos = []           # Fixed variable name

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
    tempos.append(tempo)             # Fixed variable name

# Create a DataFrame
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

# Print the DataFrame
df1


# In[14]:



features=['Artist_Name','Artist_Genres']

def combined_features(row):
  return row['Artist_Name']+" "+ row["Artist_Genres"]#combine the data


# In[15]:


#have selected two features i.e artist name and genre and combining them and forming a new column for both user as well as top 50 global playlist
df['combined_features']=df.apply(combined_features,axis=1)
df1['combined_features']=df1.apply(combined_features,axis=1)


# In[16]:


df1


# In[17]:


df['combined_features'].iloc[1]


# In[18]:


#testing the recomendation system on top 50 global playlist
cv=CountVectorizer()
df['combined_features']


# In[19]:


count_matrix=cv.fit_transform(df['combined_features'])


# In[20]:


count_matrix.toarray


# In[21]:


count_matrix.shape


# In[22]:


#using cosine similarity to find the similar datapoints in the matrix
cosine_sim=cosine_similarity(count_matrix)
cosine_sim


# In[23]:


cosine_sim.shape


# In[24]:


#function for extracting the index number/ID based on the given title of the user track 
# also to combine all the duplicate values
#isnt required here as all the songs are unique in the list
def get_id_from_music(title):
  return df[df.Track_Name==title].index[0]


# In[25]:


music_index=get_id_from_music("Cruel Summer")#user input


# In[26]:


music_index


# In[27]:


#forming a list of the cosine similar data ints based on the index number extracted before 
similar_music=list(enumerate(cosine_sim[music_index]))


# In[28]:


#sorting the aforesaid list
sorted_sim_music=sorted(similar_music,key=lambda x:x[1],reverse=True)


# In[29]:


print(sorted_sim_music)


# In[32]:


#extracting the index number of the track name 
def get_title(index):
  return df[df.index==index]['Track_Name'].values[0]


# In[34]:


# displaying the top 10 cosine similar track to the user inputted track
i=0
for music in sorted_sim_music:
  print(get_title(music[0]))
  i=i+1
  if i>10:
    break


# In[35]:


## if we wanna combine two playlists, 
##here we are now comining wit6h the favourite playlist of the users
combined_df= pd.concat([df,df1],axis=0)
combined_df.reset_index(drop=True, inplace=True)
combined_df['combined_features']
a=len(df)


# In[36]:


#idk why the count vector
cv2=CountVectorizer


# In[37]:


count_matrix2=cv2.fit_transform(combined_df['combined_features'])


# In[38]:


tfidf=TfidfVectorizer()


# In[39]:


Tf_matrix=tfidf.fit_transform(combined_df['combined_features'])


# In[40]:


Tf_matrix.toarray


# In[41]:


Tf_matrix.shape


# In[42]:


cosine_sim1=cosine_similarity(Tf_matrix)
cosine_sim1


# In[43]:


cosine_sim1.shape


# In[44]:


def get_id_from_course1(title):
  return combined_df[combined_df.Track_Name==title].index[0]


# In[45]:


music_index1=get_id_from_course1("Karma Chameleon")


# In[46]:


music_index1


# In[49]:


similar_music1=list(enumerate(cosine_sim1[music_index1]))


# In[50]:


#sorted_sim_music1=sorted(similar_music1,key=lambda x:x[1],reverse=True)


# In[51]:


val1=similar_music1[:a]
sorted_sim_music1=sorted(val1,key=lambda x:x[1],reverse=True)
print(sorted_sim_music1)


# In[52]:


def get_title(index):
  return combined_df[combined_df.index==index]['Track_Name'].values[0]


# In[53]:


i=0
for music in sorted_sim_music1:
  print(get_title(music[0]))
  i=i+1
  if i>10:
    break


# In[ ]:





# In[ ]:





# In[ ]:




