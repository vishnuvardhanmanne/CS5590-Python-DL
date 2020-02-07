class Employee:
    emp_count=0
    sum=0
    def __init__(self, ename, sal, dept):
        self.ename=ename
        self.sal=sal
        Employee.emp_count+=1
        Employee.sum+=self.sal
        self.dept=dept
class Fulltime_Employee(Employee):
    def __init__(self,n,s,d):
        Employee.__init__(self,n,s,d)
employee1 = Employee("sam",2000,10)
employee2 = Employee("jam",4000,20)
employee3 = Employee("ram",6000,10)
employee4 = Employee("bam",8000,10)
employee5 = Employee("kam",10000,20)
employee6 = Employee("nam",12000,10)
print("total number of employees:",Fulltime_Employee.emp_count)
print("Average salary of the employees is", (Employee.sum/Employee.emp_count))