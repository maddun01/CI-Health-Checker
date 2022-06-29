from fileHandling import FileHandling
from job import Job
import os
from jobHandling import JobHandling
from statistic import Statistic
from gitlabAccess import GitlabAccess


class StartUp:

    file_handling = FileHandling()
    job_handling = JobHandling()
    stat = Statistic()
    gitlab_access = GitlabAccess()
    job = Job()

    def start_up(self):
        job_filesize = os.path.getsize(self.file_handling.jobs_filename)
        if job_filesize == 0:
            print("Empty jobs file detected - fetching from GitLab")
            self.gitlab_access.store_jobs()
            self.job.get_jobs()
            print("New contents in jobs file detected - recalculating statistics")
            self.file_handling.wipe_file("stats")
            self.job_handling.call_statistics()
        if self.job.count_jobs == 0:
            self.job.get_jobs()

        stat_filesize = os.path.getsize(self.file_handling.stats_filename)
        if stat_filesize == 0:
            print("Empty statistics file detected - calculating statistics")
            self.job_handling.call_statistics()
        if self.stat.count_stats == 0:
            self.stat.get_stats()
