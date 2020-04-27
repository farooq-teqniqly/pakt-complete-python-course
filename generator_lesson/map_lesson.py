class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"{self.make}, {self.model}"

    @classmethod
    def create(cls, **properties):
        return cls(**properties)


if __name__ == "__main__":
    makes = ["BMW", "Ford", "Dodge", "Mercedes-Benz", "Mercury"]

    starts_with_mer = (make for make in makes if make.startswith("Mer"))
    upper_case = (make.upper() for make in starts_with_mer)

    print(list(upper_case))

    vehicle = Vehicle.create(model="Mustang", make="Ford")
    print(vehicle)
