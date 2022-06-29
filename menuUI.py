class MenuUI:
    def display_menu(self):
        print('''\nMenu
1. Display jobs or statistics
2. Display a specific job or statistic
3. Search jobs or statistics
4. Add a new job record
5. Edit a job record
6. Delete a job record
0. Quit''')

    def jobs_or_stats(self):
        print("1. Display jobs\n2. Display statistics\n")

    @property
    def return_to_menu_header(self):
        return ("Press Q at any time to return to the main menu\n")