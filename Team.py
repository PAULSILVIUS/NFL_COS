class Team:
    def __init__(self, name, defeated_teams):
        self.name = name
        self.defeated_teams = defeated_teams
        self.circle_list = [name, defeated_teams]
        
    def add_defeated_team(self,name,defeated_teams):
        self.name = name
        self.defeated_teams.append(defeated_teams)
        
    def print_data(name, defeated_teams):
        print("Team Name:", name)
        print("Defeated Teams:", defeated_teams)
    
    def circle(self, circle_list):
        circle_list.append(self.name, self.defeated_teams)
        print("Team Name:", self.name)
        print("Defeated Teams:", self.defeated_teams)
    

