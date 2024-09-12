def game():
    import random
    score=random.randint(1,99)
    print(f"Your Score is: {score}")

    with open("score.txt") as f:
        highscore = f.read()
        if(highscore==""):
            highscore = 0
        
    if(score>int(highscore)):
        with open("score.txt","w") as f:  
            f.write(str(score))
        
    return score

game()





    
    
    



    