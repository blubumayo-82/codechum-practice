score1, penaly_minutes1, submissions1 = map(int, input("Enter Player 1 stats: ").split())
score2, penaly_minutes2, submissions2 = map(int, input("Enter Player 2 stats: ").split())

if score1 > score2:
    print("Player 1 wins")
elif score2 > score1:
    print("Player 2 wins")
elif penaly_minutes1 < penaly_minutes2:
    print("Player 1 wins")
elif penaly_minutes2 < penaly_minutes1:
    print("Player 2 wins")
elif submissions1 < submissions2:
    print("Player 1 wins")
elif submissions2 < submissions1:
    print("Player 2 wins")
else: 
    print("Exact Tie")
