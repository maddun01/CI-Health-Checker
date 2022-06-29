from dataUI import DataUI
from fileHandling import FileHandling
from inputValidation import InputValidation
from job import Job
from jobHandling import JobHandling
from menuUI import MenuUI


class AddEntries:

    data_UI = DataUI()
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
        self.new_jobs_entry = ""
        self.added_id = ""
        self.to_return = False

    def add_jobs_data(self):
        while self.to_return == False:
            print(self.menu_UI.return_to_menu_header)
            self.added_id = (self.job.count_jobs) + 1
            while self.id_number == " ":
                self.id_number = input("Enter the job's ID: ")
                if self.id_number.upper() == "Q":
                    self.reset_variables()
                    return
                else:
                    self.id_number = self.input_validation.validate_int(
                        self.id_number, "Error: Please enter a number")

            while self.name == " ":
                self.name = input("Enter the job's name: ")
                if self.name.upper() == "Q":
                    self.reset_variables()
                    return
                else:
                    self.name = self.input_validation.validate_string(
                        self.name)

            while self.project_id == " ":
                self.project_id = input("Enter the job's project ID: ")
                if self.project_id.upper() == "Q":
                    self.reset_variables()
                    return
                else:
                    self.project_id = self.input_validation.validate_int(
                        self.project_id, "Error: Please enter a number")

            while self.queued_duration == " ":
                self.queued_duration = input(
                    "Enter the job's queued duration: ")
                if self.queued_duration.upper() == "Q":
                    self.reset_variables()
                    return
                else:
                    self.queued_duration = self.input_validation.validate_float(
                        self.queued_duration)

            while self.duration == " ":
                self.duration = input("Enter the job's duration: ")
                if self.duration.upper() == "Q":
                    self.reset_variables()
                    return
                else:
                    self.duration = self.input_validation.validate_float(
                        self.duration)

            while self.status == " ":
                self.status = input(
                    "Enter the job's status (success, failed, skipped or canceled): ")
                if self.status.upper() == "Q":
                    self.reset_variables()
                    return
                else:
                    self.status = self.input_validation.validate_status(
                        self.status)

            self.new_jobs_entry = self.format_jobs_entry.format(
                self.added_id, self.id_number, self.name, self.project_id, self.queued_duration, self.duration, self.status)
            self.data_UI.display_temp_data(self.new_jobs_entry)
            self.save_jobs_data()
        self.to_return = False

    def save_jobs_data(self):
        choice = input("Are you sure you want to save? (Y/N/Q) ")
        if choice.upper() == "Y":
            self.file_handling.open_file("jobs", "a")
            self.file_handling.jobs_file.write(self.new_jobs_entry + "\n")
            self.file_handling.close_file("jobs")
            self.job.clear_jobs_list()
            self.job.get_jobs()
            print("\nNew entry saved")
            self.job_handling.recalculate_statistics()
        elif choice.upper() == "Q":
            self.to_return = True
            pass
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
        self.added_id = " "
