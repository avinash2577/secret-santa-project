# src/services/file_service.py
import csv
from typing import List, Dict
from pathlib import Path
from ..models.employee import Employee, Assignment
from ..exceptions.custom_exceptions import FileError, ValidationError


class FileService:
    @staticmethod
    def read_csv(file_path: Path) -> List[Dict]:
        """Read data from CSV file"""
        try:
            with open(file_path, 'r', newline='') as file:
                return list(csv.DictReader(file))
        except Exception as e:
            raise FileError(f"Error reading file {file_path}: {str(e)}")

    @staticmethod
    def write_csv(file_path: Path, data: List[Dict], fieldnames: List[str]) -> None:
        """Write data to CSV file"""
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            raise FileError(f"Error writing to file {file_path}: {str(e)}")

    def read_employees(self, file_path: Path) -> List[Employee]:
        """Read and parse employees from CSV"""
        try:
            data = self.read_csv(file_path)
            return [
                Employee(
                    name=row['Employee_Name'],
                    email_id=row['Employee_EmailID']
                )
                for row in data
            ]
        except KeyError as e:
            raise ValidationError(f"Invalid CSV format: missing column {str(e)}")

    def read_previous_assignments(self, file_path: Path) -> List[Assignment]:
        """Read and parse previous assignments from CSV"""
        try:
            data = self.read_csv(file_path)
            return [
                Assignment(
                    employee=Employee(
                        name=row['Employee_Name'],
                        email_id=row['Employee_EmailID']
                    ),
                    secret_child=Employee(
                        name=row['Secret_Child_Name'],
                        email_id=row['Secret_Child_EmailID']
                    )
                )
                for row in data
            ]
        except KeyError as e:
            raise ValidationError(f"Invalid CSV format: missing column {str(e)}")

    def write_assignments(self, file_path: Path, assignments: List[Assignment]) -> None:
        """Write assignments to CSV"""
        data = [
            {
                'Employee_Name': assignment.employee.name,
                'Employee_EmailID': assignment.employee.email_id,
                'Secret_Child_Name': assignment.secret_child.name,
                'Secret_Child_EmailID': assignment.secret_child.email_id
            }
            for assignment in assignments
        ]
        fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
        self.write_csv(file_path, data, fieldnames)