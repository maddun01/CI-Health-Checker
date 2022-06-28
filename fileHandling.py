class FileHandling:

    def __init__(self):
        self.jobs_filename = "Jobs.csv"
        self.stats_filename = "Stats.csv"

    def open_file(self, filename, mode):
        if filename == "jobs":
            if mode == "a":
                self.jobs_file = open(self.jobs_filename, "a")
            elif mode == "r":
                self.jobs_file = open(self.jobs_filename, "r")
            elif mode == "n":
                self.jobs_file = open(self.jobs_filename, "a", newline="")
        elif filename == "stats":
            if mode == "a":
                self.stats_file = open(self.stats_filename, "a")
            elif mode == "r":
                self.stats_file = open(self.stats_filename, "r")

    def close_file(self, filename):
        if filename == "jobs":
            self.jobs_file.close()
        elif filename == "stats":
            self.stats_file.close()

    def wipe_file(self, filename):
        if filename == "jobs":
            self.jobs_file = open(self.jobs_filename, "w")
            self.jobs_file.truncate()
            self.close_file("jobs")
        elif filename == "stats":
            self.stats_file = open(self.stats_filename, "w")
            self.stats_file.truncate()
            self.close_file("stats")

    def write_header_to_file(self, filename):
        if filename == "jobs":
            self.open_file("jobs", "a")
            self.jobs_file.write(
                "ID,JOBID,NAME,PROJECTID,QUEUEDDURATION,DURATION,STATUS\n")
            self.close_file("jobs")
        elif filename == "stats":
            self.open_file("stats", "a")
            self.stats_file.write(
                "ID,NAME,INSTANCES,AVERAGEQUEUEDDURATION,AVERAGEDURATION,PASSES,FAILS,SKIPS,CANCELLATIONS\n")
            self.close_file("stats")
