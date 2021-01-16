class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.score = goals+assists

    def __str__(self):
        return f"{self.name:25} {self.team:3} {self.goals:2} + {self.assists:2} = {self.score}"
