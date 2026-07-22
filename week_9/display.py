def display_ticket ():
    print('===IT Helpdask Ticket===')
    student_name = input("Enter Student Name: ")
    student_id = input("Enter Student ID: ")
    issue = input("Enter Issue: ")
    location = input("Enter Location: ")
    priority = input("Enter Priority (High/Medium/Low): ").lower()


    return student_name, student_id, issue, location, priority

