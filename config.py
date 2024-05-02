class Config:
    def updateEnrolment(self, email, enrolmentlist):
            students = read_from_file()
            new_enrolment = []
            for subject in enrolmentlist:
                new_enrolment.append({"name": subject.getName(), "ID": subject.getID(), "mark": subject.getMark(), "grade": subject.getGrade()})
            for student in students:
                if student['email'] == email:
                    student['enrolment'] = new_enrolment
                    break
            write_to_file(students)

    def updatePassword(self, email, password):
            students = read_from_file()
            for student in students:
                if student['email'] == email:
                    student['password'] = password
                    break
            write_to_file(students)

    def updateStudent(self, ID):
            students = read_from_file()
            students = [student for student in students if student['ID'] != ID]
            write_to_file(students)


def generateSubject():
    subjects = []
    names = ["Subject", "Subject", "Subject", "Subject", "Subject", "Subject", "Subject", "Subject"]
    subjects = []
    unique_ids = set()

    # Generate unique IDs
    while len(unique_ids) < len(names):
        unique_id = f"{random.randint(100, 999):03}"  # Generate and pad in one step
        unique_ids.add(unique_id)
    
    # Create Subject instances
    for name, unique_id in zip(names, unique_ids):
        subjects.append(Subject(name, unique_id))
    
    return subjects
subjects = generateSubject()
