# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:47:09 2019

@author: huyn
"""
"""
Given a map Map<String, List<String>> userSongs with user names as keys and a list of all 
the songs that the user has listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list
of all the songs within that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user 
name and the value is a list of the user's favorite genre(s). Favorite genre is 
the most listened to genre. A user can have more than one favorite genre if he/she 
has listened to the same number of songs per each of the genres.

Input:
userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output: {  
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}

Explanation:
David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
"""

def getFavoriteGeneres(userSongs,songGenres):
    songToGenres = {}
    for genres in songGenres:
        for song in songGenres[genres]:
            if song not in songToGenres:
                songToGenres[song] = set()
            songToGenres[song].add(genres) 
    res = {}
    for user in userSongs:
        genresSet = set()
        for song in userSongs[user]:
            genresSet.update(songToGenres[song])
        res[user] = genresSet
    return res
