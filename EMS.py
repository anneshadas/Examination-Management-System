# EXAMINATION MANAGEMENT SYSTEM
def repeat():
    choice2 = input("\nGo to main menu (y/n): ")
    if choice2 == 'y':
        print("\nYou are now being directed to the main menu...")
        main_menu()
        choice1 = int(input("Enter your choice: "))
        homepage(choice1)
    elif choice2 == 'n':
        exit()
    else:
        print("SORRY THE WEBSITE IS UNABLE TO RESPOND. PLEASE ENTER A VALID OPTION!")

# HOME PAGE    
print("\n\t\t\t  C.V.RAMAN GLOBAL UNIVERSITY\n\t\t\tMahura,Janla,Bhubaneswar-752054\n")
print("We welcome you to the Homepage of Examination Cell of C.V.Raman Global University")
print("[NOTE: This page is meant only for B.Tech CSE students]")

def main_menu():
    print("\n1) Student Profile\n2) Rules and Regulations of Exam\n3) Exam Schedule\n4) Room Allotment\n5) Results\n")
main_menu()

choice1 = int(input("What do you want to check? : "))
def homepage(choice1):
    if choice1 == 1:  # Student Profile
        print("\n\n\t\t\t\t STUDENT PROFILE\n")
        print("Please provide your details...\n")
        name = input("Name: ")
        reg_no = int(input("Registration No.: "))
        roll_no = input("Roll No.: ")
        branch = input("Branch: ")
        year_of_study = int(input("Year of study (1 to 4): "))
        if year_of_study not in [1, 2, 3, 4]:
            print("INVALID YEAR!")
            exit()
        semester = int(input("Semester (1 to 8): "))
        if (year_of_study == 1 and semester not in [1, 2]) or \
           (year_of_study == 2 and semester not in [3, 4]) or \
           (year_of_study == 3 and semester not in [5, 6]) or \
           (year_of_study == 4 and semester not in [7, 8]):
            print("INVALID SEMESTER!")
            exit()
        email_id = input("Email ID: ")
        print("\nYou've registered in the Student Database of the college with the following details\n")
        print("Name: ", name.title(), "\nReg. No.: ", reg_no, "\nRoll No.: ", roll_no.upper(), "\nCourse: B.Tech", "\nBranch: ", branch.upper(), "\nYear: ", year_of_study, "\nSem: ", semester, "\nEmail ID: ", email_id)
        repeat()

    elif choice1 == 2:  # Rules and Regulations of Exam
        print("\n\n\t\t\t  RULES AND REGULATIONS OF EXAM\n")
        print("As a candidate, you are supposed to follow the given instructions properly in the exam hall\n")
        print("1) ID Card is mandatory for attending the exams\n2) Decorum of the exam hall should be maintained\n3) Use of mobile phone, tablet or any such gadget is strictly prohibited\n4) Students found cheating will be penalised and will not be allowed to give the exam of the respective subject(s)\n")
        print("Violation of any of the above mentioned rules will lead to adoption of serious action by the Examination Cell Authority")
        repeat()

    elif choice1 == 3:  # Exam Schedule
        print("\n\n\t\t\t\t   EXAM SCHEDULE\n")
        print("We bring it to your notice that the Mid-Sem and End-Sem Schedules of 1st to 4th year are out now!\nKindly enter your details to view the schedule...\n")
        year_of_study = int(input("Year of study (1 to 4): "))
        if year_of_study not in [1, 2, 3, 4]:
            print("NO RESULTS FOUND!")
            exit()
        semester = int(input("Semester (1 to 8): "))
        if (year_of_study == 1 and semester not in [1, 2]) or \
           (year_of_study == 2 and semester not in [3, 4]) or \
           (year_of_study == 3 and semester not in [5, 6]) or \
           (year_of_study == 4 and semester not in [7, 8]):
            print("NO RESULTS FOUND!")
            exit()

        mid_sem_date = ['23/09/24', '24/09/24', '25/09/24', '26/09/24', '27/09/24']
        end_sem_date = ['11/11/24', '13/11/24', '15/11/24', '18/11/24', '20/11/24']

        subjects = {
            1: ["Maths", "IEE/BEE", "IME/Physics", "Programming in Problem Solving", "NO EXAM"],
            2: ["Maths", "IEE/BEE", "IME/Physics", "Data Structure", "NO EXAM"],
            3: ["Maths", "Green Chemistry", "DAA", "Universal Human Values", "DCCN"],
            4: ["Database Engineering", "Green Chemistry", "Switching circuit/logic design", "OOP using Java", "Computer Organisation"],
            5: ["Theory of Computation", "Machine Learning", "Operational System", "CSN", "NO EXAM"],
            6: ["Enterprise Java", "IOT/Advanced Machine Learning", "Blockchain", "Open Elective(1)", "NO EXAM"],
            7: ["Computation Intelligence", "NO EXAM", "Open Elective(2)", "NO EXAM", "Open Elective(3)"],
            8: ["NO EXAM", "NO EXAM", "NO EXAM", "NO EXAM", "NO EXAM"]
        }

        print("Exam Type:\n1) Mid Sem\n2) End Sem")
        choice3 = int(input("Choose exam type: "))

        if choice3 == 1:
            print("\nMID SEMESTER SCHEDULE")
            print(mid_sem_date)
            print(subjects[semester])
            print("Exam Timing: 10:30 am to 11:30 am")
        elif choice3 == 2:
            print("\nEND SEMESTER SCHEDULE")
            print(end_sem_date)
            print(subjects[semester])
            print("Exam Timing: 10:30 am to 1:30 pm")

        repeat()
    elif choice1==4: #Room Allotment
        print("\n\n\t\t\t\t ROOM ALLOTMENT\n")
        print("Enter your details...\n")
        year_of_study=int(input("Year of study (1 to 4): "))
        if year_of_study not in [1,2,3,4]:
            print("NO RESULTS FOUND!")
            exit()
        semester=int(input("Semester (1 to 8): "))
        if (year_of_study==1 and semester not in [1,2]) or \
           (year_of_study==2 and semester not in [3,4]) or \
           (year_of_study==3 and semester not in [5,6]) or \
           (year_of_study==4 and semester not in [7,8]):
            print("NO RESULTS FOUND!")   
            exit()

        def assign_room(grp_no,sr_no):
            group_dict={1:{(1,21):'001',(22,42):'002',(43,63):'003',(64,84):'004',(85,90):'005'}, # Group 1
                        2:{(1,15):'005',(16,36):'006',(37,57):'007',(58,78):'008',(79,90):'009'}, # Group 2
                        3:{(1,9):'009',(10,30):101,(31,51):102,(52,72):103,(73,90):104},          # Group 3
                        4:{(1,3):104,(4,24):105,(25,45):106,(46,66):107,(67,87):108,(88,90):109}, # Group 4
                        5:{(1,18):109,(19,39):201,(40,60):202,(61,81):203,(82,90):204},           # Group 5
                        6:{(1,12):204,(13,33):205,(34,54):206,(55,75):207,(76,90):208},           # Group 6
                        7:{(1,6):208,(7,27):209,(28,48):301,(49,69):302,(70,90):303},             # Group 7
                        8:{(1,21):304,(22,42):305,(43,63):306,(64,84):307,(85,90):308},           # Group 8
                        9:{(1,15):308,(16,36):309,(37,57):401,(58,78):402,(79,90):403},           # Group 9
                       10:{(1,9):403,(10,30):404,(31,51):405,(52,72):406,(73,90):407}}            # Group 10
            
            group_rooms=group_dict.get(grp_no)
            if not group_rooms:
                return "INVALID!"
            
            for key in group_rooms:
                if key[0]<=sr_no<=key[1]:
                    return group_rooms[key]
            return "INVALID!"

        grp_no=int(input("Group No. (1 to 10): "))
        sr_no=int(input("Serial No. (1 to 90): "))
        room = assign_room(grp_no,sr_no)

        if year_of_study in [1,3]:
            print(f"Your Room No.: BS {room}")
        elif year_of_study in [2,4]:
            print(f"Your Room No.: CS {room}")
        repeat()
    elif choice1 == 5:  # Results
        results3()

    else:
        print("PLEASE ENTER A VALID NUMBER!")

def load_results():
    results_data = {}
    try:
        with open("results.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(';')
                reg_no = int(parts[0])
                name = parts[1]
                marks = {}
                for mark in parts[2:]:
                    subject, score = mark.split(':')
                    marks[subject.strip()] = int(score.strip())
                results_data[reg_no] = {"Name": name, "Marks": marks}
    except FileNotFoundError:
        # Default data in case file is not found
        results_data = {
            2301020545: {"Name": "Prabhat kumar", "Marks": {"DM-GT": 85, "DCCN": 91, "DAA": 93, "UHV": 96, "G-CHEM": 91}},
            2301020476: {"Name": "Ujjwal Rai", "Marks": {"DM-GT": 89, "DCCN": 88, "DAA": 80, "UHV": 85, "G-CHEM": 91}},
            2301020299: {"Name": "Swagata maji", "Marks": {"DM-GT": 92, "DCCN": 88, "DAA": 80, "UHV": 85, "G-CHEM": 91}},
            2301020711: {"Name": "Aditi kumari", "Marks": {"DM-GT": 82, "DCCN": 84, "DAA": 83, "UHV": 95, "G-CHEM": 91}},
            2301020224: {"Name": "Annesha das", "Marks": {"DM-GT": 88, "DCCN": 84, "DAA": 87, "UHV": 91, "G-CHEM": 92}},
            2301020728: {"Name": "Tapu mohanta", "Marks": {"DM-GT": 86, "DCCN": 88, "DAA": 80, "UHV": 85, "G-CHEM": 91}}
        }
    return results_data

def save_results(results_data):
    with open("results.txt", "w") as file:
        for reg_no, data in results_data.items():
            name = data["Name"]
            marks = '; '.join([f"{subject}: {score}" for subject, score in data["Marks"].items()])
            file.write(f"{reg_no}; {name}; {marks}\n")

def add_new_student(results_data, reg_no):
    name = input("Enter the student's name: ")
    marks = {}
    subjects = ["DM-GT", "DCCN", "DAA", "UHV", "G-CHEM"]
    
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter mark for {subject}: "))
                marks[subject] = mark
                break
            except ValueError:
                print("Invalid input! Please enter a number.")
    
    results_data[reg_no] = {"Name": name, "Marks": marks}
    save_results(results_data)
    print("\nNew student result added successfully!")

def show_result(reg_no, results_data):
    student_result = results_data.get(reg_no)
    if student_result:
        print("\nStudent Name:", student_result["Name"])
        print("Marks:")
        for subject, marks in student_result["Marks"].items():
            print(f"{subject}: {marks}")
    else:
        print("No results found for the entered registration number.")

def teacher_options(results_data):
    while True:
        option = input("\nChoose an option:\n1. Show result\n2. Add new result\n3. Update existing result\n4. Exit\nEnter your choice: ").strip()
        
        if option == "1":  # Show result
            reg_no_input = input("Enter Registration Number to view result: ")
            if reg_no_input.isdigit():
                show_result(int(reg_no_input), results_data)
            else:
                print("Invalid registration number.")
        
        elif option == "2":  # Add new result
            reg_no_input = input("Enter new Registration Number: ")
            if reg_no_input.isdigit():
                reg_no = int(reg_no_input)
                if reg_no not in results_data:
                    add_new_student(results_data, reg_no)
                else:
                    print("This registration number already exists.")
            else:
                print("Invalid registration number.")
        
        elif option == "3":  # Update result
            reg_no_input = input("Enter Registration Number to update result: ")
            if reg_no_input.isdigit():
                reg_no = int(reg_no_input)
                student_result = results_data.get(reg_no)
                if student_result:
                    for subject in student_result["Marks"].keys():
                        while True:
                            try:
                                new_mark = int(input(f"Enter new mark for {subject}: "))
                                student_result["Marks"][subject] = new_mark
                                break
                            except ValueError:
                                print("Invalid input! Please enter a number.")
                    
                    results_data[reg_no] = student_result
                    save_results(results_data)
                    print("\nMarks updated successfully!")
                else:
                    print("No result found for this registration number.")
            else:
                print("Invalid registration number.")
        
        elif option == "4":  # Exit
            break
        else:
            print("Invalid choice. Please select a valid option.")

def results3():
    print("\n\n\t\t\t\t RESULTS\n")
    role = input("Are you a student or a teacher? (student/teacher): ").strip().lower()

    results_data = load_results()

    if role == "student":
        while True:
            reg_no_input = input("Enter your Registration Number: ")
            if reg_no_input.isdigit():
                show_result(int(reg_no_input), results_data)
            else:
                print("Invalid registration number.")

            # Ask if they want to check another result
            another = input("\nDo you want to see another result or exit? (another/exit): ").strip().lower()
            if another == "exit":
                print("Exiting the student section. Goodbye!")
                break
            elif another != "another":
                print("Invalid choice. Exiting the student section.")
                break

    elif role == "teacher":
        teacher_options(results_data)
    else:
        print("Invalid role. Please start the program again.")

homepage(choice1)