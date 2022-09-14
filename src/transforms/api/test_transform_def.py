from . import transform_df, Input as IInput, Output as IOutput


class Input(IInput):
  def __init__(self, val):
    self._val = val

  def val(self):
    return {"a": 2, "b": 3}[self._val]


class Output(IOutput):
  def __init__(self):
    self.val = None

  def write(self, v):
    self.val = v

  def get(self):
    return self.val


def test_transform_df():
  output = Output()

  @transform_df(output, a=Input("a"), b=Input("b"))
  def transform(a, b):
    return a.val() + b.val()

  assert(output.get() == 5)
