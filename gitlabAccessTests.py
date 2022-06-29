from gitlabAccess import GitlabAccess
from key import Key
import csv
import unittest


class GitlabAccessTests(unittest.TestCase):

    gitlab_access = GitlabAccess()
    key = Key()

    # Tests the connect_to_gitlab method
    # Uses it to connect to the private server and fetch a specific pipeline
    # Validates that the information is fetched successfully
    def test_connect_to_gitlab(self):
        # Act
        gl = self.gitlab_access.connect_to_gitlab(self.key.token)
        project = gl.projects.get(420)
        pipeline = project.pipelines.get(52344)

        # Assert
        self.assertTrue(52344, pipeline.id)
        self.assertTrue(1, pipeline.iid)
        self.assertTrue(420, pipeline.project_id)
        self.assertTrue("failed", pipeline.status)

    # Tests the fetch_projects method
    # Uses it to fetch the project list and verifies it returns the correct number of items
    # Also checks two of the projects to make sure they're correct
    def test_fetch_projects(self):
        # Act
        self.gitlab_access.fetch_projects()

        # Assert
        self.assertEqual(26, len(self.gitlab_access.project_id_list))
        self.assertEqual([505, 502, 479, 477, 442, 434, 433, 427, 421, 420, 408, 406, 365, 314, 301,
                         295, 294, 282, 258, 247, 154, 153, 129, 128, 125, 123], self.gitlab_access.project_id_list)

    def test_store_jobs(self):
        # Arrange
        self.gitlab_access.project_id_list = ["434"]
        jobs_list = []
        file = open("jobs.csv", "w")
        file.truncate(0)
        file.close()
        header = ['ID', 'JOBID', 'NAME', 'PROJECTID',
                  'QUEUEDDURATION', 'DURATION', 'STATUS']

        # Act
        self.gitlab_access.store_jobs()
        file = open("jobs.csv", "r")
        csv_reader = csv.reader(file)
        for job in csv_reader:
            jobs_list.append(job)
        file.close()

        # Assert
        self.assertIn(header, jobs_list)
        self.assertEqual("504188", jobs_list[1][1])
        self.assertEqual("skipped", jobs_list[2][6])
        self.assertEqual("434", jobs_list[4][3])
        #file = open("jobs.csv", "w")
        #file.truncate(0)
        #file.close()
