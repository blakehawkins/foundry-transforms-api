from abc import ABC, abstractmethod
import inspect

def transform_df(output, **kwargs):
  '''Accepts a single Output and a set of Inputs in the form of **kwargs.'''

  def decorate(fn):
    def inner():
      output.write(fn(*[kwargs[arg].val() for arg in inspect.getfullargspec(fn).args]))
    return inner
  return decorate


class Input(ABC):
  @abstractmethod
  def val(self):
    pass


class Output(ABC):
  @abstractmethod
  def write(self, v):
    pass

  @abstractmethod
  def get(self):
    pass
