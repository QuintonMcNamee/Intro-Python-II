class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        display_string = f"{self.name}, "
        display_string += f"{self.description}"
        return display_string