import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

from utils import fun, draws

stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
COLOR_1 = curses.color_pair(1)
COLOR_2 = curses.color_pair(2)
COLOR_3 = curses.color_pair(3)
COLOR_4 = curses.color_pair(4)


def main(stdscr):
    stdscr.bkgd(' ', COLOR_1)
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, draws.logo, COLOR_1)
        stdscr.addstr(12, 1, "Encriptar -> E", COLOR_4)
        stdscr.addstr(13, 1, "Desencriptar -> D", COLOR_4)
        stdscr.addstr(14, 1, "Salir -> C", COLOR_4)
        curses.curs_set(0)
        key = stdscr.getch()
        if key == ord('e'):
            stdscr.clear()
            stdscr.addstr(2, 0, "Modo encriptar", COLOR_2)
            stdscr.addstr(2, 20, "Continuar -> CTRL+G", COLOR_4)
            curses.curs_set(1)

            # Escritura mensaje
            stdscr.addstr(4, 0, "Mensaje a cifrar:")
            rectangle(stdscr, 5, 0, 10, 40)
            win1 = curses.newwin(4, 39, 6, 1)
            win1.bkgd(' ', COLOR_1)
            box1 = Textbox(win1, COLOR_1)
            stdscr.refresh()
            box1.edit()
            text = box1.gather().replace('\n', '')

            # Escritura contraseña
            stdscr.addstr(4, 41, "Contraseña:")
            rectangle(stdscr, 5, 41, 10, 80)
            win2 = curses.newwin(4, 38, 6, 42)
            win2.bkgd(' ', COLOR_1)
            box2 = Textbox(win2)
            stdscr.refresh()
            box2.edit()
            pwd = box2.gather().replace('\n', '')

            # Muestra de mensaje cifrado
            stdscr.addstr(11, 0, "Mensaje encriptado:")
            crypted_text = fun.encriptar(text, pwd)
            stdscr.addstr(12, 0, crypted_text, COLOR_3)
            stdscr.addstr(18, 0, "Presiona cualquier tecla para volver.", COLOR_4)
            stdscr.getch()

        elif key == ord('d'):
            stdscr.clear()
            stdscr.addstr(2, 0, "Modo desencriptar", COLOR_2)
            stdscr.addstr(2, 20, "Continuar -> CTRL+G", COLOR_4)
            curses.curs_set(1)

            # Escritura mensaje cifrado
            stdscr.addstr(4, 0, "Mensaje cifrado")
            rectangle(stdscr, 5, 0, 10, 40)
            win3 = curses.newwin(4, 39, 6, 1)
            win3.bkgd(' ', COLOR_1)
            box3 = Textbox(win3)
            stdscr.refresh()
            box3.edit()
            text = box3.gather().replace('\n', '')

            # Escritura contraseña
            stdscr.addstr(4, 41, "Contraseña:")
            rectangle(stdscr, 5, 41, 10, 80)
            win4 = curses.newwin(4, 38, 6, 42)
            win4.bkgd(' ', COLOR_1)
            box4 = Textbox(win4)
            stdscr.refresh()
            box4.edit()
            pwd = box4.gather().replace('\n', '')

            # Muestra de mensaje cifrado
            stdscr.addstr(11, 0, "Mensaje:")
            crypted_text = fun.desencriptar(text, pwd)
            stdscr.addstr(12, 0, crypted_text, COLOR_3)
            stdscr.addstr(18, 0, "Presiona cualquier tecla para volver.", COLOR_4)
            stdscr.getch()
        elif key == ord('c'):
            break


wrapper(main)
