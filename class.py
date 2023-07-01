# name = "tal"

# with open(r"28.6_class/files.csv", 'a') as f:
#     for i in range(1,101):    
#         f.writelines(str(f"{i}\n"))

# nums = [1,2,3,4,5]
# nums_string = []

# for num in nums:
#         nums_string.append(str(num)+'\n')
# with open(r"28.6_class/files.csv", 'a') as f:
#         f.writelines(nums_string)


students ="""
Name            Grade
---------------------
Tal             90
Eli             100
"""

# כותב את הנתונים לתוך הקובץ
with open(r"28.6_class/files.csv", 'w') as f:
    f.write(students)


# קורא את הנתונים מתוך הקובץ
def load_data():
    with open(r"28.6_class/files.csv", 'r') as f:
        students=f.read()
    return students


def string_to_table():
    string = load_data()
    table = []
    rows= string.strip('\n').split('\n')[2:]
    for row in rows:
        name,grade = row.split()
        table.append({"name":name,"grade":grade})
    return table

# print(string_to_table())

# טוענים את הקובץ ובפונקציה מחפשים את הערך שאנחנו רוצים load data על ידי הפונקציה של  
def search(keyword:str=""):
    students=string_to_table()
    for student in students:
        if student["name"] == keyword:
            return student
    return "not found"
keyword = input("enter text to search:")    

print(search(keyword))
print(string_to_table())
print(load_data())


