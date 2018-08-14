def computer_chooses_move(n, m):
    if (n <= m):
        return n

    else:
        amount = n % (m + 1)

        if (amount > 0):
            return amount

    return m
        
############################################################

def user_chooses_move(n, m):
    move = 0

    while (move == 0):
        print(" ")
        move = int(input("How many pieces will you take? "))

        if (move > n or move < 1 or move > m):
            print(" ")
            print("Oops! Invalid play! Try again.")
            move = 0

    return move

############################################################

def match():
    print(" ")

    n = 1
    m = 2
    
    while (m > n):
        n = int(input("How many pieces? "))
        m = int(input("Piece limit per move? "))

        if (m > n):
            print(" ")
            print("Amount of pieces must be greater than the limit of pieces per move!")
            print(" ")

    pc_play = True

    if (n % (m + 1) == 0):
        pc_play = False
        print(" ")
        print("You start!")
    else:
        print(" ")
        print("Computer start!")

    while (n > 0):

        if (pc_play):
            move = computer_chooses_move(n, m)
            pc_play = False

            if (move == 1):
                print(" ")
                print("The computer took a piece.")

            else:
                print(" ")
                print("The computer took",move,"pieces.")
            
        else:
            move = user_chooses_move(n, m)
            pc_play = True

            if (move == 1):
                print(" ")
                print("You took a piece.")

            else:
                print(" ")
                print("You took",move,"pieces.")

        n = n - move

        if (n == 1):
            print(" ")
            print("Now there is only one piece remaining on the board.")

        elif(n > 1):
            print(" ")
            print("Now there are",n,"pieces on the board.")

    if (pc_play):
        print(" ")
        print("End of the game! You won!")
        return 1
    else:
        print(" ")
        print("End of the game! The computer won!")
        return 0

############################################################

def champ():
    user = 0
    pc = 0
    x = 1

    while (x <= 3):
        print(" ")
        print("**** Round",x,"****")
        x += 1
        winner = match()

        if (winner == 1):
            user += 1

        else:
            pc += 1

    print("**** End of the championship! ****")
    print(" ")
    print("Score: You",user,"X",pc,"Computer")

############################################################
    
game_type = 0
while (game_type == 0):
    print("Welcome to the NIM game! Choice:")
    print(" ")
    print("1 - to play an isolated match")
    print("2 - to play a championship")
    print(" ")
    game_type = int(input("Your choice: "))
    print(" ")

    if (game_type == 1):
        print("You have chosen isolated game!")
        match()

    elif (game_type == 2):
        print("You have chosen a championship!")
        champ()

    else:
        print("Invalid option!")
        print(" ")
        game_type = 0
    
