class BankAccount:
    ID = 1
    def __init__(self, name, initial_deposit):
        self.balance = initial_deposit
        self.name = name
    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return self

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            return 0
        else:
            self.balance -= withdraw_amount
            return withdraw_amount

    def get_balance(self):
        return self.balance

    def account_balance(self):
        return "Name: {0} Balance: {1}".format(self.name, self.balance)
    
    def get_name(self):
        name = new_clients
        return self.name
    


f = open("c:\\python\\unit.html", "w")
f.write("<!DOCTYPE html><html><body>")
f.write("<h1>Unit Testing</h1>")
f.write("<p id=’date’></p><script>document.getElementById(’date’).innerHTML=Date();</script>")

testID = 1
f.write("<h2> Test {0}: Beggining Accounts </h2>".format(testID))
new_clients = [["Kaiser", 0], ["Ursala", 50], ["Shilah", 25]]
for i in new_clients:
    f.write("<p> Name: {0} Starting Balance: {1} </p>".format(i[0],i[1]))

people = []

testID += 1
f.write("<h2> Test {0}: Creating Accounts </h2>".format(testID))
for i in new_clients:
    people.append(BankAccount(i[0], i[1]))

testID += 1
f.write("<h2> Test {0}: Getting Balances </h2>".format(testID))
for i in people:
    f.write("<p>{0}</p>".format(i.account_balance()))

testID += 1

f.write("<h2> Test {0}: Activity </h2>".format(testID))
f.write("<ol>")
f.write("<li> Kaiser withdraws $10 </li>")
people[0].deposit(10)

f.write("<li> Shilha withdraws $5 </li>")
people[2].withdraw(5)

f.write("<li> Shilah asks Ursala for $10 and deposits it </li>")
people[2].deposit(people[1].withdraw(20))

f.write("<li> Shilah writhdraws $2 </li>")
people[2].withdraw(2)

f.write("<li> Shilah asks Ursala for $10 and deposits it; then withdraws $12 </li>")
people[1].deposit(people[2].withdraw(10)).withdraw(12)

f.write("<li> Kaiser deposits $18 </li>")
people[0].deposit(18)

f.write("</ol>")

testID += 1
f.write("<h2> Test {0}: Closing Balances </h2>".format(testID))

errorcount = 0
for i in people:
    if not (i.get_balance() == 28):
        f.write("<p>Error in {0}’s balance. Current={1} Expected=28</p>".format(i.get_name(),i.get_balance()))
        errorcount += 1
    else:
        f.write("<p>{0}’s balance correct: {1}</p>".format(i.get_name(), i.get_balance()))
        
f.write("<p> Total Errors: {0}</p>".format(errorcount))
f.write("</body></html>")
f.close()