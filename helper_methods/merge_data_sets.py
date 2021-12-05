import numpy as np
import pandas as pd

# initialize each existing song list as df
all_spotify_songs_df = pd.read_csv('../datasets/tracks.csv')

top_songs_2010_2020_df = pd.read_csv('../datasets/top_100_2011-2020_with_genres.csv')

# reduce range of 2010-2020 data set to 2016-2020 (5 years)
top_songs_2010_2020_df = top_songs_2010_2020_df[499:]
print(top_songs_2010_2020_df.head())
# top_songs_2015_2020_df = top_songs_2010_2020_df[499:]

# store list of billboard top 100 spotify ids as list to iterate
top_song_ids = top_songs_2010_2020_df['Spotify Song ID'].tolist()

# store Spotify Song ID's from top 100 list if not found in dataset including all songs
missing_song_ids = []

# Gather relevant column names from each data_set for new df (see commented code to at bottom to print list of names)
merged_song_info_feature_list = ['Spotify ID', 'Title', 'Artists', 'Year',
                                 # 'Rank', 'Genres',
                                 'Acousticness', 'Energy', 'Instrumentalness', 'Key',
                                 'Liveness', 'Loudness', 'Mode', 'Speechiness',
                                 'Tempo', 'Time Signature', 'Valence', 'Top 100']
merged_song_info_list = []

# iterate through song ids to find if each id is in all_spotify_songs_df
for top_id in top_song_ids:
    matching_song_id_index = all_spotify_songs_df.index[
        all_spotify_songs_df['id'] == top_id].tolist()[0] if any(all_spotify_songs_df.index[
                                                                     all_spotify_songs_df[
                                                                         'id'] == top_id].tolist()) else None
    if matching_song_id_index is not None:
        top_song_id_index = top_songs_2010_2020_df.index[
            top_songs_2010_2020_df['Spotify Song ID'] == top_id].tolist()[0]

        feature_list_1 = all_spotify_songs_df.iloc[matching_song_id_index].tolist()
        feature_list_2 = top_songs_2010_2020_df.loc[top_song_id_index]

        formatted_song_info = [
            feature_list_1[0],
            feature_list_1[1],
            feature_list_2[2],  # feature list 2 version of 'artists' since feature list 1 has list as a string
            feature_list_2[3],
            # will use rank to decide label rather than feature
            # feature_list_2[4],
            # will disregard genre to experiment what type of findings made without it
            # feature_list_2[5].split(","),
            feature_list_1[14],
            feature_list_1[9],
            feature_list_1[15],
            feature_list_1[10],
            feature_list_1[16],
            feature_list_1[11],
            feature_list_1[12],
            feature_list_1[13],
            feature_list_1[18],
            feature_list_1[19],
            feature_list_1[17],
            1 if feature_list_2[4] >= 50 else 0
        ]
        merged_song_info_list.append(formatted_song_info)
        print(formatted_song_info)
    else:
        missing_song_ids.append(top_id)
        print(top_id)

song_info_matrix = np.array(merged_song_info_list, dtype=object)

# transposed_song_info_list = song_info_matrix.transpose().tolist()

merged_song_info_df = pd.DataFrame(song_info_matrix, columns=merged_song_info_feature_list)

# merged_song_info_df.to_csv('../datasets/alternate_top_50_songs_from_2016_2020.csv', index=False)

# merged_song_info_dictionary['Spotify ID'] = {
#     'Spotify ID': match_value_list[0],
#     'Title': match_value_list[1],
#     'Artists': match_value_list[5],
#     # 'Year': match_value_list2[],
#     # 'Rank': match_value_list2[],
#     # 'Genres': match_value_list2[],
#     'Acousticness': match_value_list[14],
#     'Energy': match_value_list[9],
#     'Instrumentalness': match_value_list[15],
#     'Key': match_value_list[10],
#     'Liveness': match_value_list[16],
#     'Loudness': match_value_list[11],
#     'Mode': match_value_list[12],
#     'Speechiness': match_value_list[13],
#     'Tempo': match_value_list[18],
#     'Time Signature': match_value_list[19],
#     'Valence': match_value_list[17]
# }


# index:
# id=0,
# name=1,
# popularity=2,
# duration_ms=3 ~
# explicit=4   ~
# artists=5
# id_artists=6  ~
# release_date=7  ~
# danceability=8
# energy=9
# key=10
# loudness=11
# mode=12
# speechiness=13
# acousticness=14
# instrumentalness=15
# liveness=16
# valence=17
# tempo=18
# time_signature=19


'''relevant column names from all songs data set'''
# ['id', 'name', 'popularity', 'artists', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
#  'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']
