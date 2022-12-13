import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

from utils import fun


def main(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(1, 1, "e for encrypt / d for decrypt / c for exit")
        key = stdscr.getch()
        if key == ord('e'):
            stdscr.clear()
            stdscr.addstr(2, 0, "Modo encriptar")
            stdscr.addstr(2, 20, "Presiona CTRL+G para guardar")

            # Escritura mensaje
            stdscr.addstr(4, 0, "Mensaje a cifrar:")
            rectangle(stdscr, 5, 0, 10, 40)
            win1 = curses.newwin(4, 39, 6, 1)
            box1 = Textbox(win1)
            stdscr.refresh()
            box1.edit()
            text = box1.gather().replace('\n', '')

            # Escritura contraseña
            stdscr.addstr(4, 41, "Contraseña:")
            rectangle(stdscr, 5, 41, 10, 80)
            win2 = curses.newwin(4, 38, 6, 42)
            box2 = Textbox(win2)
            stdscr.refresh()
            box2.edit()
            pwd = box2.gather().replace('\n', '')

            # Muestra de mensaje cifrado
            stdscr.addstr(11, 0, "Mensaje encriptado:")
            crypted_text = fun.encriptar(text, pwd)
            stdscr.addstr(12, 0, crypted_text)
            stdscr.addstr(18, 0, "Presiona cualquier tecla para volver.")
            stdscr.getch()

        elif key == ord('d'):
            stdscr.clear()
            stdscr.addstr(2, 0, "Modo desencriptar")
            stdscr.addstr(2, 20, "Presiona CTRL+G para guardar")

            # Escritura mensaje cifrado
            stdscr.addstr(4, 0, "Mensaje cifrado:")
            rectangle(stdscr, 5, 0, 10, 40)
            win3 = curses.newwin(4, 39, 6, 1)
            box3 = Textbox(win3)
            stdscr.refresh()
            box3.edit()
            text = box3.gather().replace('\n', '')

            # Escritura contraseña
            stdscr.addstr(4, 41, "Contraseña:")
            rectangle(stdscr, 5, 41, 10, 80)
            win4 = curses.newwin(4, 38, 6, 42)
            box4 = Textbox(win4)
            stdscr.refresh()
            box4.edit()
            pwd = box4.gather().replace('\n', '')

            # Muestra de mensaje cifrado
            stdscr.addstr(11, 0, "Mensaje:")
            crypted_text = fun.desencriptar(text, pwd)
            stdscr.addstr(12, 0, crypted_text)
            stdscr.addstr(18, 0, "Presiona cualquier tecla para volver.")
            stdscr.getch()
        elif key == ord('c'):
            break


wrapper(main)
