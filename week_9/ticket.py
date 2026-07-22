def ticket_recorder(student_name, student_id, issue, location, priority):
    try:
        print("\n===== HELPDESK TICKET =====")
        print(f"Student Name : {student_name}")
        print(f"Student ID : {student_id}")
        print(f"Issue : {issue}")
        print(f"Location : {location}")
        if priority == 'high':
            print('Technician: Ahmad')
        elif priority == 'medium':
            print('Technician: Siti')
        elif priority == 'low':
            print('Technician: Ali')
        else:
            print('Priority: Under evaluation')
        print('Status: Pending')
    except Exception as e:
        print(f"An error occurred: {e}")