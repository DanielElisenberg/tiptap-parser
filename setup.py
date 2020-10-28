import re
from distutils.core import setup


with open("version.yml", encoding="utf-8") as f:
    version = re.search(r'(?<=version: ).*', f.read()).group(0)

setup(
  name='tiptap-parser',
  packages=['tiptapparser'],
  version=version,
  license='MIT',
  author='Daniel Elisenberg',
  url='https://github.com/DanielElisenberg/tiptap-parser',
  download_url='https://github.com/DanielElisenberg/tiptap-parser/archive/1.0.9.tar.gz',
  keywords=['TIPTAP', 'PARSE', 'JSON', 'HTML'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3.8',
  ],
)
