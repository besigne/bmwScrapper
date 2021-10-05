from simple_term_menu import TerminalMenu


def main():
    options = ['BMW Scrapper', 'Audi Scrapper']
    terminal_menu = TerminalMenu(options,
                                 title="Select one scrapper to run: ",
                                 )
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == 'BMW Scrapper':
        exec(open('scrapper/bmw.py').read())
    else:
        print('Audi Scrapper is not available yet')


if __name__ == "__main__":
    main()
