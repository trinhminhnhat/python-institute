# 3.4.1.13 LAB: The basics of lists - the Beatles
# # step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
newMember1 = str(input('Add Stu Sutcliffe: '))
newMember2 = str(input('Add Pete Best: '))
for x in beatles:
    beatles.append(newMember1)
    beatles.append(newMember2)
    break
print("Step 3:", beatles)

# step 4
del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list length
print("The Fab", len(beatles))
