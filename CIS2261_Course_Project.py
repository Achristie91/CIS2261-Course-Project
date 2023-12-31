def calculate_tax_and_netpay(total_hours, hourly_rate, tax_rate):
    tax = float(total_hours) * float(hourly_rate) * (float(tax_rate) / 100)
    net_pay = float(total_hours) * float(hourly_rate) - tax
    return tax, net_pay

def get_name():
    name = input("Enter employee name (Enter 'End' to Total):   ")
    return name

def get_total_hours():
    total_hours = float(input("Enter total hours:  "))
    return total_hours

def get_hourly_rate():
    hourly_rate = float(input("Enter hourly rate:  "))
    return hourly_rate

def get_tax_rate():
    tax_rate = float(input("Enter tax rate (in %):  "))
    return tax_rate

def get_gross_pay(total_hours, hourly_rate):
    gross_pay = float(total_hours) * float(hourly_rate)
    return gross_pay

def display_employee_info(name, total_hours, hourly_rate, tax_rate, 
tax, gross_pay, net_pay):
    print("----------------------------------------------------")
    print("Employee name:", name)
    print("Total hours:", total_hours)
    print("Hourly rate:", hourly_rate)
    print("Tax rate:", tax_rate)
    print("Income tax:", tax)
    print("Gross pay:", gross_pay)
    print("Net pay:", net_pay)
    print("----------------------------------------------------")

def display_total_info(total_employees, total_hours, total_tax, 
total_gross_pay, total_net_pay):
    print("----------------------------------------------------")
    print("Total number of employees:", total_employees)
    print("Total hours:", total_hours)
    print("Total tax:", total_tax)
    print("Total gross pay:", total_gross_pay)
    print("Totatl net pay:", total_net_pay)
    print("----------------------------------------------------")

def main():
    total_employees = 0
    total_hours = 0
    total_tax = 0
    total_gross_pay = 0
    total_net_pay = 0

    while  True:
        name = get_name()
        if name == "End":
            break
        hours = get_total_hours()
        hourly_rate = get_hourly_rate()
        tax_rate = get_tax_rate()
        gross_pay = get_gross_pay(hours, hourly_rate)
        tax, net_pay = calculate_tax_and_netpay(hours, hourly_rate,
tax_rate)
        display_employee_info(name, hours, hourly_rate, tax_rate, tax, 
gross_pay, net_pay)

        total_employees += 1
        total_hours += hours
        total_tax += tax
        total_gross_pay += gross_pay
        total_net_pay += net_pay
        display_total_info(total_employees, total_hours, total_tax,
total_gross_pay, total_net_pay)

if __name__ == "__main__":
    main()