import locale

locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')

# global variables, we will access throughout the program accountantSalaryVar = 100000
dataAnalystSalaryVar = 100000
contractorSalaryVar = 80000
employeeCap = 10
totalAllowedBudget = '$960,000'
actualBudget = '$1,500,000'

listOfEmployees = [
    'Ronald',
    'Bilal',
    'Tariq',
    'Cinderlla',
    'Luan',
    'Viet',
    'Sameer',
    'Reina',
    'Perla',
    'Ronalada',
]

noRelative = "No relative"
sibling = "Sibling"

dictOfEmployeeSiblings = {
    "Ronald": sibling,
    "Bilal": noRelative,
    "Tariq": noRelative,
    "Cinderlla": noRelative,
    "Luan": noRelative,
    "Viet": noRelative,
    "Sameer": noRelative,
    "Reina": noRelative,
    "Perla": noRelative,
    "Ronalada": sibling
}


def usd_to_number(money: str) -> float:
    return float(money.strip('$').replace(',', ''))


def number_to_usd(number: float) -> str:
    return locale.currency(number, grouping=True)


totalAllowedBudget = usd_to_number(totalAllowedBudget)
actualBudget = usd_to_number(actualBudget)

overBudget = abs(totalAllowedBudget - actualBudget)
print(f"We are over-budget {number_to_usd(overBudget)}")

print(
    f"\nEmployee Count: {len(listOfEmployees)}: "
    f"{'OVER EMPLOYEE CAP' if len(listOfEmployees) > employeeCap else f'{employeeCap} or less employees.'}"
)

sibling_list = {employee: status for (employee, status) in dictOfEmployeeSiblings.items() if status is sibling}
print("\nSiblings: \n" + '\n'.join(sibling_list))
