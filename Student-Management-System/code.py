# --------------
#Step 1
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
print(class_1)
print(class_2)

new_class = class_1 + class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)


#Step 2
courses = {'Math':65,'English':70,'History':80,'French':70,'Science':60}
print(courses)
total = sum(courses.values())
print(total)
percentage = (total/500)*100
print(percentage)


#Step 3
mathematics = {'Geoffrey Hinton':78,'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshua Benjio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}
print(mathematics)

max_marks_scored = max(mathematics.values())
print(max_marks_scored)

#Find out the student with the highest marks in Mathematics and store it in a variable 'topper'.
topper = max(mathematics,key = mathematics.get)
print (topper)


#Step 4
#print(topper.split())

first_name = topper.split()[0]
print(first_name)

last_name = topper.split()[1]
print(last_name)

full_name = last_name + " " + first_name
print(full_name)

certificate_name = full_name.upper()
print(certificate_name)





