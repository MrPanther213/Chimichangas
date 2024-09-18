class jedi:
    def __init__(self,name,lightsaber_color,rank):
        self.name=name
        self.lightsaber_color=lightsaber_color
        self.rank=rank

    def introduce(self):
        print(f"I am {self.name}, a {self.rank} Jedi. My lightsaber color is {self.lightsaber_color}.")

    def force_push(self):
        print(f"{self.name} uses force Push!")

        obiwan = jedi("Obi-wan Kenobi", "Blue", "Master")
        obiwan.introduce()
        obiwan.force_push()

        Zach = jedi("zach-obi", "green", "master")
