
"""
Grades come in a string such as ‘ fFAb  c a a b BcCdAAa  bC d D ’

Each letter represents a letter grade that the student got in the class. 
Your job is to determine if the average score is higher than 3 (round to the hundredths place).
A = 4, B=3, C=2, D=1, F= 0

You have to return True if the student passes or False if the student did not achieve 
the minimum score of 3.

HINT: round(12.23423423, 2) → 12.23

Method -> 
1. Use string methods to figure how many of each letter there are
2. Find the total number of letters
3. the total score (using the scoring system above)
4. Find the average score using (Total score / Total number of letters)

"""

def passing_score(grades):
    
    # Using a string function creates a new string
    # You need to assign back to the original varibale if you want in to
    # store the new string value
    grades = grades.#some-string-function()
    
    a_count = # what function can be used to count occurences of a letter?
    b_count = #
    c_count = #
    d_count = #
    e_count = #
    
    total_grades = # number of letters in the string
    total_score = # find the score using the scale (A = 4, B = 3 ...)
    
    avg_score = round((total_score / total_grades), 2)
    
    if avg_score >= 3:
        return True
    else:
        return False
    
result = passing_score(' fFAb  c a a b BcCdAAa  bC d D ')
print(result)




