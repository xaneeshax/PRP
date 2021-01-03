
'''
1. Write a loop that creates a list with numbers from 1-50
'''
nums = []
for i in range(50):
    nums.append(i+1)
    
print(nums)

'''
2. Write a function called start_with_snow where given a list the function 
outputs how many of the words start with 'snow':


words = ['snowflake', 'stop', 'snowing', 'snoop', 'snow', 'season', 'snowman']

start_with_snow(words) = 4
'''

def start_with_snow(words):
    
    count = 0
    for word in words:
        if 'snow' == word[0:4]:
            count += 1
            
    return count
            

'''
3. Given the dictionary:
'''
    
office = {
    
    'Jim' : ['pranks', 'sales', 'basketball'],
    'Dwight' : ['beets', 'sales', 'bears', 'battlestar galactica'],
    'Michael' : ['basketball', 'sales', 'pranks'],
    'Pam' : ['pranks', 'beets', 'art'],
    'Angela': ['accounting', 'beets', 'cats']

}


'''
Do the following:
    
    1. Change Jim's interests to ['pranks', 'hanging out with friends']
    2. How many interests does Angela have?
    3. How many keys are in this dictionary? (No code needed)
    4. How many people have 'sales' as an interest (No code needed)
'''

office['Jim'] = ['pranks', 'hanging out with friends']

len(office['Angela'])













