games = int(input())
winner = list(input())
if winner.count("D") > winner.count("A"):
    print("Danik")
elif winner.count("D") < winner.count("A"):
    print("Anton")
else:
    print("Friendship")
