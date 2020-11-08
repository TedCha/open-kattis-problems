# https://open.kattis.com/problems/opensource

projectByStudents = {}
studentSet = set()

while True:
    line = input()

    if line == "1":
        removeSet = set()

        for student in studentSet:
            count = 0
            for project in projectByStudents:
                if student in projectByStudents[project]:
                    count += 1
            if count > 1:
                removeSet.add(student)

        for project in projectByStudents:
            projectByStudents[project] = len({x for x in projectByStudents[project] if x not in removeSet})
        
        for w in sorted(projectByStudents.items(), key=lambda x: (-x[1], x[0])):
            print(f"{w[0]} {w[1]}")

        projectByStudents = {}
        continue
    
    if line == "0":
        break

    if line.isupper() == True:
        project = line
        projectByStudents[project] = set()
    
    else:
        student = line
        projectByStudents[project].add(student)
        studentSet.add(student)
