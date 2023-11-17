class Team:
    def __init__(self, name, defeated_teams):
        self.name = name
        self.defeated_teams = defeated_teams
    
    # Setters
    def setName (self, name): self.name = name
    def setDefeatedTeams(self, defeated_teams): self.defeated_teams = defeated_teams
    
    # Getters
    def getName (self): return self.name
    def getDefeatedTeams (self): return self.defeated_teams

        
    def add_defeated_team(self,name,defeated_teams):
        self.name = name
        self.defeated_teams.append(defeated_teams)
        
    def print_data(name, defeated_teams):
        print("Team Name:", name)
        print("Defeated Teams:", defeated_teams)
    
    def compare(team1, team2):
        for defeated_team in team1.defeated_teams:
            if defeated_team == team2.name:
                return True
        return False
            

        
    

