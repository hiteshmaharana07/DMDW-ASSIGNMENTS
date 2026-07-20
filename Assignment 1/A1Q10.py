class Employee:
    def input(self):
        self.emp_id = int(input("Enter Employee ID: "))
        self.emp_name = input("Enter Employee Name: ")
        self.basic_pay = float(input("Enter Basic Pay: "))
    def calc(self):
        self.ta = self.basic_pay * 0.10
        self.da = self.basic_pay * 0.40
        self.gross_pay = self.basic_pay + self.ta + self.da
    def display(self):
        print("\nEmployee Details")
        print("Employee ID   :", self.emp_id)
        print("Employee Name :", self.emp_name)
        print("Basic Pay     :", self.basic_pay)
        print("TA            :", self.ta)
        print("DA            :", self.da)
        print("Gross Pay     :", self.gross_pay)
emp = Employee()
emp.input()
emp.calc()
emp.display()
