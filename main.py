# drill 2: working with lists
from pyscript import display, document

def get_name(e):
    document.getElementById('div1').innerHTML = ' '

    club_fmember = ['pocholo', 'aisha', 'joaquin']
    club_lmember = ['comanda', 'padua', 'villar']

    f_name = document.getElementById('fname').value.lower().strip()
    name_checker = f_name in club_fmember  # true (1) or false (0)

    l_name = document.getElementById('lname').value.lower().strip()
    name_checker = l_name in club_lmember  # true (1) or false (0)

    display_message = ('Sorry, your name is not in the list', f'Congratulations {f_name}! You are now part of the Math guild.')

    display(display_message[name_checker], target='div1') # displays the message