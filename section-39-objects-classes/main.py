class Car:
    notes = []  # it's like static property

    def __init__(self, model: str) -> None:
        self.model = model
        self.how_many_times_move = 0
        self.notes = []

    def __str__(self) -> str:
        return self.model

    def move(self) -> None:
        self.how_many_times_move += 1
        print(f"Car {self.model} moving")

    def stop(self) -> None:
        print(f"Car {self.model} stopped")

    @staticmethod
    def merge_notes(*args):
        Car.notes.extend(args)

    @staticmethod
    def get_notes():
        return Car.notes


bmw = Car("BMW")
print(bmw)
print(dir(bmw))
print(bmw.__dict__)  # {'model': 'BMW'}
print(type(bmw))  # <class '__main__.Car'>
print(isinstance(bmw, object))  # True
print(isinstance(bmw, Car))  # True

bmw.move()  # Car BMW moving
bmw.stop()  # Car BMW stopped

Car.move(bmw)  # Car BMW moving
Car.stop(bmw)  # Car BMW stopped

print(bmw.how_many_times_move)

Car.merge_notes("a", "b", "c")
bmw.merge_notes("za", "xb", "dc")

print(Car.get_notes())
