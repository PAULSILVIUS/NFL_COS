from Team import Team

class CircleOfParity:
    def __init__(self):
        self.circle = []

    def add_object(self, Team):
        self.circle.append(Team)

    def print_objects(self):
        for obj in self.circle:
            print(obj)