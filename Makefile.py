from pymaker import command, r, declare_argument

declare_argument('-f', '--file', default='Nothing')

@command
def start():
    "This is a help message! "
    r('echo "Hello!"')

@command(deps=['start'])
def end():
    r(['echo', 'Goodbye!'])

@command
def testcli(ns):
    print(ns)
    r(f'echo {ns.file}')

@command
def build():
    r("flit install")
