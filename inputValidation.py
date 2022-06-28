from Job import Job
from JobHandling import JobHandling
from Statistic import Statistic


class InputValidation:

    job = Job()
    job_handling = JobHandling()
    stat = Statistic()

    def validate_int(self, var_to_validate, error_message):
        try:
            var_to_validate = int(var_to_validate)
        except:
            print(error_message)
            return " "
        else:
            return (int(var_to_validate))

    def validate_job_ID(self, var_to_validate):
        var_to_validate = self.validate_int(
            var_to_validate, "Error: Please enter a number")
        if var_to_validate == " ":
            return False
        else:
            if 0 < var_to_validate and var_to_validate < self.job.count_jobs + 1:
                return (int(var_to_validate))
            else:
                print("Error: Given ID does not exist")
                return False

    def validate_stat_ID(self, var_to_validate):
        var_to_validate = self.validate_int(
            var_to_validate, "Error: Please enter a number")

        if 0 < var_to_validate and var_to_validate < len(self.stat.stats_list) + 1:
            return (int(var_to_validate))
        else:
            print("Error: Given ID does not exist")
            return False

    def validate_status(self, var_to_validate):
        if var_to_validate.lower() == "success" or var_to_validate.lower() == "failed" or var_to_validate.lower() == "skipped" or var_to_validate.lower() == "canceled":
            return (var_to_validate)
        else:
            print("Error: Invalid entry for this field")
            return " "

    def validate_float(self, var_to_validate):
        try:
            var_to_validate = float(var_to_validate)
        except:
            print("Error: Please enter a decimal (can be an integer)")
            return " "
        else:
            return float(round(var_to_validate, 3))

    def validate_string(self, var_to_validate):
        if var_to_validate == "" or var_to_validate == " ":
            print("Error: Please enter a phrase")
            return " "
        else:
            return var_to_validate
