# Employee Gross Wage Calculator

A Python application that calculates gross wages with overtime logic and validates user input for accurate payroll results. Built to practice clean input handling, business rules, and testable logic.

![Screenshot of the Gross Wage Calculator](screenshots/app-screenshot.png)

## Why This Project Exists

Payroll calculations look simple until you add real-world rules: regular hours vs. overtime, hourly rates, and the need to reject invalid input before it produces wrong pay. I built this project to practice translating payroll rules into clean, testable Python code.

## Features

- Calculates regular pay and overtime pay based on hours worked
- Validates user input (rejects negative hours, non-numeric values, and missing fields)
- Applies overtime rules (e.g., 1.5x for hours over 40)
- Displays a clear breakdown of regular pay, overtime pay, and total gross pay
- Handles edge cases such as zero hours and maximum hour limits

## Tech Stack

- **Language:** Python 3
- **Libraries:** Standard library only (or list any you used, e.g., `decimal` for currency)
- **Testing:** `unittest` or `pytest`

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/camilledana/employee-gross-wage-calculator.git
