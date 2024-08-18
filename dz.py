path = r"C:\Users\Admin\Desktop\dz.txt"

with open(path, "w") as file1:
    file1.write("name: Vlad\n")
    file1.write("surname: Babinsky\n")
    file1.write("age: 15\n")
    file1.write("Study in: It-Step\n")

with open(path, "r") as file1:
    printt = file1.read()
    print(printt)