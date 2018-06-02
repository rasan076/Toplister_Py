def calculate_gained_points(ratingOfWinner, ratingOfLoser):


    def calculate_elo_prediction(player1rating, player2rating):
        exponent = (player2rating - player1rating) / 400.0
        denominator = 1 + 10**exponent
        prediction = 1 / denominator
        return prediction
    
    
    def calculate_gained_points_from_prediction(expectedScoreOfWinner):
        K = 32
        delta = K * (1 - expectedScoreOfWinner)
        return delta
    
    
    expectedScore = calculate_elo_prediction(ratingOfWinner, ratingOfLoser)
    delta = calculate_gained_points_from_prediction(expectedScore)
    return delta
