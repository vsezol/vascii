from cx_Freeze import setup, Executable

executables = [Executable('vascii.py', icon='icon.ico')]

setup(name='vascii',
      version='0.0.1',
      description='Realtime video ascii converter!',
      executables=executables)