try:
    dict={'Alice':85,'James':34,'Harmana':74,'Karmel':92,'Clerk':65}
    s=str(input("Enter the student's name: "))
    print(dict[s])
except KeyError:
    print("Student not found.")
