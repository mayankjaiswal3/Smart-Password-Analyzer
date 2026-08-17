import string
import random

WEAK_PASSWORD_THRESHOLD = 4

def count_by_rule(password,rule):
    return sum(1 for i in password if rule(i))

def Password_analyzer(password):
    analysis ={
        "length":len(password),
        "upper_case":count_by_rule(password,str.isupper),
        "lower_case":count_by_rule(password,str.islower),
        "digits":count_by_rule(password,str.isdigit),
        "special":count_by_rule(password,lambda i : i in string.punctuation)
    }
    return analysis
    
def calculate_score(analysis):
    
    base_score=sum([
        analysis["length"]>= 8,
        analysis["upper_case"] >= 1,
        analysis["lower_case"] >= 1,
        analysis["digits"] >= 1,
        analysis["special"]>= 1
    ])

    bonus_score = sum([
        analysis["length"] >= 12,
        analysis["upper_case"] >= 2,
        analysis["lower_case"] >= 2,
        analysis["digits"] >= 2,
        analysis["special"] >= 2
    ])
    score=base_score+bonus_score
    return score

def security_level(score):
    strengths = [
        "Extremely Weak",
        "Very Weak",
        "Weak",
        "Poor",
        "Fair",
        "Average",
        "Moderate",
        "Good",
        "Strong",
        "Very Strong",
        "Excellent"
    ]
    return strengths[score] if 0 <= score <= 10 else "invalid score"
    
def gen_suggestion(score):
    if score <= WEAK_PASSWORD_THRESHOLD:
        alphalow=random.choices(string.ascii_lowercase,k=4)
        alphaup=random.choices(string.ascii_uppercase,k=3)
        num=random.choices(string.digits,k=3)
        sp_char=random.choices("!@#$%^&*?~",k=2)
        suggested_password=alphalow+alphaup+num+sp_char
        random.shuffle(suggested_password)
        return "".join(suggested_password)
    
if __name__=="__main__":
    password=input("enter your password:- ")
    main_analysis=Password_analyzer(password)
    score=calculate_score(main_analysis)
    level_of_security=security_level(score)
    suggestion=gen_suggestion(score)

    print("\n----- PASSWORD ANALYSIS -----")
    print(f"Length : {main_analysis['length']}")
    print(f"Uppercase : {main_analysis['upper_case']}")
    print(f"Lowercase : {main_analysis['lower_case']}")
    print(f"Digits : {main_analysis['digits']}")
    print(f"Special : {main_analysis['special']}")

    print(f"\n security level : {level_of_security}")
    print(f"\n security score : {score}")
    
if suggestion:
    print(f"\n suggested password : {suggestion}")


    
    






