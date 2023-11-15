class Team:
    defeated_teams = []
    def __init__(self, name, defeated_teams):
        self.name = name
        self.defeated_teams = defeated_teams
        
    def add_defeated_team(self, defeated_teams):
        self.defeated_teams.append(defeated_teams)
        
    def print_data(name,defeated_teams):
        print("Team Name:", name)
        print("Defeated Teams:", defeated_teams)