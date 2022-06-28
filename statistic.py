import csv
from FileHandling import FileHandling


class Statistic:

    file_handling = FileHandling()

    stats_list = []

    def get_stats(self):
        self.file_handling.open_file("stats", "r")
        csv_reader = csv.DictReader(self.file_handling.stats_file)
        for stat in csv_reader:
            self.stats_list.append(stat)
        self.file_handling.close_file("stats")

    def clear_stats_list(self):
        self.stats_list.clear()

    @property
    def count_stats(self):
        return(len(self.stats_list))
