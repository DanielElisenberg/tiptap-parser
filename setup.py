import yaml

from distutils.core import setup
from setuptools.command.build import build as _build

class build(_build):
    def run(self):
        subprocess.call(["pip", "install", "pyyaml"])
        _build.run(self)

with open("version.yml") as version_yml:
    version = yaml.load(version_yml, Loader=yaml.FullLoader)['version']

setup(
  name='tiptap-parser',
  packages=['tiptapparser'],
  version=version,
  license='MIT',
  author='Daniel Elisenberg',
  url='https://github.com/DanielElisenberg/tiptap-parser',
  download_url='https://github.com/DanielElisenberg/tiptap-parser/archive/1.0.2.tar.gz',
  keywords=['TIPTAP', 'PARSE', 'JSON', 'HTML'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3.8',
  ],
)
