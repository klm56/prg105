# determine users credit score if good,bad,fair, or excellent

credit_score = int(input("What is your credit score?"))

if credit_score >= 720:
    print("Your credit score is excellent")
elif credit_score >= 690:
    print("Your credit score is good")
elif credit_score > 630:
    print("Your credit score is fair")
else:
    print("Your credit score is bad")
