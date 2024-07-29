

bloodtype = input("What is your bloodtype? (A+, AB+, O+, B+, A-, AB-, O-, B-): ")

if bloodtype  == "A+":
    print("You you can donate to: A+, AB+ ")
    print("You can receive from: A+, A-, O+, O- ")

if bloodtype  == "AB+":
    print("You you can donate to: AB+ Only ")
    print("You can receive from: All blood types (A+, AB+, O+, B+, A-, AB-, O-, B-) ")

if bloodtype  == "O+":
    print("You you can donate to: O+, A+, B+, AB+ ")
    print("You can receive from: O+, O- ")

if bloodtype  == "B+":
    print("You you can donate to: B+, AB+ ")
    print("You can receive from: B+, B-, O+, O- ")

if bloodtype  == "A-":
    print("You you can donate to: A-, A+, AB-, AB+ ")
    print("You can receive from: A-, O- ")

if bloodtype  == "AB-":
    print("You you can donate to: AB-, AB+ ")
    print("You can receive from: AB-, A-, B-, O- ")

if bloodtype  == "O-":
    print("You you can donate to: All blood types (A+, AB+, O+, B+, A-, AB-, O-, B-) ")
    print("You can receive from: O- Only ")

if bloodtype  == "B-":
    print("You you can donate to: B-, B+, AB-, AB+ ")
    print("You can receive from: B-, O- ")