from dataclasses import dataclass
from typing import Optional

@dataclass
class Employee:
    name: str
    email_id: str

@dataclass
class Assignment:
    employee: Employee
    secret_child: Employee