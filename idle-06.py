fruit_type = input("enter the fruit type:").strip().title()
'''.strip().title() on input to take case-sensitive and trim spaces'''
if fruit_type == "orages":
    print('oranges are 50/- per kilo')
elif fruit_type =="apples":
    print('apples are 120/- per kilo')
elif fruit_type =="bananas":
    print('bananas are 30/- per kilo')
elif fruit_type =="Cherries":
    print('cherries are 600/- per kilo')
else:
    print(f"Sorry, we are out of {fruit_type}")
