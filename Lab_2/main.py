from typing import Dict, List, TYPE_CHECKING, Any
from datetime import datetime
from dataclasses import dataclass
from random import randint
from collections import defaultdict


@dataclass
class PersonalInfo:
    # Attributes:

    def __init__(self, id_: int, first_name: str, second_name: str, address: str, phone_number: str,
                 email: str, position: int, rank: str, salary: float):
        self.id_ = id_
        self.first_name = first_name
        self.second_name = second_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.rank = rank
        self.salary = salary

    # Get full name

    @property
    def full_name(self):
        return self.first_name + " " + self.second_name

    # Set Full Name

    @full_name.setter
    def full_name(self, fullname):
        try:
            buffer_full_name = fullname.split(" ")
            self.first_name = buffer_full_name[0]
            self.second_name = buffer_full_name[1]
        except NameError:
            print("Something going wrong🤔.\n It should look like this:")
            print(f"{self.first_name}  {self.second_name} ✅")


class Employee:

    # Attributes:

    def __init__(self, personal_info: PersonalInfo):
        self.personal_info = personal_info

    # 2 abstract method's

    def calculate_salary(self) -> None:  # Use isinstance
        if isinstance(self.personal_info.salary, (int, float)):
            print(f'Hi {self.personal_info.first_name}\n')
            print(f"Your salary for this month is:  {self.personal_info.salary}$")
            print(f"Your salary for this year will be:  {self.personal_info.salary * 12}$")
            print(f"Your salary for this year with bonus 15% =  {self.personal_info.salary * 12 * 1.5}$ \n")
        else:
            print("Something going wrong😨.Maybe Incorrect data??🤔")

    def ask_sick_leave(self, project_manager) -> bool:
        print(f'\nHey,{manager.full_name}. I feell so bad,maybe temperature.Can you give sick-leave?')
        random_int = randint(0, 10)
        if random_int >= 5:
            return f'Okay. You can be free. Get well😇'
        else:
            return 'Sorry i can not free you now🥲'


class Project:

    # Attributes:

    def __init__(self, task_list: list[int]):
        self.task_list = task_list

    # def get_specific_employees(self, employee_type) -> List[Employee]:
    #     pass


class ProjectManager(Employee):

    # Attributes:

    def __init__(self, employee_requests: Any):
        self.employee_requests = employee_requests

    def calculate_salary(self) -> None:
        if isinstance(self.personal_info.salary, (int, float)):
            print(f'Hi {self.personal_info.first_name}')
            print(f"Your salary for this month is:  {self.personal_info.salary}$")
            print(f"Your salary for this year is:  {self.personal_info.salary * 12}$")
            print(f"Your salary for this year with bonus 10% =  {self.personal_info.salary * 12 * 1.1}$")
        else:
            print("Something going wrong😨.Maybe Incorrect data??🤔")

    # def discuss_progress(self, engineer: Employee) -> None:
    # pass


class Developer(Employee):

    def calculate_salary(self) -> None:
        if isinstance(self.personal_info.salary, (int, float)):
            print(f'Hi {self.personal_info.first_name}\n')
            print(f"Your salary for this month is:  {self.personal_info.salary}$")
            print(f"Your salary for this year is:  {self.personal_info.salary * 12}$")
            print(f"Your salary for this year with bonus 10% =  {self.personal_info.salary * 12 * 1.1}$")
        else:
            print("Something going wrong😨.Maybe Incorrect data??🤔")

    def ask_sick_leave(self, project_manager) -> bool:
        random_int = randint(0, 10)
        if random_int >= 5:
            return 'Okay.you can be free. Get well😇'
        else:
            return 'Sorry i can not free you now🥲'


class AssignManagement:

    # Attributes:

    def __init__(self) -> None:
        self.project_employee = defaultdict(list)
        self.employee_project = defaultdict(list)

    def assign(self, employeeid_, project_title) -> None:
        self.project_employee[employeeid_].append(project_title)
        self.employee_project[project_title].append(employeeid_)

    def unassign(self, employeeid_, project_title) -> None:
        if project_title in self.project_employee and employeeid_ in self.employee_project:
            self.project_employee[employeeid_].remove(project_title)
            self.employee_project[project_title].remove(employeeid_)
        else:
            print("It is not possible to retrieve a connection that does not exist!")


class Task:

    # Attributes:

    def __init__(self, id_: int, title: str, deadline: datetime, items: List[str], status: List[str],
                 related_project: str):
        self.id_ = id_
        self.title = title
        self.deadline = deadline
        self.items = items
        self.status = status
        self.related_project = related_project

    def implement_item(self, item_name: str) -> str:
        self.items.append(item_name)
        return f"Added part with title {item_name}"

    def add_comment(self, comment: str) -> None:
        self.status = comment


class Assignment:

    # Attributes:

    def __init__(self, received_tasks: dict[Task]):
        self.received_tasks = received_tasks

    def get_tasks_to_date(self, date: datetime) -> List:  # Returns all tasks before date in arguments.
        return [value for key, value in dict.items() if key <= date]


class QualityAssurance(Employee):

    def calculate_salary(self) -> None:
        if isinstance(self.personal_info.salary, (int, float)):
            print(f"Your salary for this month is:  {self.personal_info.salary}$")
            print(f"Your salary for this year is:  {self.personal_info.salary * 12}$")
            print(f"Your salary for this year with bonus 10% is: {self.personal_info.salary * 12 * 1.1}$")
        else:
            print("Something going wrong😨.Maybe Incorrect data??🤔")

    def ask_sick_leave(self, project_manager) -> bool:
        random_int = randint(0, 10)
        if random_int >= 5:
            return 'BB'
        else:
            return 'U can not leave now'