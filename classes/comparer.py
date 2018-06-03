import random
from classes.song import Song
from elo_engine import calculate_gained_points


class Comparer:
    song_list = ()
    sample_list = ()
    song1 = ""
    song2 = ""
    
    
    def __init__(self, song_list):
        self.song_list = song_list
        self.initialize()
    
    
    def initialize(self):
        self.sample_list = random.sample(self.song_list, 2)
        
        self.song1 = self.sample_list[0]
        self.song2 = self.sample_list[1]
    
    
    def getFirstSong(self):
        return self.song1
    
    
    def getSecondSong(self):
        return self.song2
    
    
    def selectWinner(self, number):
        if (self.song1 != "") and (self.song2 != ""):
            if (number == 1):
                scoreGained = calculate_gained_points(self.song1.score, self.song2.score)
                self.song1.addScore(scoreGained)
                self.song2.addScore(-scoreGained)
                self.initialize()
                return 0
            elif (number == 2):
                scoreGained = calculate_gained_points(self.song2.score, self.song1.score)
                self.song2.addScore(scoreGained)
                self.song1.addScore(-scoreGained)
                self.initialize()
                return 0
        return -1