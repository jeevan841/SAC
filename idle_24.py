class_info = {
    "class_name": "CSE(AI)",
    "semester" : 3,
    "subject":"SAC-LAB"
}
students = [
    {"name": "reda", "roll_no":85},
    {"name": "grecia", "roll_no":90},
    {"name": "satish", "roll_no":128}
]

def display_class_info():
    print("Class Information:")
    for key, value in class_info.items():
        print(f"{key.capitalize()}:{value}")
def display_students():
    for s in students:
        print(f"roll no.: {s['roll_no']} - Name: {s['name']}")
