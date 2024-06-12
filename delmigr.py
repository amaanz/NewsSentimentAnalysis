import os
import glob

for filename in glob.glob('**/migrations/*.py', recursive=True):
    if not filename.endswith('__init__.py'):
        os.remove(filename)

for filename in glob.glob('**/migrations/*.pyc', recursive=True):
    os.remove(filename)
