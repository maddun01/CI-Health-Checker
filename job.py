import csv
from FileHandling import FileHandling


class Job:

    file_handling = FileHandling()

    jobs_list = []

    def get_jobs(self):
        self.file_handling.open_file("jobs", "r")
        csv_reader = csv.DictReader(self.file_handling.jobs_file)
        for job in csv_reader:
            self.jobs_list.append(job)
        self.file_handling.close_file("jobs")

    def clear_jobs_list(self):
        self.jobs_list.clear()

    @property
    def count_jobs(self):
        return(len(self.jobs_list))
