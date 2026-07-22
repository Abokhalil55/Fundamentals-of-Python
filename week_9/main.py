from display import display_ticket
from ticket import ticket_recorder

def main ():
    student_name, student_id, issue, location, priority = display_ticket ()
    ticket_recorder(student_name, student_id, issue, location, priority)


if __name__ == "__main__":
    main()