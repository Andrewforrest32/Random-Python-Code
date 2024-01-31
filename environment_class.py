class Environment:
    def __init__(self,terrain,weather):
        self.terrain = terrain
        self.weather = weather
    
    def weather_effect(self):
        if self.weather == "Hail" or self.weather == "Sandstorm":
            return True
    def weather_damage(self):
            return 0.0625