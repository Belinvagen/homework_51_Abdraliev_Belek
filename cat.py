import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.hunger = 40
        self.happiness = 40
        self.is_sleeping = False
        self.image = self.get_image()

    def get_image(self):
        if self.happiness < 30:
            return 'sad_cat.png'
        elif self.happiness < 70:
            return 'neutral_cat.png'
        else:
            return 'happy_cat.png'

    def feed(self):
        if not self.is_sleeping:
            self.hunger = min(100, self.hunger + 15)
            self.happiness = min(100, self.happiness + 5)
            if self.hunger > 100:
                self.happiness = max(0, self.happiness - 30)
        self.image = self.get_image()

    def play(self):
        if self.is_sleeping:
            self.is_sleeping = False
            self.happiness = max(0, self.happiness - 5)
        else:
            if random.randint(1, 3) == 1:
                self.happiness = 0  # Cat goes into a rage
            else:
                self.happiness = min(100, self.happiness + 15)
            self.hunger = max(0, self.hunger - 10)
        self.image = self.get_image()

    def sleep(self):
        self.is_sleeping = True

    def perform_action(self, action):
        if action == 'feed':
            self.feed()
        elif action == 'play':
            self.play()
        elif action == 'sleep':
            self.sleep()
