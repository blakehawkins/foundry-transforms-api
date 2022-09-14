from setuptools import setup

setup(
  name="transforms",
  version="0.3.0",
  packages=['transforms', 'transforms.api'],
  package_dir={'transforms': 'src/transforms', 'transforms.api': 'src/transforms/api'}
)
