import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from cryptography.fernet import Fernet

global key
with open('key.key', 'rb') as filein:
    key = filein.read()


def main(stdscr):
    global key
    f = Fernet(key)

    win = curses.newwin(3, 18, 2, 2)
    box = Textbox(win)

    rectangle(stdscr, 2, 2, 10, 20)
    stdscr.refresh()

    box.edit()
    text = box.gather().replace('\n', '')
    text = bytes(text, 'utf-8')
    crypted = f.encrypt(text)
    stdscr.addstr(10, 40, crypted)
    stdscr.getch()


wrapper(main)
