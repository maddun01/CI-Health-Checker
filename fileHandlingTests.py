from fileHandling import FileHandling
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
        file = open("jobs.csv", "w")
        file.write("Add this to the file")
        file.close()
        contents = []

        # Act
        self.file_handling.wipe_file("jobs")
        file = open("jobs.csv", "r")
        for item in file:
            contents.append(item)
        file.close()

        # Assert
        self.assertEqual(0, len(contents))

    def test_wipe_stats_file(self):
        # Arrange
        file = open("stats.csv", "w")
        file.write("Add this to the file")
        file.close()
        contents = []

        # Act
        self.file_handling.wipe_file("stats")
        file = open("stats.csv", "r")
        for item in file:
            contents.append(item)
        file.close()

        # Assert
        self.assertEqual(0, len(contents))

    def test_write_jobs_header(self):
        #Arrange
        file = open("jobs.csv", "w")
        file.truncate(0)
        file.close()

        #Act
        self.file_handling.write_header_to_file("jobs")
        self.file_handling.jobs_file.close()
        
        file = open("jobs.csv", "r")
        line = file.readline()
        file.close()

        #Assert
        self.assertEqual("ID,JOBID,NAME,PROJECTID,QUEUEDDURATION,DURATION,STATUS\n", line)
        file = open("jobs.csv", "w")
        file.truncate(0)
        file.close()

    def test_write_stats_header(self):
        #Arrange
        file = open("stats.csv", "w")
        file.truncate(0)
        file.close()

        #Act
        self.file_handling.write_header_to_file("stats")
        self.file_handling.stats_file.close()
        
        file = open("stats.csv", "r")
        line = file.readline()
        file.close()

        #Assert
        self.assertEqual("ID,NAME,INSTANCES,AVERAGEQUEUEDDURATION,AVERAGEDURATION,PASSES,FAILS,SKIPS,CANCELLATIONS\n", line)
        file = open("stats.csv", "w")
        file.truncate(0)
        file.close()

