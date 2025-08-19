def calculate_grades(raw_grades : str):
    grade_sheet = {
        'A':4,
        'B+':3.5,
        'B':3,
        'C+':2.5,
        'C':2,
        'D':1,
        'I':0,
        'F':0
    }

    non_qpi_units = {
        'PHYED',
        'NSTP',
        'INTACT',
        'Subject'
    }

    weighted_grade_total = 0
    current_units = 0

    raw_grades = raw_grades.split('\n')
    for i in raw_grades:
        curr_row = i.split('\t')
        if curr_row != ['']:
            if curr_row[3].split()[0] not in non_qpi_units:
                curr_units = curr_row[5]
                curr_grade = curr_row[6].strip()
                current_units += int(curr_units)
                weighted_grade_total += int(curr_units) * grade_sheet[curr_grade]

    final_grade = round(weighted_grade_total / current_units, 2)
    return final_grade