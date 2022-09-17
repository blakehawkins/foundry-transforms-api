# install

```
pipenv install git+ssh://github.com/blakehawkins/foundry-transforms-api#egg=transformsbase
```

# Usage

```
from transformsbase.api import Input, Output, transform_df

class MyOutput(Output):
  def __init__(self):
    self.val = None

  def write(self, v):
    self.val = v

  def get(self):
    return self.val

class MyInput(Input):
  def __init__(self, val):
    self._val = val

  def val(self):
    return {"a": 2, "b": 3}[self._val]

if __name__ == '__main__':
  output = MyOutput()

  @transform_df(output, a=MyInput("a"), b=MyInput("b"))
  def transform(a, b):
    return a + b

  print(output.get())
```
