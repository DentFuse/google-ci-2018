# My certificate: ude.my/UC-ZWA0GXRV

import operator
import random

def readStudentDetails():
    print("Please enter number of students: ")
    numberOfStudent = int(input());
    studentRecords = {}
    for student in range(0, numberOfStudent):
        print("Enter name of student")
        name = input()
        print("Enter marks")
        marks = int(input())
        studentRecords[name] = marks
    return studentRecords

def rankAndRewardStudents(studentRecords):
    reward = 3
    cashReward = (500, 300, 100)
    sorted_dict = sorted(studentRecords.items(), key = operator.itemgetter(1), reverse = True)
    while (reward != 0):
        reward = reward -1
        print("{} has scored {} marks and gets a {}$ cash reward".format(sorted_dict[reward][0], sorted_dict[reward][1], cashReward[reward]))
    return sorted_dict

def appreciateStudents(studentRecords):
    for student in studentRecords:
        if (studentRecords[student] >= 950):
            print("{} gets a special appreciation for scoring extermely well. He/She got a score of {} marks".format(student, studentRecords[student]))

def lottery(sorted_dict):
    winner = random.choice(sorted_dict)
    print("{} wins 50$ as a lucky reward!! Btw he scored {} marks...".format(winner[0], winner[1]))

students = readStudentDetails()
sorted_dict = rankAndRewardStudents(students)
appreciateStudents(students)
lottery(sorted_dict)