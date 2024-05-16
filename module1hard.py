grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
students.sort()
elements_sum = list(map(sum, grades))
elements_quantity = list(map(len, grades))
average = list(float(a)/float(b) for a, b in zip(elements_sum, elements_quantity))
rating = dict(zip(students, average))
print(rating)
