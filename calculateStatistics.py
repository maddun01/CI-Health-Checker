class CalculateStatistics:

    def __init__(self):
        self.number_of_instances = 0
        self.number_of_passes = 0
        self.number_of_fails = 0
        self.number_of_skips = 0
        self.number_of_cancellations = 0
        self.average_queued_duration_list = []
        self.average_duration_list = []

    def calculate_instances(self):
        self.number_of_instances += 1

    def collect_average_durations(self, av_duration, duration_type):
        if duration_type == "queued":
            if av_duration == "None":
                pass
            else:
                self.average_queued_duration_list.append(float(av_duration))
        elif duration_type == "duration":
            if av_duration == "None":
                pass
            else:
                self.average_duration_list.append(float(av_duration))

    def calculate_average_durations(self):
        self.average_queued_duration = 0
        if len(self.average_queued_duration_list) != 0:
            for i in self.average_queued_duration_list:
                self.average_queued_duration += i
            self.average_queued_duration = round(
                self.average_queued_duration / len(self.average_queued_duration_list), 3)
        else:
            self.average_queued_duration = "None"

        self.average_duration = 0
        if len(self.average_duration_list) != 0:
            for i in self.average_duration_list:
                self.average_duration += i
            self.average_duration = round(
                self.average_duration / len(self.average_duration_list), 3)
        else:
            self.average_duration = "None"

    def calculate_status(self, status):
        if status == "success":
            self.number_of_passes += 1
        elif status == "failed":
            self.number_of_fails += 1
        elif status == "skipped":
            self.number_of_skips += 1
        elif status == "canceled":
            self.number_of_cancellations += 1

    def reset_statistics(self):
        self.number_of_instances = 0
        self.number_of_passes = 0
        self.number_of_fails = 0
        self.number_of_skips = 0
        self.number_of_cancellations = 0
        self.average_queued_duration_list.clear()
        self.average_duration_list.clear()
