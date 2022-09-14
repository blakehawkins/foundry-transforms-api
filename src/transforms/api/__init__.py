from abc import ABC, abstractmethod
import inspect

def transform_df(output, **kwargs):
  '''Accepts a single Output and a set of Inputs in the form of **kwargs.'''

  def decorate(fn):
    output.write(fn(*[kwargs[arg] for arg in inspect.getfullargspec(fn).args]))
    return fn
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
