from pathlib import Path
from src.services.file_service import FileService
from src.services.assignment_service import AssignmentService
from src.exceptions.custom_exceptions import SecretSantaError

def main():
    try:
        # Initialize services
        file_service = FileService()
        assignment_service = AssignmentService()

        # Set up file paths
        data_dir = Path('data')
        employees_file = data_dir / 'employees.csv'
        previous_assignments_file = data_dir / 'previous_assignments.csv'
        output_file = data_dir / 'new_assignments.csv'

        # Read input data
        employees = file_service.read_employees(employees_file)
        previous_assignments = file_service.read_previous_assignments(previous_assignments_file)

        # Create new assignments
        assignment_service.set_previous_assignments(previous_assignments)
        new_assignments = assignment_service.create_assignments(employees)

        # Write output
        file_service.write_assignments(output_file, new_assignments)
        print(f"Successfully created new Secret Santa assignments in {output_file}")

    except SecretSantaError as e:
        print(f"Error: {str(e)}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())