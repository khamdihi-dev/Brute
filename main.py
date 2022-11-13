from os import system
from run import folder

system('git pull') ; system('clear')
if __name__ == '__main__':
        try:
                folder()
        except Exception as e:exit(str(e))
