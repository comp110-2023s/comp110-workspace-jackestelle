

class River:
    day: int
    bears: int
    fish: int

    def __init__(self, num_fish: int, num_bears: int):
        self.fish = num_fish
        self.bears = num_bears
        self.day = 0

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {self.fish}")
        print(f"Bear population: {self.bears}")

   
