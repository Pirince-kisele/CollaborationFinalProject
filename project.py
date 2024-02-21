# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import datetime


class Employee:
    def __init__(self, name, hours_worked, rate, shift):
        self.name = name
        self.hours_worked = hours_worked
        self.rate = rate
        self.shift = shift


class Payroll:
    def __init__(self, employee):
        self.employee = employee

    def calculate_pay(self):
        if self.employee.hours_worked > 40:
            regular_hours = 40
            overtime_hours = self.employee.hours_worked - 40
        else:
            regular_hours = self.employee.hours_worked
            overtime_hours = 0

        regular_pay = regular_hours * self.employee.rate
        overtime_pay = overtime_hours * self.employee.rate * 1.5
        total_pay = regular_pay + overtime_pay

        return total_pay, overtime_pay, overtime_hours, regular_hours


class Check:
    def __init__(self, payroll, tax_rate):
        self.payroll = payroll
        self.tax_rate = tax_rate

    def print_check(self):
        total_pay, overtime_pay, overtime_hours, regular_hours = self.payroll.calculate_pay()
        taxes = total_pay * self.tax_rate
        net_pay = total_pay - taxes

        print(f"Employee Shift: {self.payroll.employee.shift}")
        print(f"Employee Name: {self.payroll.employee.name}")
        print(f"Hours Worked: {self.payroll.employee.hours_worked}")
        print(f"Hourly Rate: ${self.payroll.employee.rate}")
        print(f"Regular hours: {regular_hours} hours")
        print(f"Overtime hours: {overtime_hours} hours")
        print(f"Overtime Pay: ${overtime_pay}")
        print(f"Date: {datetime.date.today()}")
        print(f"Gross Pay: ${total_pay}")
        print(f"Taxes: ${taxes}")
        print(f"Net Pay: ${net_pay}")

# Example usage


def get_shift(number):
    if number == 1:
        return 'Day Shift'
    elif number == 2:
        return 'Night Sshift'
    else:
        return f"There is not {number} Shift in this company"


def main():
    name = input("Enter Employee Name: ")
    hours_work = int(input("Enter Hours Work: "))
    hourly_rate = int(input("Enter Employee Rate: "))
    tax_rate = 0.2
    number = int(input("Enter Employee Shift (1 or 2): "))

    employee = Employee(name, hours_work, hourly_rate, get_shift(number))
    payroll = Payroll(employee)
    check = Check(payroll, tax_rate)
    check.print_check()


main()
