#1

class Student:
    def __init__(self, name, surname, student_id, course, faculty, speciality, is_mestnyi=False, subjects=[], semester=1):
        self.fullname = name + ' ' + surname
        self.id = student_id
        self.s_course = course
        self.s_faculty = faculty
        self.speciality = speciality
        self.is_mestnyi = is_mestnyi
        self.subjects = subjects
        self.semester = semester

    def all_info(self):
        print("Досье:", self.fullname)
        print('ID: ',self.id, '| Курс: ',self.s_course)
        print('Факультет: ',  self.s_faculty, '| Специальность: ', self.speciality)
        print("Местный: ", self.is_mestnyi)
        print("Предметы: ", self.subjects)
        print("Семестр: ", self.semester)

    def get_full_name(self):
        print(self.fullname)

    def add_subject(self, subject):
        add = self.subjects.append(subject)
        return add

    def semester_change(self):
        change = self.semester + 1
        changeSub = self.subjects.clear()
        return [change, changeSub]

    
class Faculty:
    def __init__(self, name, dean, students=[]):
        self.faculty_name = name
        self.dean = dean
        self.students = students
    

    def add_student(self, student):

        student = self.students.append(Student)
        return student
    

    
    



while True:

    print('Введите имя, фамилию и ID студента (ID должно содержать тоько цифры): ')
    s1 = Student(input(), input(), int(input()), 1, 'Военный', 'Разведка', True, ['Georaphy'], 2)
    print('Введите имя, фамилию и ID студента (ID должно содержать тоько цифры): ')
    s2 = Student(input(), input(), int(input()), 1, 'Военный', 'Разведка', True, ['Georaphy'], 2)
    print('Введите имя, фамилию и ID студента (ID должно содержать тоько цифры): ')
    s3 = Student(input(), input(), int(input()), 1, 'IT', 'SE', True, ['Georaphy'], 2)
    print('Введите имя, фамилию и ID студента (ID должно содержать тоько цифры): ')
    s4 = Student(input(), input(), int(input()), 1, 'IT', 'SE', True, ['Georaphy'], 2)
    print('Введите имя, фамилию и ID студента (ID должно содержать тоько цифры): ')
    s5 = Student(input(), input(), int(input()), 1, 'IT', 'SE', True, ['Georaphy'], 2)
    

    print('')
    s1.all_info()
    print('')
    s2.all_info()
    print('')
    s3.all_info()
    print('')
    s4.all_info()
    print('')
    s5.all_info()

    print('Чтобы изменить информацию о студенте, нажмите: \n1 - Посмотреть полное имя; 2 - добавить предметы; 3 - удалить предметы')
    a = [int(x) for x in input().split()]

    for i in range(len(a)):
        if a[i] == 1:
            s1.get_full_name()
            s2.get_full_name() 
            s3.get_full_name() 
            s4.get_full_name() 
            s5.get_full_name()      
        elif a[i] == 2:
            s1.add_subject(['Math', 'PI'])
            s1.all_info()
            s2.add_subject(['Math', 'PI'])
            s2.all_info()
            s3.add_subject(['Math', 'PI'])
            s3.all_info()
            s4.add_subject(['Math', 'PI'])
            s4.all_info()
            s5.add_subject(['Math', 'PI'])
            s5.all_info()
            print('_________________________')
        elif a[i] == 3:
            s1.semester_change()
            s1.all_info()
            s2.semester_change()
            s2.all_info()
            s3.semester_change()
            s3.all_info()
            s4.semester_change()
            s4.all_info()
            s5.semester_change()
            s5.all_info()
            print('_________________________')
    else:
        f = Faculty('Военный', 'N', [])
        print(f'Факультет: {f.faculty_name} | ', f'Декан: {f.dean}\n')
        print('Имена студентов:')
        f.add_student([s1.get_full_name(), s2.get_full_name()])
        print('')
        f1 = Faculty('IT', 'X', [])
        print(f'Факультет: {f1.faculty_name} | ', f'Декан: {f1.dean}\n')
        print('Имена студентов:')
        f.add_student([s3.get_full_name(), s4.get_full_name(), s5.get_full_name()])

    break

    



    

    




   

    
   


  



































#s1 = Student('Исаев', 'Максим', 13246500, 1, 'Военный', 'Разведка', True, [], 2)
#s1.all_info()
#s1.get_full_name()
#s1.add_subject(['Math', 'PI'])
#s1.semester_change()
#s1.all_info()


#run = True
#while run:
#    a = input()
#    c = 10
#    if a == '1':
#        s1.all_info()
#    elif a == '2':
#        s1.get_full_name()
#    elif a == '3':
#        s1.add_subject(['Math', 'PI'])
#    elif a == '4':
#        s1.semester_change()
#    else:
#        print('Доступ заблокирован!!!') 
#        break