class MyTypeError(TypeError):
  def __init__(self, message: str, code: int):
    super().__init__(message)
    self._code = code

  @property
  def code(self) -> int:
    return self._code


if __name__ == "__main__":
  error = MyTypeError("Waht?", 12345)
  print(error)
  print(error.code)
  
  """
    Raises error because there is no setter.
    https://www.freecodecamp.org/news/python-property-decorator/
  """
  error.code = 234