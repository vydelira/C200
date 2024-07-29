#ballon return true
#color return false
#red return false
#green return true
def passThroughDoor(string):
    for i in range(0, len(string)-1):
        currentchar = string[i]
        if string[i] == string[i +1]:
            return True
    return False
print(passThroughDoor("blue"))
print(passThroughDoor("yellow"))
 