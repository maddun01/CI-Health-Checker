import csv
from fileHandling import FileHandling


class Statistic:

    file_handling = FileHandling()

    stats_list = []

    def get_stats(self):
        self.file_handling.open_file("stats", "r")
        csv_reader = csv.reader(self.file_handling.stats_file)
        for job in csv_reader:
            self.stats_list.append(job)

        if self.count_stats == 0:
            pass
        else:
            self.stats_list.pop(0)

    def clear_stats_list(self):
        self.stats_list.clear()

    @property
    def count_stats(self):
        return(len(self.stats_list))
