import abc

class Vehicle(abc.ABC):
  @abc.abstractmethod
  def __init__(self, make: str, model: str, base_price: float):
    self.make = make
    self.model = model
    self.base_price = base_price

  def __repr__(self) -> str:
    return str({
      "make": self.make,
      "model": self.model,
      "base_price": self.base_price
    })

class Ford(Vehicle):
  def __init__(self, model: str, base_price: float):
    super().__init__("Ford", model, base_price)

class BMW(Vehicle):
  def __init__(self, model: str, base_price: float):
    super().__init__("BMW", model, base_price)


if __name__ == "__main__":
  ford = Ford("Edge", "32000.00")
  print(ford)

  bmw = BMW("M850i", "105000.00")
  print(bmw)
