from pymaker import command, r

@command
def start():
    r('echo "Hello!"')

@command('end', deps=['start'])
def end():
    r(['echo', 'Goodbye!'])
