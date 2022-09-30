import re
import datetime


class Developer:
    """ Creating Class Developer """
    id_counter = 0

    def __init__(self, name="name", address="address", phone_number="+1000000000",
                 email="email@com", position=-1, rank="rank", salary=-1, projects=[]):
        try:
            self.id: int = self.id_counter
            self.id_counter += 1
            self.name: str = name
            self.address: str = address
            if re.match("^\\+?[1-9][0-9]{7,14}$", phone_number) is None:
                raise ValueError("Phone number is not valid!")
            self.phone_number: str = phone_number
            self.email: str = email
            self.position: int = position
            self.rank: str = rank
            self.salary: float = salary
            self.projects: [Project] = projects
        except Exception as e:
            raise ValueError("Developer instantiation error! " + str(e))

    def assigned_projects(self):
        """ Get all project to developer."""
        return self.projects


class Assignment:
    """Link class"""
    def __init__(self, project, description: str = "Description"):
        self.parent_project: Project = project
        self.received_tasks = {}
        self.is_done = False
        self.description = description
        self.status = "0%"

    def __str__(self):
        return f"Assignment from project '{self.parent_project.title}' is {'' if self.is_done else 'not'} done." \
               f"\nTask list:{str(self.received_tasks)} "

    def __update_status(self):
        if len(self.received_tasks) > 0:
            percentage = len(list(filter(lambda x: x["is_done"] is True, self.received_tasks.values()))) / len(self.received_tasks)
            self.status = str(percentage)+"%"

    def add_task(self, title: str = "task", is_done: bool = False, description: str = "Task Description", due_date: datetime = None):
        """Adds task to assignment"""
        try:
            if len(self.parent_project.task_list) <= len(self.received_tasks):
                raise ValueError("Assignment task list cannot be longer than project task list!")
            self.received_tasks.update({due_date: {"title": title, "is_done": is_done, "description": description}})
            self.__update_status()
        except Exception as e:
            raise ValueError("Task creation error! " + str(e))

    def get_tasks_to_datetime(self, date: datetime):
        # TODO: test and finish
        return str(list([(task_date, task) for task_date, task in self.received_tasks.items() if date > task_date]))


class Project:
    """Creating Project with tasks"""
    def __init__(self, title="Title", start_date=None, task_list=[], developers=[], limit=-1):
        try:
            self.title: str = title
            self.start_date: datetime = start_date
            self.task_list: [str] = task_list
            self.developers: [Developer] = developers
            self.limit: int = limit
        except Exception as e:
            raise ValueError("Project instantiation error! " + str(e))

    def assign_possibility(self, dev: Developer):
        """Checking if developer can be added to the project"""
        return not self.limit <= len(self.developers)

    def add_developer(self, dev: Developer):
        """Add developer to project"""
        try:
            if self.limit <= len(self.developers):
                raise ValueError("Project developer limit is exceeded!")
            if dev in self.developers:
                raise ValueError("Developer is already in the list!")
            self.developers.append(dev)
            dev.projects.append(self)
        except ValueError as e:
            raise ValueError("Failed to add developer! " + str(e))

    def remove_developer(self, dev: Developer):
        """Remove developer from project"""
        try:
            self.developers.remove(dev)
            dev.projects.remove(self)
        except ValueError:
            raise ValueError("Developer was not found in the project!")


class QAEngineer(Developer):
    """Developer with access to testing"""
    def __init__(self, name="name", address="address", phone_number="+10000000",
                 email="email@com", position=-1, rank="rank", salary=-1):
        Developer.__init__(self, name, address, phone_number, email, position, rank, salary)

    def test_feature(self, *feature):
        return str(*feature)


class ProjectManager(Developer):
    """Developer with access to testing"""
    def __init__(self, project: Project, name="name", address="address", phone_number="+10000000",
                 email="email@com", position=-1, rank="rank", salary=-1):
        Developer.__init__(self, name, address, phone_number, email, position, rank, salary)
        self.project = project

    def discuss_progress(self, dev: Developer):
        try:
            if dev not in self.project.developers:
                raise ValueError("Project manager has no access to developer!")
            print(f"Discussion with {dev.name} happened")
        except ValueError as e:
            raise ValueError(f"Discussion with {dev.name} failed! " + str(e))


if __name__ == '__main__':
    try:
        dev1 = Developer(name="Dev1")
        project1 = Project(limit=2, task_list=["task1", "task2"])
        project1.add_developer(dev1)
        assignment1 = Assignment(project1, "test assignment1")
        assignment1.add_task("Task1", due_date=datetime.datetime(2002, 2, 3))
        assignment1.add_task("Task2", due_date=datetime.datetime(2022, 2, 1))
        print(assignment1.get_tasks_to_datetime(datetime.datetime(2021, 3, 1)))
        qa = QAEngineer()
        print('\n' + qa.test_feature(assignment1))
        pm = ProjectManager(project1)
        pm.discuss_progress(dev1)
        dev2 = Developer(name="Dev2")
        pm.discuss_progress(dev2)
    except Exception as e:
        print(e)
