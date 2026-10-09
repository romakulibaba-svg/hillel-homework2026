from student import Student
from group import Group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)
print("-" * 30)

assert gr.find_student('Jobs') == st1, 'Помилкак порівняння екземплярів класу Student'
assert gr.find_student('Jobs2') is None, "Шуканого студента не повинно бути!"

gr.delete_student('Taylor')
print(gr)  #
print("-" * 30)
print("Усі тести успішно пройдено!")