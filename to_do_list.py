

'''
Define a function called to_do that takes two inputs: action and activity

Actions: ‘remove’, ‘add’, ‘pop first’
Activity: the name of the activity

to_do(‘remove’, ‘eat pizza’) → removes the pizza from the list
to_do(‘add’, ‘eat pizza’) → should add pizza to the list
to_do(‘pop first’, None) → should pop the first element of the list

'''

# The main list that I want to make changes to
to_do_list = []

def to_do(action, activity):
    
    if action == 'add':
        # Which list function can I use to add an item to my list?
        # What if the user is adding something that's already in the list?
        # What function can I use to check if a value is already in the list?
        pass
        
    elif action == 'remove':
        # Which list function can I use to remove an item from my list?
        # What if the user is removing something that's not in the list?
        # What function can I use to check if a value is already in the list?
        pass
            
    elif action == 'pop first':
        # Which list function can I use to remove the first item of my list?
        # What if the list is empty?
        # How can I check if my list is empty or not?
        pass
        
    else:
        print('this request is not supported')


to_do('add', 'eat pizza') # will add 'eat pizza' to the list
to_do('add', 'wash my hair') # will add 'wash my hair' to the list
to_do('remove', 'wash my hair') # will remove 'wash my hair from the list
to_do('pop first', None) # will pop the first element, 'eat pizza' from list

# The to_do list will now be empty









to_do_list = []

def to_do(action, activity):
    if action == 'add':
        if activity in to_do_list:
            print('already in the list')
        else:
            to_do_list.append(activity)
        
    elif action == 'remove':
        if activity in to_do_list:
            to_do_list.remove(activity)
        else:
            print('this activity is not in the list')
            
    elif action == 'pop first':
        if len(to_do_list) != 0:
            to_do_list.pop(0)
        else:
            print('the to do list is empty')
    else:
        print('this request is not supported')
        
        
to_do('add', 'eat dinner')
print(to_do_list)

to_do('add', 'wash my hair')
print(to_do_list)

to_do('add', 'wash my hair')
print(to_do_list)

to_do('remove', 'wash my hair')
print(to_do_list)

to_do('pop first', None)
print(to_do_list)
        
    
    