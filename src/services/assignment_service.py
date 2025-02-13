from typing import List, Set
import random
from ..models.employee import Employee, Assignment
from ..exceptions.custom_exceptions import AssignmentError

class AssignmentService:
    def __init__(self):
        self.previous_assignments: List[Assignment] = []

    def set_previous_assignments(self, assignments: List[Assignment]) -> None:
        """Set previous year's assignments"""
        self.previous_assignments = assignments

    def is_valid_assignment(self, employee: Employee, secret_child: Employee) -> bool:
        """Check if assignment is valid based on rules"""
        # Rule 1: Cannot be own secret child
        if employee.email_id == secret_child.email_id:
            return False

        # Rule 2: Cannot have same secret child as previous year
        for prev_assignment in self.previous_assignments:
            if (prev_assignment.employee.email_id == employee.email_id and 
                prev_assignment.secret_child.email_id == secret_child.email_id):
                return False

        return True

    def create_assignments(self, employees: List[Employee]) -> List[Assignment]:
        """Create new Secret Santa assignments"""
        if len(employees) < 2:
            raise AssignmentError("At least 2 employees are required for Secret Santa")

        assignments: List[Assignment] = []
        available_children = employees.copy()
        
        for employee in employees:
            valid_children = [
                child for child in available_children
                if self.is_valid_assignment(employee, child)
            ]

            if not valid_children:
                raise AssignmentError(f"Could not find valid assignment for {employee.name}")

            secret_child = random.choice(valid_children)
            assignments.append(Assignment(employee=employee, secret_child=secret_child))
            available_children.remove(secret_child)

        return assignments
