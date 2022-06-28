from fileHandling import FileHandling
from job import Job
from jobHandling import JobHandling
from key import Key
import gitlab


class GitlabAccess:

    file_handling = FileHandling()
    job = Job()
    job_handling = JobHandling()
    key = Key()

    project_id_list = []

    def connect_to_gitlab(self, token):
        return(gitlab.Gitlab(url=self.key.url, private_token=token))

    def fetch_projects(self):
        self.gl = self.connect_to_gitlab(self.key.token)
        group = self.gl.groups.get(self.key.group)
        projects = group.projects.list(all=True, include_subgroups=True)
        for project in projects:
            self.project_id_list.append(project.id)

    def store_jobs(self):
        self.gl = self.connect_to_gitlab(self.key.token)
        if len(self.project_id_list) == 0:
            self.fetch_projects()
        self.file_handling.write_header_to_file("jobs")
        self.file_handling.close_file("jobs")
        added_id = 1
        for i in self.project_id_list:
            project = self.gl.projects.get(int(i))
            self.file_handling.open_file("jobs", "a")
            jobs = project.jobs.list(all=True)
            for job in jobs:
                if job.queued_duration == None:
                    queued_duration = None
                else:
                    queued_duration = round(job.queued_duration, 3)
                if job.duration == None:
                    duration = None
                else:
                    duration = round(job.duration, 3)

                self.file_handling.jobs_file.write(str(added_id) + "," + str(job.id) + "," + "\"" + str(job.name) + "\"" + "," + str(
                    job.project_id) + "," + str(queued_duration) + "," + str(duration) + "," + str(job.status) + "\n")
                added_id += 1
            print(f"Jobs from Project {i} fetched and stored")
        self.file_handling.close_file("jobs")
        print("Completed")

    @property
    def projects_return(self):
        return(self.project_id_list)
