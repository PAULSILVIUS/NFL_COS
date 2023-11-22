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
    
    def compare(self, other):
        for team in self.defeated_teams:
            if team == other.name:
                print('True')
                return True
        self.swap(other)
       # print('False')
        return False

    def swap(self, other):
        self.name, other.name = other.name, self.name
        self.defeated_teams, other.defeated_teams = other.defeated_teams, self.defeated_teams


    
        
    

