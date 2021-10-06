from simple_term_menu import TerminalMenu


def main():
    options = ['BMW Scrapper', 'Audi Scrapper', 'exit']
    terminal_menu = TerminalMenu(options,
                                 title="Select one scrapper to run: ",
                                 )
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == 'BMW Scrapper':
        exec(open('scrapper/bmw.py').read())
    elif options[menu_entry_index] == 'Audi Scrapper':
        exec(open('scrapper/audi.py').read())
    else:
        print('Goodbye!')


if __name__ == "__main__":
    main()
