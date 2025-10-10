
class EmployeeTreeNode:
    def __init__(self, data):
        self.data = data
        self.subordinates = []


    def dfs(self, name):
        # depth first search
        print("At node", self.data)
        # base case
        if name is self.data:
            print("FOUND")
            return self
        
        # if name is in Supervisors subordinates
        for sub in self.subordinates:
            found = sub.dfs(name)
            if found:
                return found
        print("Not found")    
        return -1  
    
    def add_employee_by_name(self, new_emp_name, supervisor_name):
        # got get the object of the supervisor
        supervisor = self.dfs(supervisor_name)
        # make a new object of child
        child = EmployeeTreeNode(new_emp_name)
        # add child as subordinate of supervisor 
        supervisor.subordinates.append(child)

# root = EmployeeTreeNode(1)
# two = EmployeeTreeNode(2)
# five = EmployeeTreeNode(5)
# root.subordinates.append(two)
# root.subordinates.append(five)
# three = EmployeeTreeNode(3)
# four = EmployeeTreeNode(4)
# two.subordinates.append(three)
# two.subordinates.append(four)
# six = EmployeeTreeNode(6)
# eight = EmployeeTreeNode(8)
# five.subordinates.append(six)
# five.subordinates.append(eight)
# seven = EmployeeTreeNode(7)
# six.subordinates.append(seven)

# root.add_employee_by_name(9, 2)