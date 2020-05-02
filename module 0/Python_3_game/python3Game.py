#global variables, we will access throughout the program
accountantSalaryVar = 100000 
dataAnalystSalaryVar = 100000 
contractorSalaryVar = 80000 
employeeCap = 10 
totalAllowedBudget = '$960,000'
actualBudget = '$1,500,000'

#more global variables, we will access throughout the program
listOfEmployees = ['Ronald', 'Bilal', 'Tariq', 'Cinderlla', 'Luan', 'Viet', 'Sameer', 'Reina', 'Perla', 'Ronalada']

dictOfEmployeeSiblings =  {
      "Ronald": "Sibling",
      "Bilal": "No relative",
      "Tariq": "No relative",
      "Cinderlla": "No relative",
      "Luan": "No relative",
      "Viet": "No relative",
      "Sameer": "No relative",
      "Reina": "No relative",
      "Perla": "No relative",
      "Ronalada": "Sibling" }

#lets' test to see if the list we were given passes the number of employees check
totalAllowedBudget = totalAllowedBudget.strip('$')
totalAllowedBudget = totalAllowedBudget.replace(',','')
actualBudget = actualBudget.strip('$')
actualBudget = actualBudget.replace(',','')

overBudget = abs(int(totalAllowedBudget) - int(actualBudget))
print("We are overBudget " + str(overBudget))

def checkEmployeeCap(numberOfEmployeesCap, listOfEmployees):
    #local variable, accessible only within a function
    numberOfExistingEmployee = len(listOfEmployees)
        
    if (numberOfEmployeesCap < numberOfExistingEmployee):
        print("We have more than the employee cap...")
    else:
        print("We have 10 or less employees...")

#lets' test to see if the list we were given passes the number of employees check
checkEmployeeCap(employeeCap, listOfEmployees)        

def checkEmployeeSiblings(dictOfEmployeeSiblings):
  for name, relation in dictOfEmployeeSiblings.items():
    if relation == "Sibling":
      print(name)

#lets' test to see if the list we were given passes the number of employees check
checkEmployeeSiblings(dictOfEmployeeSiblings) 

print("Dear Management, Shareholders and the Law\n\
    We have found $540,000 overspend in budget with 2 relatives, Ronald and Ronalada. Good news is we now have some functions to run through our company to ensure we don't have this issue again.\
      Sincerely,\
        Trying to catch corruption...\
  ")