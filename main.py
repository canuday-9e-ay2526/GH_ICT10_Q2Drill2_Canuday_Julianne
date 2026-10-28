#Math Club checker
from pyscript import display, document

def add_member(e):
    document.getElementById('result').innerHTML = ' '
    student_first = document.getElementById('firstname').value
    student_last = document.getElementById('lastname').value

    student_name = str(student_first) + " " + str(student_last) # Combine input values

    # All sets
    Teacher = {'Louise Ferma'}
    G10 = {'Aisha Padua', 'Julianne Canuday', 'Pocholo Commanda', 'Jesse Villante', 'Dwayne Chua', 'Rachmiel Lozada', 'Alonzo Paulino'}
    G11 = {'Clarisse Casal'}
    G12= {'Zoe Laquindanum',  'Zedric Ramirez', 'Megan Ty', 'Reina Fortaleza'}

    Math_Complete = G10 | G11 | G12 | Teacher # Union - Join sets
    Math_Complete.add(student_name) # Add input
   
    


    display(f'Here is a list of All the members: {Math_Complete}', target='result') # Displays all members

    display(f'There are {len(Math_Complete)} Members Total', target='result') # Displays Number of members