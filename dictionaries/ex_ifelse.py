enter_score = int(input("Enter your score : "))
show_grade = ""

if enter_score > 79:
    show_grade = "A"
elif enter_score < 80 and enter_score > 74:
    show_grade = "B+"
elif enter_score < 75 and enter_score > 69:
    show_grade = "B"
elif enter_score < 70 and enter_score > 64:
    show_grade = "C+"
elif enter_score < 65 and enter_score > 59:
    show_grade = "C"
elif enter_score < 60 and enter_score > 54:
    show_grade = "D+"
elif enter_score < 55 and enter_score > 49:
    show_grade = "D"
else:
    show_grade = "F"

print("grade : " + show_grade)