import pytest
from pathlib import Path
from src.services.file_service import FileService
from src.models.employee import Employee, Assignment
from src.exceptions.custom_exceptions import FileError, ValidationError

class TestFileService:
    @pytest.fixture
    def file_service(self):
        return FileService()

    @pytest.fixture
    def sample_employees_csv(self, tmp_path):
        content = "Employee_Name,Employee_EmailID\nJohn Doe,john@acme.com\nJane Smith,jane@acme.com"
        file_path = tmp_path / "employees.csv"
        file_path.write_text(content)
        return file_path

    def test_read_employees(self, file_service, sample_employees_csv):
        employees = file_service.read_employees(sample_employees_csv)
        assert len(employees) == 2
        assert employees[0].name == "John Doe"
        assert employees[0].email_id == "john@acme.com"

    def test_read_invalid_csv(self, file_service, tmp_path):
        invalid_file = tmp_path / "invalid.csv"
        invalid_file.write_text("Invalid,CSV\nData")
        with pytest.raises(ValidationError):
            file_service.read_employees(invalid_file)