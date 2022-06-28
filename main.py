from addEntries import AddEntries
from dataUI import DataUI
from deleteEntries import DeleteEntries
from editEntries import EditEntries
from inputValidation import InputValidation
from menuUI import MenuUI
from startup import StartUp


def main():
    while(1):
        menu_UI.display_menu()
        user_choice = input_validation.validate_int(
            input("\nSelect an option: "), "Error: Please enter a number (0-5)")

        if user_choice == 1:
            print("\nDisplay all jobs or all statistics\n")
            print(menu_UI.return_to_menu_header)
            menu_UI.jobs_or_stats()
            choice = input("Select an option: ")
            if choice.upper() == "Q":
                pass
            else:
                choice = input_validation.validate_int(
                    choice, "Error: Please enter a number (0-5)")
                if choice == 1:
                    data_UI.display("jobs")
                elif choice == 2:
                    data_UI.display("stats")

        elif user_choice == 2:
            print("\nDisplay a specific job or statistic\n")
            print(menu_UI.return_to_menu_header)
            menu_UI.jobs_or_stats()
            choice = input("Select an option: ")
            if choice.upper() == "Q":
                pass
            else:
                choice = input_validation.validate_int(
                    choice, "Error: Please enter a number (0-5)")
                if choice == 1:
                    entry_choice = input_validation.validate_job_ID(
                        input("Enter job ID: "))
                    if entry_choice == False:
                        pass
                    else:
                        data_UI.display_by_id("jobs", entry_choice)
                elif choice == 2:
                    entry_choice = input_validation.validate_stat_ID(
                        input("Enter statistic ID: "))
                    if entry_choice == False:
                        pass
                    else:
                        data_UI.display_by_id("stats", entry_choice)

        elif user_choice == 3:
            print("\nSearch jobs or statistics\n")
            print(menu_UI.return_to_menu_header)
            menu_UI.jobs_or_stats()
            choice = input("Select an option: ")
            if choice.upper() == "Q":
                pass
            else:
                choice = input_validation.validate_int(choice, "Error: Please enter a number (0-5)")
                if choice == 1:
                    search_phrase = input("Enter a search phrase to use: ")
                    if search_phrase.upper() == "Q":
                        pass
                    else:
                        data_UI.search_records("jobs", search_phrase)
                elif choice == 2:
                    search_phrase = input("Enter a search phrase to use: ")
                    if search_phrase.upper() == "Q":
                        pass
                    else:
                        data_UI.search_records("stats", search_phrase)

        elif user_choice == 4:
            print("\nAdd a record\n")
            add_entries.add_jobs_data()

        elif user_choice == 5:
            print("\nEdit a record\n")
            edit_entries.choose_data_to_edit()
        elif user_choice == 6:
            print("\nDelete a record\n")
            delete_entries.choose_data_to_remove()

        elif user_choice == 0:
            quit_choice = input("0: Quit. Are you sure (Y/N)? ")
            if quit_choice.upper() == "Y":
                break
            else:
                pass


add_entries = AddEntries()
data_UI = DataUI()
delete_entries = DeleteEntries()
edit_entries = EditEntries()
input_validation = InputValidation()
menu_UI = MenuUI()
start_up = StartUp()

start_up.start_up()
main()
