from dataUI import DataUI
from deleteEntries import DeleteEntries
from fileHandling import FileHandling
from inputValidation import InputValidation
from job import Job
from jobHandling import JobHandling
from menuUI import MenuUI


class EditEntries:

    data_UI = DataUI()
    delete_entries = DeleteEntries()
    file_handling = FileHandling()
    input_validation = InputValidation()
    job = Job()
    job_handling = JobHandling()
    menu_UI = MenuUI()

    def __init__(self):
        self.format_jobs_entry = "{},{},\"{}\",{},{},{},{}"
        self.name = " "
        self.project_id = " "
        self.queued_duration = " "
        self.duration = " "
        self.status = " "
        self.id_number = " "
        self.instances = " "
        self.passes = " "
        self.fails = " "
        self.skips = " "
        self.cancellations = " "
        self.new_jobs_entry = " "
        self.to_validate = ""
        self.id_to_edit = False
        self.to_return = False

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
        print("Enter the new values, or leave blank to leave unchanged\n")
        self.item = self.job.jobs_list[id_to_edit-1]
        while self.id_number == " ":
            self.id_number = input("Enter the job's new ID: ")
            if self.id_number.upper() == "Q":
                self.reset_variables()
                self.to_return = True
                return
            else:
                self.id_number = self.is_null(self.id_number, 1)
                if self.to_validate == True:
                    self.id_number = self.input_validation.validate_int(
                        self.id_number, "Error: Please enter a number")

        while self.name == " ":
            self.name = input("Enter the job's new name: ")
            if self.name.upper() == "Q":
                self.reset_variables()
                self.to_return = True
                return
            else:
                self.name = self.is_null(self.name, 2)

        while self.project_id == " ":
            self.project_id = input("Enter the job's new project ID: ")
            if self.project_id.upper() == "Q":
                self.reset_variables()
                self.to_return = True
                return
            else:
                self.project_id = self.is_null(self.project_id, 3)
                if self.to_validate == True:
                    self.project_id = self.input_validation.validate_int(
                        self.project_id, "Error: Please enter a number")

        while self.queued_duration == " ":
            self.queued_duration = input(
                "Enter the job's new queued duration: ")
            if self.queued_duration.upper() == "Q":
                self.reset_variables()
                self.to_return = True
                return
            else:
                self.queued_duration = self.is_null(self.queued_duration, 4)
                if self.to_validate == True:
                    self.queued_duration = self.input_validation.validate_float(
                        self.queued_duration)

        while self.duration == " ":
            self.duration = input("Enter the job's new duration: ")
            if self.duration.upper() == "Q":
                self.reset_variables()
                self.to_return = True
                return
            else:
                self.duration = self.is_null(self.duration, 5)
                if self.to_validate == True:
                    self.duration = self.input_validation.validate_float(
                        self.duration)

        while self.status == " ":
            self.status = input("Enter the job's new status: ")
            if self.status.upper() == "Q":
                self.reset_variables()
                self.to_return = True
                return
            else:
                self.status = self.is_null(self.status, 6)
                if self.to_validate == True:
                    self.status = self.input_validation.validate_status(
                        self.status)

        self.new_jobs_entry = self.format_jobs_entry.format(
            self.item[0], self.id_number, self.name, self.project_id, self.queued_duration, self.duration, self.status)
        self.data_UI.display_temp_data(self.new_jobs_entry)
        self.save_changes()

    def is_null(self, var_to_check, pos):
        if var_to_check == "":
            self.to_validate = False
            return(self.item[pos])
        else:
            self.to_validate = True
            return(var_to_check)

    def save_changes(self):
        choice = input("Are you sure you want to save? (Y/N/Q) ")
        if choice.upper() == "Y":
            self.job.jobs_list[self.id_to_edit - 1][1] = self.id_number
            self.job.jobs_list[self.id_to_edit - 1][2] = self.name
            self.job.jobs_list[self.id_to_edit - 1][3] = self.project_id
            self.job.jobs_list[self.id_to_edit - 1][4] = self.queued_duration
            self.job.jobs_list[self.id_to_edit - 1][5] = self.duration
            self.job.jobs_list[self.id_to_edit - 1][6] = self.status
            self.delete_entries.update_file()
            self.to_return = True
        elif choice.upper() == "Q":
            self.reset_variables()
            self.to_return = True
            return
        self.reset_variables()

    def reset_variables(self):
        self.name = " "
        self.project_id = " "
        self.queued_duration = " "
        self.duration = " "
        self.status = " "
        self.id_number = " "
        self.instances = " "
        self.passes = " "
        self.fails = " "
        self.skips = " "
        self.cancellations = " "
        self.new_jobs_entry = " "
        self.id_to_edit = False
