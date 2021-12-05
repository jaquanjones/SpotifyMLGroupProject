import pandas as pd

df = pd.read_csv('../datasets/merged_2015_2020_top_songs.csv')

artists_lists = df['Artists'].tolist()

formatted_artists_lists = []

for artist in artists_lists:
    formatted_artists_lists.append(artist.split(','))

for artists in formatted_artists_lists:
    new_artist_list = []
    for artist in artists:
        artist.strip('[')
        artist.strip(']')
        artist = artist[2:-2] if artist[0].isalpha() is False else artist
        new_artist_list.append(artist)
    artists = new_artist_list
    print(type(artists))
    print(artists)

# for artist in artists_lists:
#
#     print(artist.split(','))
#     print(type(artist))


# def clean_mixed_formatting(list_string):
#     unformatted_list = list_string.split(',')
#     formatted_list = []
#
#     for item in unformatted_list:
#         item.strip('[')
#         item.strip(']')
#         item.strip('\"')
#         item = item[2:-1] if item[0].isalpha() is False else item
#         if item[0] == '\"':
#             item = item[1:]
#         if item[-1] == '\'':
#             item = item[:-1]
#         formatted_list.append(item)
#
#     return formatted_list
