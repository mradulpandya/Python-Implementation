from User import User

User_data = User()

file = open("C:\\Users\HP\Desktop\\read_write_file.txt", "a")
file.write(User_data.name)
file.write(" , ")
file.write(User_data.age)
file.write(" , ")
file.write(User_data.profession)
file.write('\n')
file.close()


