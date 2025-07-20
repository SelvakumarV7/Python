# You are given a JSON string representing information about students. Each student object has the following attributes: "name", "age", and "grade".
# Write a function to parse the JSON string and print the name, age, and grade of each student.

import json

json_str = '{"students": [{"name": "John", "age": 20, "grade": "A"},{"name": "Alice", "age": 18, "grade": "B"}]}'
def student_info(json_str):
    data = json.loads(json_str)
    students = data.get('students',[])
    for student in students:
        name = student.get('name','')
        age = student.get('age','')
        grade = student.get('grade','')
        print(f'name: {name}')
        print(f'age: {age}')
        print(f'grade:{grade}')
student_info(json_str)