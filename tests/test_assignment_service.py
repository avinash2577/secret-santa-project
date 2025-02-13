import pytest
from src.services.assignment_service import AssignmentService
from src.models.employee import Employee, Assignment
from src.exceptions.custom_exceptions import AssignmentError

class TestAssignmentService:
    @pytest.fixture
    def assignment_service(self):
        return AssignmentService()

    @pytest.fixture
    def sample_employees(self):
        return [
            Employee("John Doe", "john@acme.com"),
            Employee("Jane Smith", "jane@acme.com"),
            Employee("Bob Wilson", "bob@acme.com")
        ]

    def test_valid_assignment(self, assignment_service, sample_employees):
        assignments = assignment_service.create_assignments(sample_employees)
        assert len(assignments) == len(sample_employees)
        
        # Test no self-assignments
        for assignment in assignments:
            assert assignment.employee.email_id != assignment.secret_child.email_id

    def test_insufficient_employees(self, assignment_service):
        with pytest.raises(AssignmentError):
            assignment_service.create_assignments([Employee("John Doe", "john@acme.com")])
