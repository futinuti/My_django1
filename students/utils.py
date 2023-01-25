
def format_list_students(students):
    string = '<table><thead><tr><th>First name</th><th>Last name</th><th>Email</th><th>Phone</th></tr><thead><tbody>'
    # string = '<br>'.join(str(student) for student in students)
    for st in students:
        string += f'<tr><td>{st.first_name}</td><td>{st.last_name}</td><td>{st.email}</td><td>{st.phone}</td></td>'
    string += '</tbody></table>'
    return string
