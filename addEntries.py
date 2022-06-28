from DataUI import DataUI
from FileHandling import FileHandling
from InputValidation import InputValidation
from Job import Job
from JobHandling import JobHandling
from MenuUI import MenuUI


class AddEntries:

    data_UI = DataUI()
    file_handling = FileHandling()
    input_validation = InputValidation()
    job = Job()
    job_handling = JobHandling()
    menu_UI = MenuUI()

    def __init__(self):
        self.new_jobs_entry = {}
        self.to_return = False

    def add_data(self):
        fields = [
            ("Enter the job's ID: ", "JOBID", lambda user_input: self.input_validation.validate_int(
                user_input, "Error: Please enter a number")),
            ("Enter the job's name: ", "NAME",
             lambda user_input: self.input_validation.validate_string(user_input)),
            ("Enter the job's project ID: ", "PROJECTID", lambda user_input: self.input_validation.validate_int(
                user_input, "Error: Please enter a number")),
            ("Enter the job's queued duration: ", "QUEUEDDURATION",
             lambda user_input: self.input_validation.validate_float(user_input)),
            ("Enter the job's duration: ", "DURATION",
             lambda user_input: self.input_validation.validate_float(user_input)),
            ("Enter the job's status (success, failed, skipped or canceled): ", "STATUS",
             lambda user_input: self.input_validation.validate_status(user_input))
        ]
        while self.to_return != True:
            self.new_jobs_entry = {}
            self.new_jobs_entry["ID"] = self.job.count_jobs + 1
            print(self.menu_UI.return_to_menu_header)
            for user_prompt, field, validation_type in fields:
                user_input = " "
                while user_input == " ":
                    user_input = input(user_prompt)
                    if user_input.upper() == "Q":
                        return
                    else:
                        user_input = validation_type(user_input)
                        self.new_jobs_entry[field] = user_input
            self.data_UI.display_temp_data(self.new_jobs_entry)
            self.save_jobs_data()

    def save_jobs_data(self):
        choice = input("Are you sure you want to save? (Y/N/Q) ")
        if choice.upper() == "Y":
            self.job.jobs_list.append(self.new_jobs_entry)
            self.job_handling.save_to_jobs_file()
            print("\nNew entry saved")
            self.job_handling.recalculate_statistics()
        elif choice.upper() == "Q":
            self.to_return = True
            return
        self.reset_variables()

    def reset_variables(self):
        self.new_jobs_entry = {}
        self.to_return = False
