import sqlite3


class Student:
    def __init__(self, name, surname, student_id):
        self.name = name
        self.surname = surname
        self.student_id = student_id

    def display_info(self):
        print(f"Öğrenci Bilgileri: {self.name} {self.surname}, ID: {self.student_id}")

    
   
    
    @staticmethod
    def create_students_table(cursor):
        new_class=input('lütfen sınıf adı giriniz')
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {new_class} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                surname TEXT,
                student_id TEXT
            )
        ''')
        
    @staticmethod
    def input_student():
        name = input("Öğrenci ismini giriniz: ")
        surname = input("Öğrenci soyismini giriniz: ")
        student_id = input("Öğrenci numarasını giriniz: ")
        return {'name': name, 'surname': surname, 'student_id': student_id}
        
    @staticmethod
    def insert_student(cursor, student,grade):
        cursor.execute('''
            INSERT INTO {} (name, surname, student_id)
            VALUES (?, ?, ?)
        '''.format(grade),(student['name'], student['surname'], student['student_id']),)
    
        conn.commit()
    
    @staticmethod
    def delete_student(cursor,grade):

        all_students = Student.get_all_students(cursor,grade)
        print(f" \n {grade} tablosundaki tüm öğrenciler:")
        for student in all_students:
            print(f"ID: {student[0]}, Name: {student[1]}, Surname: {student[2]}, Student ID: {student[3]}")

        deleted =input('silmek istediğiniz öğrencinin ismini giriniz')
        cursor.execute(f'SELECT * FROM {grade} WHERE name = ?', (deleted,))
        matching_students = cursor.fetchall()
        
         

        if not matching_students:
            print(f"{deleted} isimli öğrenci kaydı bulunamadı ana menüye yonlendiriliyorsunuz")
        
        elif len(matching_students) ==1:
            cursor.execute(f'DELETE FROM {grade} WHERE name = ?', (deleted ,))
            print(f'{deleted} isimli öğrenci kaydı silinmiştir')
            conn.commit()
        else:
            print(f"Birden fazla {deleted} isimli öğrenci bulundu:")
            for student in matching_students:
                print(f"ID: {student[0]}, Name: {student[1]}, Surname: {student[2]}, Student ID: {student[3]}")

            selected_id = input("Silmek istediğiniz öğrencinin ID'sini giriniz: ")
            cursor.execute(f'DELETE FROM {grade} WHERE student_id = ?', (selected_id,))

            conn.commit()
            if cursor.rowcount > 0:
                print(f"ID'si {selected_id} olan öğrenci kaydı silinmiştir")
            else:
                print(f"ID'si {selected_id} olan öğrenci kaydı bulunamadı")


    @staticmethod
    def update_student_info(cursor,grade):
        all_students = Student.get_all_students(cursor,grade)
        print('öğrenciler: \n')

        for student in all_students:
            print(f" Name: {student[1]}, Surname: {student[2]}, Student ID: {student[3]}")

        updated = input('Kaydını güncellemek istediğiniz öğrenci adını giriniz: ')

        cursor.execute(f'SELECT * FROM {grade} WHERE name = ?', (updated,))
        student_data =cursor.fetchall()
        print(student_data)

        if not student_data:
            print(f"{updated} isimli öğrenci kaydı bulunamadı ana menüye yönlendiriliyorsunuz")

        elif len(student_data) ==1:
            updating_column = int(input(f''' {updated}, 'nin hangi verisini güncellemek istersiniz ?'
                            1. name
                            2. surname
                            3. id
                            '''))

            if updating_column == 1:

                new_name = input('Yeni ismi giriniz: ')
                cursor.execute(f"UPDATE {grade} SET name = ? WHERE name  = ?", (new_name, updated))
                print(f"{updated} isimli öğrenci adı güncellenmiştir yeni isim : {new_name}")
                conn.commit()

            elif updating_column == 2:

                new_surname = input('Yeni soyismi giriniz: ')
                cursor.execute(f"UPDATE {grade} SET surname = ? WHERE name  = ?", (new_surname, updated))
                print(f"{updated} isimli öğrenci soyadı güncellenmiştir yeni soyisim : {new_surname}")
                conn.commit()
            elif updating_column == 3:

                new_id = input('Yeni numara giriniz: ')
                cursor.execute(f"UPDATE {grade} SET student_id = ? WHERE name  = ?", (new_id, updated))
                print(f"{updated} isimli öğrencinin numarası güncellenmiştir, yeni numara : {new_id}")
                conn.commit()
            else:
                print('lütfen 3 secenekten birini seçiniz')
                print('\n')

                updating_column = int(input(f''' {selected_id}, 'nin hangi verisini güncellemek istersiniz ?'
                                1. name
                                2. surname
                                3. id
                                '''))

                if updating_column == 1:

                    new_name = input('Yeni ismi giriniz: ')
                    cursor.execute(f"UPDATE {grade} SET name = ? WHERE student_id  = ?", (new_name, updated))
                    print(f"{updated} numaralı öğrenci adı güncellenmiştir yeni isim : {new_name}")
                    conn.commit()

                elif updating_column == 2:

                    new_surname = input('Yeni soyismi giriniz: ')
                    cursor.execute(f"UPDATE {grade} SET surname = ? WHERE student_id  = ?", (new_surname, updated))
                    print(f"{updated} numaralı öğrenci soyadı güncellenmiştir yeni soyisim : {new_surname}")
                    conn.commit()
                elif updating_column == 3:

                    new_id = input('Yeni numara giriniz: ')
                    cursor.execute(f"UPDATE {grade} SET student_id = ? WHERE student_id  = ?", (new_id, updated))
                    print(f"{updated} isimli öğrencinin numarası güncellenmiştir, yeni numara : {new_id}")
                    conn.commit()
                
                else:
                    print('yanlıs tusladınız')

        else:

            print(f"Birden fazla {updated} isimli öğrenci bulundu:")
            for student in student_data:
                print(f" Name: {student[1]}, Surname: {student[2]}, Student ID: {student[3]}")

            selected_id = input("Güncellemek istediğiniz öğrencinin ID'sini giriniz: ")
                
            updating_column = int(input(f''' {selected_id}, 'nin hangi verisini güncellemek istersiniz ?'
                                1. name
                                2. surname
                                3. id
                                '''))

            if updating_column == 1:

                new_name = input('Yeni ismi giriniz: ')
                cursor.execute(f"UPDATE {grade} SET name = ? WHERE student_id  = ?", (new_name, selected_id))
                print(f"{updated} numaralı öğrenci adı güncellenmiştir yeni isim : {new_name}")
                conn.commit()

            elif updating_column == 2:

                new_surname = input('Yeni soyismi giriniz: ')
                cursor.execute(f"UPDATE {grade} SET surname = ? WHERE student_id  = ?", (new_surname, selected_id))
                print(f"{updated} numaralı öğrenci soyadı güncellenmiştir yeni soyisim : {new_surname}")
                conn.commit()

            elif updating_column == 3:

                new_id = input('Yeni numara giriniz: ')
                cursor.execute(f"UPDATE {grade} SET student_id = ? WHERE student_id  = ?", (new_id, selected_id))
                print(f"{updated} isimli öğrencinin numarası güncellenmiştir, yeni numara : {new_id}")
                conn.commit()
            else:
                print('lütfen 3 secenekten birini seçiniz')
                print('\n')

                updating_column = int(input(f''' {selected_id}, 'nin hangi verisini güncellemek istersiniz ?'
                                1. name
                                2. surname
                                3. id
                                '''))

                if updating_column == 1:

                    new_name = input('Yeni ismi giriniz: ')
                    cursor.execute(f"UPDATE {grade} SET name = ? WHERE student_id  = ?", (new_name, selected_id))
                    print(f"{updated} numaralı öğrenci adı güncellenmiştir yeni isim : {new_name}")
                    conn.commit()

                elif updating_column == 2:

                    new_surname = input('Yeni soyismi giriniz: ')
                    cursor.execute(f"UPDATE {grade} SET surname = ? WHERE student_id  = ?", (new_surname, selected_id))
                    print(f"{updated} numaralı öğrenci soyadı güncellenmiştir yeni soyisim : {new_surname}")
                    conn.commit()

                elif updating_column == 3:

                    new_id = input('Yeni numara giriniz: ')
                    cursor.execute(f"UPDATE {grade} SET student_id = ? WHERE student_id  = ?", (new_id, selected_id))
                    print(f"{updated} isimli öğrencinin numarası güncellenmiştir, yeni numara : {new_id}")
                    conn.commit()
                else:
                    print('yanlıs tusladınız')

            
    @staticmethod
    def get_all_students(cursor,grade):
        cursor.execute(f'SELECT * FROM {grade}')
        return cursor.fetchall()

    


conn = sqlite3.connect('students.db')
cursor = conn.cursor()


# main kod menusu 
start= True

while start == True:
    
    menu = int(input(''' Öğrenci kayıt uygulamamıza hoşgeldiniz, hangi işlemi yapmak istersiniz ? numara seçiniz:
        
            1. yeni sınıf oluşturma
            2. var olan sınıfta güncelleme ve görüntüleme
        '''))
        
    if  menu == 1:

        Student.create_students_table(cursor)
        print('yenisınıf açılmıştır veri tabanını kontrol edebilirsiniz')
    elif menu == 2:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        grade=input(f''' 
            hangi sınıf üzerinde işlem yapmak istersiniz ?
        {tables}
                
        ''')
        choice =int(input(f''' {grade} sınıfı üzerinde hangi işlemi yapmak istersiniz ?
            1.yeni öğrenci ekleme
            2. öğrenci silme
            3.öğrenci kaydı güncelleme
            4.Seçili öğrenciyi görüntüleme
            5.sınıftaki öğrencilerin tümünü görüntüleme
                          
                          '''))
        
        if choice == 1:
            
            number = int(input("Kaç öğrenci eklemek istersiniz: "))
            students = []

            for i in range(number):
                student = Student.input_student()
                students.append(student)
                Student.insert_student(cursor, student,grade)
                print('öğrenciler başarıyla eklendi tabloyu kontrol edebilirsiniz')

            all_students = Student.get_all_students(cursor,grade)
            print(f"\n {grade} tablosundaki tüm öğrenciler:")
            for student in all_students:
                print(f"ID: {student[0]}, Name: {student[1]}, Surname: {student[2]}, Student ID: {student[3]}")



        if choice == 2:
            Student.delete_student(cursor,grade)

        if choice == 3:
            Student.update_student_info(cursor,grade)

        if choice ==4:
            cursor.execute(f'SELECT * FROM {grade} ')
            all_names=cursor.fetchall()
            for i in all_names:
                print(i[1])
            
            select =input('görüntülemek istediğiniz öğrencinin adını giriniz')
            cursor.execute(f'SELECT * FROM {grade} WHERE name = ?', (select,))
            print('bu isimdeki öğrencilerimiz: ')
            print( cursor.fetchall())

        if choice ==5:

            all_students = Student.get_all_students(cursor,grade)
            print(f"\n {grade} tablosundaki tüm öğrenciler:")
            for student in all_students:
                print(f"ID: {student[0]}, Name: {student[1]}, Surname: {student[2]}, Student ID: {student[3]}")
            
        else:
            print('\n ... \n')
    else:
        print('lütfen 2 seçenekten birini seçiniz \n')



conn.commit()
conn.close()

conn.close()