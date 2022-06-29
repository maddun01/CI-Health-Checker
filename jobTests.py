from job import Job
import unittest


class JobTests(unittest.TestCase):

    job = Job()

    # Test the get_stats method by adding items to the file,
    # then calling the method and checking the length is correct.
    # The test also makes sure the header is deleted from the list
    def test_get_jobs(self):
        # Arrange
        file = open("jobs.csv", "w")
        file.write("This line should be deleted\n")
        for i in range(5):
            file.write(f"This is line {i}\n")
        file.close()
        ls = ["This line should be deleted"]

        # Act
        self.job.get_jobs()
        file = open("jobs.csv", "w")
        file.truncate(0)
        file.close()

        # Assert
        self.assertEqual(5, len(self.job.jobs_list))
        self.assertNotIn(ls, self.job.jobs_list)

# Tests the clear_jobs method by adding items to jobs_list,
# then calling the method and verifying the list is empty
    def test_clear_jobs_list(self):
        # Arrange
        for i in range(10):
            self.job.jobs_list.append(i)

        # Act
        self.job.clear_jobs_list()

        # Assert
        self.assertEqual(0, len(self.job.jobs_list))
