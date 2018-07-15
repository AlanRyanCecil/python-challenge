import os
import csv
import re

import us_states as st

read_path = os.path.join('employee_data.csv')
write_path = ('updated_employee_data.csv')

with open(read_path, 'r') as data_in, \
        open(write_path, 'w') as data_out:
    reader = csv.reader(data_in, delimiter=',')
    writer = csv.writer(data_out, delimiter=',')

    new_header = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
    writer.writerow(new_header)

    next(reader)
    for row in reader:
        emp_id, emp_name, dob, ssn, state = row

        emp_name = re.split('\s', emp_name)
        first_name = emp_name[0]
        last_name = emp_name[1]

        dob = re.split('-', dob)
        dob.insert(2, dob.pop(0))
        dob = '/'.join(dob)

        ssn = re.sub('\d{3}-\d{2}', '***-**', ssn)

        state = st.abbrev[state]

        writer.writerow([
            emp_id,
            first_name,
            last_name,
            dob,
            ssn,
            state,
        ])
