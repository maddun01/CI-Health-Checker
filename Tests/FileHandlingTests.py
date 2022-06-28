from FileHandling import FileHandling
import unittest


class FileHandlingTests(unittest.TestCase):

    file_handling = FileHandling()

    def test_open_jobs_file_readable(self):
        # Act
        self.file_handling.open_file("jobs", "r")

        # Assert
        self.assertTrue(self.file_handling.jobs_file.readable())
        self.file_handling.jobs_file.close()

    def test_open_jobs_file_writable(self):
        # Act
        self.file_handling.open_file("jobs", "a")

        # Assert
        self.assertTrue(self.file_handling.jobs_file.writable())
        self.file_handling.jobs_file.close()

    def test_open_stats_file_readable(self):
        # Act
        self.file_handling.open_file("stats", "r")

        # Assert
        self.assertTrue(self.file_handling.stats_file.readable())
        self.file_handling.stats_file.close()

    def test_open_stats_file_writable(self):
        # Act
        self.file_handling.open_file("stats", "a")

        # Assert
        self.assertTrue(self.file_handling.stats_file.writable())
        self.file_handling.stats_file.close()

    def test_wipe_jobs_file(self):
        # Arrange
        file = open("Jobs.csv", "w")
        file.write("Add this to the file")
        file.close()
        contents = []

        # Act
        self.file_handling.wipe_file("jobs")
        file = open("Jobs.csv", "r")
        for item in file:
            contents.append(item)
        file.close()

        # Assert
        self.assertEqual(0, len(contents))

    def test_wipe_stats_file(self):
        # Arrange
        file = open("Stats.csv", "w")
        file.write("Add this to the file")
        file.close()
        contents = []

        # Act
        self.file_handling.wipe_file("stats")
        file = open("Stats.csv", "r")
        for item in file:
            contents.append(item)
        file.close()

        # Assert
        self.assertEqual(0, len(contents))

    def test_write_jobs_header(self):
        # Arrange
        file = open("Jobs.csv", "w")
        file.close()
        COMPARISON_STRING = "ID,JOBID,NAME,PROJECTID,QUEUEDDURATION,DURATION,STATUS\n"

        # Act
        self.file_handling.write_header_to_file("jobs")

        file = open("Jobs.csv", "r")
        line = file.readline()
        file.close()

        # Assert
        self.assertEqual(COMPARISON_STRING, line)
        file = open("Jobs.csv", "w")
        file.close()

    def test_write_stats_header(self):
        # Arrange
        file = open("Stats.csv", "w")
        file.close()
        COMPARISON_STRING = "ID,NAME,INSTANCES,AVERAGEQUEUEDDURATION,AVERAGEDURATION,PASSES,FAILS,SKIPS,CANCELLATIONS\n"

        # Act
        self.file_handling.write_header_to_file("stats")

        file = open("Stats.csv", "r")
        line = file.readline()
        file.close()

        # Assert
        self.assertEqual(COMPARISON_STRING, line)
        file = open("Stats.csv", "w")
        file.close()
