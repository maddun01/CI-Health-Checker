from dataUI import DataUI
from fileHandling import FileHandling
from inputValidation import InputValidation
from job import Job
from jobHandling import JobHandling
from menuUI import MenuUI


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
                id_to_remove = self.input_validation.validate_job_ID(id_to_remove)
                if id_to_remove == False:
                    pass
                else:
                    self.data_UI.display_by_id("jobs", id_to_remove)
                    choice = input("Are you sure you want to delete this? (Y/N/Q): ")
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
            line[0] = int(line[0]) - 1
        self.update_file()

    def update_file(self):
        self.file_handling.wipe_file("jobs")
        self.file_handling.write_header_to_file("jobs")
        for item in self.job.jobs_list:
            self.file_handling.jobs_file.write(str(item[0]) + "," + str(item[1]) + "," + "\"" + str(
                item[2]) + "\"" + "," + str(item[3]) + "," + str(item[4]) + "," + str(item[5]) + "," + str(item[6]) + "\n")
        self.file_handling.close_file("jobs")
        print("Jobs file updated\n")
        self.job_handling.recalculate_statistics()
