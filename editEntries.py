from DataUI import DataUI
from DeleteEntries import DeleteEntries
from FileHandling import FileHandling
from InputValidation import InputValidation
from Job import Job
from JobHandling import JobHandling
from MenuUI import MenuUI


class EditEntries:

    data_UI = DataUI()
    delete_entries = DeleteEntries()
    file_handling = FileHandling()
    input_validation = InputValidation()
    job = Job()
    job_handling = JobHandling()
    menu_UI = MenuUI()

    def __init__(self):
        self.to_validate = False
        self.id_to_edit = False
        self.to_return = False
        self.edited_entry = {}

    def choose_data_to_edit(self):
        while self.id_to_edit == False:
            if self.to_return == True:
                self.to_return = False
                return
            else:
                print(self.menu_UI.return_to_menu_header)
                self.id_to_edit = input("Enter the ID of the job to edit: ")
                if self.id_to_edit.upper() == "Q":
                    self.reset_variables()
                    return
                else:
                    self.id_to_edit = self.input_validation.validate_job_ID(
                        self.id_to_edit)
                    if self.id_to_edit == False:
                        pass
                    else:
                        self.data_UI.display_by_id("jobs", self.id_to_edit)
                        choice = input(
                            "Are you sure you want to edit this? (Y/N/Q): ")
                        if choice.upper() == "Y":
                            self.edit_data(self.id_to_edit)
                        elif choice.upper() == "N":
                            self.id_to_edit = False
                        elif choice.upper() == "Q":
                            self.reset_variables()
                            self.to_return = False
                            return

    def edit_data(self, id_to_edit):
        fields = [
            ("Enter the job's new ID: ", "JOBID", lambda user_input: self.input_validation.validate_int(
                user_input, "Error: Please enter a number")),
            ("Enter the job's new name: ", "NAME",
             lambda user_input: self.input_validation.validate_string(user_input)),
            ("Enter the job's new project ID: ", "PROJECTID", lambda user_input: self.input_validation.validate_int(
                user_input, "Error: Please enter a number")),
            ("Enter the job's new queued duration: ", "QUEUEDDURATION",
             lambda user_input: self.input_validation.validate_float(user_input)),
            ("Enter the job's new duration: ", "DURATION",
             lambda user_input: self.input_validation.validate_float(user_input)),
            ("Enter the job's new status (success, failed, skipped or canceled): ",
             "STATUS", lambda user_input: self.input_validation.validate_status(user_input))
        ]
        while self.to_return != True:
            print("Enter the new values, or leave blank to leave unchanged\n")
            self.item = self.job.jobs_list[id_to_edit-1]
            self.edited_entry = {}
            self.edited_entry["ID"] = id_to_edit

            for user_prompt, field, validation_type in fields:
                user_input = " "
                while user_input == " ":
                    user_input = input(user_prompt)
                    if user_input.upper() == "Q":
                        return
                    else:
                        user_input = self.is_null(user_input, field)
                        if self.to_validate == True:
                            user_input = validation_type(user_input)
                        self.edited_entry[field] = user_input
            self.data_UI.display_temp_data(self.edited_entry)
            self.save_changes()

    def is_null(self, var_to_check, key):
        if var_to_check == "":
            self.to_validate = False
            return(self.item[key])
        else:
            self.to_validate = True
            return(var_to_check)

    def save_changes(self):
        choice = input("Are you sure you want to save? (Y/N/Q) ")
        if choice.upper() == "Y":
            self.job.jobs_list[self.id_to_edit - 1] = self.edited_entry
            self.delete_entries.update_file()
        elif choice.upper() == "Q":
            self.to_return = True
            return
        self.reset_variables()

    def reset_variables(self):
        self.to_validate = False
        self.id_to_edit = False
        self.to_return = False
        self.edited_entry = {}
