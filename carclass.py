class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0.0
        self.is_engine_on = False

    def start_engine(self):
        self.is_engine_on = True
        print("engine has started")

    def stop_engine(self):
        self.is_engine_on = False
        print("engine has stopped")

    def accelerate_engine(self, faster):
        if self.is_engine_on:
            self.speed += faster
            print(f"speed is now{self.speed}km/h")
        else:
            print("engine isn't on")


car = Car("ford", "jeep", "2024")
