students = {}

numStudents, rounds = [int(x) for x in input().split(' ')]

mostRecentThrow = {}

for studentToThrow, studentThrownTo in enumerate([int(x) for x in input().split(' ')]):
    if studentThrownTo in students:
        students[studentThrownTo].append(studentToThrow+1)
    else:
        students[studentThrownTo] = [studentToThrow+1]

    mostRecentThrow[studentToThrow+1] = str(studentThrownTo)




for _ in range(rounds-1):

    recents = {}
    for student in range(1, numStudents+1):
        
        if student in students and student not in recents: # if the student has something to do
            if students[student] != None: # if the student's list is not empty
                thrownTo = students[student][0] # the student that the snowball is being thrown at
                mostRecentThrow[student] = str(thrownTo)
                if thrownTo in students: # if the student is in students
                    students[thrownTo].append(student) # add the student that threw the snowball in his list
                    if len(students[thrownTo]) == 1:
                        recents[thrownTo] = 0
                else: # if hes not in the dictionary
                    students[thrownTo] = [student]  # make a new key of him with the value of the student that threw the snowball
                    recents[thrownTo] = 0 # make sure that in this round he doesn't throw
                students[student].pop(0) # delete the element in the person that threw the snowball's list


print(' '.join(mostRecentThrow.values()))