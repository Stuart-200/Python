class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        print(f"Hello! I am {self.name}. My model is {self.model}.")

    def ask_question(self, other_robot):
        print(f"{self.name}: Hello {other_robot.name}, what is your purpose?")
        print(f"{other_robot.name}: My purpose is to help humans and learn new things.")

robot1 = Robot("Alpha", "X995")
robot2 = Robot("Beta", "Z442")


robot1.introduce()
robot2.introduce()

print("\n")


robot1.ask_question(robot2)
