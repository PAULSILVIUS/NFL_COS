class Data:
    def __init__(self, array):
        self.array = array
        
    def get_all_teams(self):
        result = []
        for item in self.array:
            result.append(item[0])
        result = list(set(result))    
        return result
    
    # returns a list of teams that the specified team defeated
    def get_team_wins(self, team):
        result = []
        for item in self.array:
            if item[0] == team:
                result.append(item[1])
        return result