class Employee:
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}."

    def __init__(self, name, position, salary, children):
        self.name = name
        self.position = position
        self.salary = salary
        self.children = children

    def get_net_salary(self):
        tax = self.salary* 0.15 - self.children * 1500
        netSalary = self.salary - tax
        return f"Zaměstnanci bude na účet vyplaceno {netSalary} Kč."

employee1 = Employee("Tomáš Novák", "ekonom", 65000, 3)

print(employee1.get_net_salary())