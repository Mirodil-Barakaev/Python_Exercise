class Team:
    def __init__(self,players): self.players=players
    def __len__(self): return len(self.players)
print(len(Team(["a","b","c"])))