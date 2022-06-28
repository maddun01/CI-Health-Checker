from DataUI import DataUI
from FileHandling import FileHandling
from InputValidation import InputValidation
from Job import Job
from JobHandling import JobHandling
from MenuUI import MenuUI


class DeleteEntries:

    data_UI = DataUI()
    file_handling = FileHandling()
    input_validation = InputValidation()
    job = Job()
    job_handling = JobHandling()
    menu_UI = MenuUI()
    to_return = False

    def choose_data_to_remove(self):
        while self.to_return == False:
            print(self.menu_UI.return_to_menu_header)
            id_to_remove = input("Enter the ID of the job to delete: ")
            if id_to_remove.upper() == "Q":
                return
            else:
                id_to_remove = self.input_validation.validate_job_ID(
                    id_to_remove)
                if id_to_remove == False:
                    pass
                else:
                    self.data_UI.display_by_id("jobs", id_to_remove)
                    choice = input(
                        "Are you sure you want to delete this? (Y/N/Q): ")
                    if choice.upper() == "Y":
                        self.remove_data(id_to_remove)
                        return
                    elif choice.upper() == "N":
                        pass
                    elif choice.upper() == "Q":
                        return

    def remove_data(self, id_to_remove):
        self.job.jobs_list.pop(id_to_remove-1)
        for i in range(id_to_remove-1, self.job.count_jobs):
            line = self.job.jobs_list[i]
            line["ID"] = int(line["ID"]) - 1
        self.update_file()

    def update_file(self):
        self.file_handling.wipe_file("jobs")
        self.file_handling.write_header_to_file("jobs")
        self.job_handling.save_to_jobs_file()
        print("Jobs file updated\n")
        self.job_handling.recalculate_statistics()
