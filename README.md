<<<<<<< HEAD
=======
# secret-santa-project
A Secret Santa assignment system for company exam

>>>>>>> 3314eaa521394e836af6bf22baa99ccd2f69da5f
- Secret Santa Assignment System

A modular and extensible Secret Santa assignment system that helps organize gift exchanges while following specific rules and constraints.

-- Features

- Read employee information from CSV files
- Handle previous year's assignments to avoid repetition
- Generate random, valid assignments following rules
- Export assignments to CSV
- Comprehensive error handling
- Unit tested
-- Project Structure


secret_santa/
├── src/              # Source code
├── tests/            # Unit tests
├── data/             # Input/output CSV files
└── main.py          # Entry point

-- Installation

1. Install dependencies:
pip install -r requirements.txt

-- Usage

1. Prepare your input CSV files in the "data" directory:
   - "employees.csv": List of employees
   - "previous_assignments.csv": Last year's assignments

2. Run the program:
python main.py

3. Find the output in "data/new_assignments.csv"

-- Error Handling

The application handles various error scenarios:
- Invalid CSV format
- File I/O errors
- Invalid assignments
- Insufficient number of employees

-- Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
