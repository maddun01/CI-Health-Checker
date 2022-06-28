from calculateStatistics import CalculateStatistics
from fileHandling import FileHandling
from job import Job
from statistic import Statistic


class JobHandling:

    calculate_statistics = CalculateStatistics()
    file_handling = FileHandling()
    job = Job()
    stat = Statistic()

    unique_jobs_list = []

    def unique_jobs(self):
        if len(self.job.jobs_list) == 0:
            self.job.get_jobs()
        for item in self.job.jobs_list:
            name = item[2]
            if name not in self.unique_jobs_list:
                self.unique_jobs_list.append(name)

    def call_statistics(self):
        if len(self.unique_jobs_list) == 0:
            self.unique_jobs()

        self.file_handling.write_header_to_file("stats")
        id_number = 1
        for unique_job in self.unique_jobs_list:
            for item in self.job.jobs_list:
                job_name = item[2]
                if job_name == unique_job:
                    self.calculate_statistics.calculate_instances()
                    self.calculate_statistics.collect_average_durations(
                        item[4], "queued")
                    self.calculate_statistics.collect_average_durations(
                        item[5], "duration")
                    self.calculate_statistics.calculate_status(
                        item[6].strip("\n"))
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
        print("Changes to job file detected - recalculating statistics")
        self.file_handling.wipe_file("stats")
        self.unique_jobs_list.clear()
        self.call_statistics()

    @property
    def unique_jobs_return(self):
        return(self.unique_jobs_list)

    @property
    def count_unique_jobs(self):
        return(len(self.unique_jobs_list))
