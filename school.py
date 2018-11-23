class School:
    def __init__(self, name = None, roster = {}):
        self.name = name
        self.roster = roster
    
    def add_student(self, name, grade):
        if grade in self.roster:
            self.roster[grade].append(name)
        else:
            self.roster[grade] = []
            self.roster[grade].append(name)
            
    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
        return {x:sorted(self.roster[x]) for x in self.roster}