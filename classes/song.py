class Song:
    
    title = ""
    main_artists = []
    main_artists_countries = []
    featuring_artists = []
    featuring_artists_countries = []
    year = 0
    genre = ""
    score = 1600
    comparisons = 0
    
    
    def __init__(self, *id):
        if id:
            self.id = id[0]
        else:
            self.id = 99999999999
    
    
    def addScore(self, diff):
        self.score += diff
        self.comparisons += 1
