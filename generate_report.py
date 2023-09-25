#!/usr/bin/env python3

import csv

csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

# Reads employee data from a CSV file using a custom dialect 'empDialect' and returns it as a list of dictionaries
def read_employees(csv_file_location):
  with open(csv_file_location):
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
      employee_list.append(data)
  return employee_list
employee_list = read_employees('<csv_file_path>')
#Display for result check
#print(employee_list)

# Returns a dictionary with department names as keys and the count of employees in each department as values
def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data
dictionary = process_data(employee_list)
#Display for result check
#print(dictionary)

# Exports a report
def write_report(dictionary, report_file):
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k]+'\n'))
write_report(dictionary, '<path/report.txt>')
#Go to the report path and check the file
#cd '<path>'
#cat report.txt
