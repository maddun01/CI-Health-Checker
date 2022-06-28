from CalculateStatistics import CalculateStatistics
from FileHandling import FileHandling
from Job import Job
from Statistic import Statistic


class JobHandling:

    calculate_statistics = CalculateStatistics()
    file_handling = FileHandling()
    job = Job()
    stat = Statistic()

    unique_jobs_list = []
    jobs_field_names = ["ID", "JOBID", "NAME", "PROJECTID",
                        "QUEUEDDURATION", "DURATION", "STATUS"]

    def unique_jobs(self):
        if self.job.count_jobs == 0:
            self.job.get_jobs()
        for item in self.job.jobs_list:
            name = item["NAME"]
            if name not in self.unique_jobs_list:
                self.unique_jobs_list.append(name)

    def call_statistics(self):
        if len(self.unique_jobs_list) == 0:
            self.unique_jobs()

        self.file_handling.write_header_to_file("stats")
        self.file_handling.open_file("stats", "a")
        id_number = 1
        for unique_job in self.unique_jobs_list:
            for item in self.job.jobs_list:
                job_name = item["NAME"]
                if job_name == unique_job:
                    self.calculate_statistics.calculate_instances()
                    self.calculate_statistics.collect_average_durations(
                        item["QUEUEDDURATION"], "queued")
                    self.calculate_statistics.collect_average_durations(
                        item["DURATION"], "duration")
                    self.calculate_statistics.calculate_status(
                        item["STATUS"].strip("\n"))
            self.calculate_statistics.calculate_average_durations()
            self.file_handling.stats_file.write(str(id_number) + "," + "\"" + str(unique_job) + "\"" + "," + str(
                self.calculate_statistics.number_of_instances) + "," + str(self.calculate_statistics.average_queued_duration) + "," + str(
                self.calculate_statistics.average_duration) + "," + str(self.calculate_statistics.number_of_passes) + "," + str(
                self.calculate_statistics.number_of_fails) + "," + str(self.calculate_statistics.number_of_skips) + "," + str(
                self.calculate_statistics.number_of_cancellations) + "\n")

            self.calculate_statistics.reset_statistics()
            id_number += 1
        self.file_handling.close_file("stats")
        self.stat.clear_stats_list()
        self.stat.get_stats()

    def recalculate_statistics(self):
        print("Changes to jobs file detected - recalculating statistics")
        self.file_handling.wipe_file("stats")
        self.unique_jobs_list.clear()
        self.call_statistics()

    def save_to_jobs_file(self):
        self.file_handling.open_file("jobs", "n")
        for item in self.job.jobs_list:
            self.file_handling.jobs_file.write(str(item["ID"]) + "," + str(item["JOBID"]) + "," + "\"" + str(item["NAME"]) + "\"" + "," + str(
                item["PROJECTID"]) + "," + str(item["QUEUEDDURATION"]) + "," + str(item["DURATION"]) + "," + str(item["STATUS"]) + "\n")
        self.file_handling.close_file("jobs")

    def append_to_jobs_file(self, new_entry):
        self.file_handling.open_file("jobs", "a")
        self.file_handling.jobs_file.write(new_entry + "\n")
        self.file_handling.close_file("jobs")
        self.job.clear_jobs_list()
        self.job.get_jobs()

    @property
    def unique_jobs_return(self):
        return(self.unique_jobs_list)

    @property
    def count_unique_jobs(self):
        return(len(self.unique_jobs_list))
