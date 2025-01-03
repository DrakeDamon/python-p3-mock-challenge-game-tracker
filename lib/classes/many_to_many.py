class Game:
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not len(title) > 0:
            raise ValueError("Title must be at least 1 character long")
        self._title = title


    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        raise TypeError("Title must be a string")



    def results(self):
        all_results = Result.all
        return[result for result  in all_results if result.game == self]

    def players(self):
        all_results = Result.all
        return list(set([result.player for result in all_results if result.game == self]))

    def average_score(self, player):
        player_results = [result for result in Result.all if result.game == self and result.player == player]
        player_score = [result.score for result in player_results]
        return sum(player_score) / len(player_score) if player_score else 0

class Player:
    def __init__(self, username):
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
        if len(username) < 2 or len(username) > 16:
            raise ValueError("Username must be between 2 and 16 characters long")
        self._username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError("Username must be a string")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Username must be between 2 and 16 characters long")
        self._username = value

    def results(self):
        all_results = Result.all
        return list(set([result for result in all_results if result.player == self]))

    def games_played(self):
        player_results = [result for result in Result.all if result.player == self]
        return list(set([result.game for result in player_results]))
    def played_game(self, game):
        return any(result for result in Result.all
                   if result.player == self and result.game == game)

    def num_times_played(self, game):
        return len([result for result in Result.all
                    if result.player == self and result.game == game])

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game

        if not isinstance(score, int):
            raise TypeError("Score must be an integer")
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
            raise TypeError("Score must be an integer")

    