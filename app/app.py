from customtkinter import *
import customtkinter
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


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('pay roll')
        # set the theme of the app
        # Themes: "blue" (standard), "green", "dark-blue"
        customtkinter.set_default_color_theme("green")
        # set the appearance mode
        customtkinter.set_appearance_mode("system")  # default
        self.geometry("800x400")
        # config grid layout on the window
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Frame number 1
        self.frame_one = CTkFrame(self, width=300)
        self.frame_one.grid_columnconfigure(0, weight=1)
        self.frame_one.grid(row=0, column=0, sticky=(NSEW), padx=10, pady=10)

        CTkLabel(self.frame_one, text="Employee Pay Stub", font=('Courier', 18, 'bold'), justify=CENTER).grid(row=0, column=0, sticky=(EW), columnspan=2, pady=15)


        CTkLabel(self.frame_one, text="Employee Name", font=('Courier', 18, 'bold'),
                 justify=CENTER).grid(row=1, column=0, sticky=("W"), padx=10, pady=10)
        self.name = CTkEntry(self.frame_one, width=200,
                             height=30, placeholder_text="Enter Employee Name:")
        self.name.grid(row=1, column=1, sticky="W", padx=10, pady=10)


        CTkLabel(self.frame_one, text="Hours Work", font=('Courier', 18, 'bold'),
                 justify=CENTER).grid(row=2, column=0, sticky=("W"), padx=10)
        self. hours_work = CTkEntry(
            self.frame_one, width=200, height=30, placeholder_text="Enter Hours Work")
        self. hours_work.grid(row=2, column=1, sticky="W", padx=10, pady=10)


        CTkLabel(self.frame_one, text="Employee Rate", font=('Courier', 18, 'bold'),
                 justify=CENTER).grid(row=3, column=0, sticky=("w"), padx=10)
        self.hourly_rate = CTkEntry(
            self.frame_one, width=200, height=30, placeholder_text="Enter Employee Rate:")
        self.hourly_rate.grid(row=3, column=1, sticky="W", padx=10, pady=10)


        CTkLabel(self.frame_one, text="Employee Shift", font=('Courier', 18, 'bold'),
                 justify=CENTER).grid(row=4, column=0, sticky=("w"), padx=10)
        self.number = CTkEntry(self.frame_one, width=200, height=30,
                               placeholder_text="Enter Employee Shift (1 or 2)")
        self.number.grid(row=4, column=1, sticky="WE", padx=10, pady=10)

        CTkButton(self.frame_one, text="Submit",command=self.main ).grid(row=8, column=0, sticky=SW, padx=10,pady=(60, 10))  
        CTkButton(self.frame_one, text="Quit", command= self.destroy, fg_color="red",font=("Arial", 14, 'bold')).grid(row=8, column=1, sticky=SE, padx=10,pady=(60,10))  


        

        # Frame number 2
        self.frame_two = CTkFrame(self, width=150)
        self.frame_two.grid_columnconfigure(0, weight=1)
        self.frame_two.grid(row=0, column=1, sticky=(NSEW), pady=10, padx=(0,10))

        def main(self):
            self.name = input("Enter Employee Name: ")
            hours_work = int(input("Enter Hours Work: "))
            hourly_rate = int(input("Enter Employee Rate: "))
            tax_rate = 0.2
            number = int(input("Enter Employee Shift (1 or 2): "))

            employee = Employee(name, hours_work, hourly_rate, get_shift(number))
            payroll = Payroll(employee)
            check = Check(payroll, tax_rate)
            check.print_check()


app = App()
app.mainloop()
