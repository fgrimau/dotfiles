import os
import curses


def list_executables():
    places = ["/bin/", "/usr/bin/", "/usr/local/bin/"]
    executables = []
    for place in places:
        for entry in os.scandir(place):
            if entry.is_file() and entry.name not in executables:
                executables.append(entry.name)
    executables = sorted(executables)
    return executables


def get_choices(input, executables):
    if input != "":
        return [i for i in executables if input == i[:len(input)]]
    return executables


def drawall(stdscr, choices, selected, x_length):
    position_x = 0
    for index, executable in enumerate(choices[selected:]):
        if(index == 0):
            stdscr.attron(curses.color_pair(1))
        if position_x + len(executable) > x_length:
            chose = executable[:x_length - position_x]
            try:
                stdscr.addstr(1, position_x, chose)
            except curses.error:
                pass
            break
        stdscr.addstr(1, position_x, executable)
        if(index == 0):
            stdscr.attroff(curses.color_pair(1))
        position_x += len(executable) + 1
        try:
            stdscr.addstr(1, position_x-1, " ")
        except curses.error:
            pass


def main(stdscr):
    curses.curs_set(0)

    y_length, x_length = stdscr.getmaxyx()

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    executables = list_executables()
    running = True
    selected = 0
    input = ""

    while running:
        stdscr.addstr(0, 0, " "*(len(input) + 1))
        stdscr.addstr(0, 0, input)
        choices = get_choices(input, executables)
        stdscr.addstr(1, 0, " "*x_length)
        drawall(stdscr, choices, selected, x_length)

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_LEFT:
            if selected > 0:
                selected -= 1
        elif key == curses.KEY_RIGHT:
            if selected < len(choices) - 1:
                selected += 1
        elif chr(key) in ('KEY_ENTER', '\n'):
            to_ex = input if len(choices) == 0 else choices[selected]
            os.system("{} & disown;exit".format(to_ex))
            running = False
        elif chr(key) in ('KEY_BACKSPACE', '\b', '\x7f', 'ć'):
            input = input[:-1]  # Delete last char from the input
        elif chr(key) in ('KEY_TAB', '\t'):
            input = choices[0]  # Set the input to the first entry shown
        else:
            selected = 0
            input += chr(key)


curses.wrapper(main)
