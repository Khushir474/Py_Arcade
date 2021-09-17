class game:

    # initializing all required variables and attributes
    def __init__(self,board,res=0):
        self.res=res
        self.board=board
        for i in range(1,11):
            self.board[i]=' '
        # print ('res is',self.res) 
    
    # to print the boad
    # need to remove 'None' that is being printed
    def show(self):
        print()
        print(self.board[7]+'  | '+self.board[8]+' | '+self.board[9])
        print('---+---+---')
        print(self.board[4]+'  | '+self.board[5]+' | '+self.board[6])
        print('---+---+---')
        print(self.board[1]+'  | '+self.board[2]+' | '+self.board[3])
        print()
        # print ('res is',self.res) 

    # get input from user X
    # check to see if user X entered a viable block
    # if so, then modify board{}
    def checkX(self):
        for i in range(10):
            self.board[10]='X'
            num1=int(input('user X, enter your preferred block '))
            if self.board[num1]==' ':
                self.board[num1]='X'
                game.show(self)
                break
            else:
                print('block already filled. Enter again')
                continue
    
    # get inpu from user O
    # check to see if user O entered a viable block
    # if so, then modify board{}
    def checkO(self):
        for i in range(10):
            self.board[10]='O'
            num1=int(input('user O, enter your preferred block '))
            if self.board[num1]==' ':
                self.board[num1]='O'
                game.show(self)
                break
            else:
                print('block already filled. Enter again')
                continue    
   
    # determine the winner, set self.res = 1
    def winner(self):

        # print('checking winner')
        if self.board[1]==self.board[2]==self.board[3]!=' ':
            print('*********user',self.board[10],'won the game*********')
            self.res=1
        elif self.board[4]==self.board[5]==self.board[6]!=' ':
            print('*********user',self.board[10],'won the game*********')
            self.res=1
        elif self.board[7]==self.board[8]==self.board[9]!=' ':
            print('*********user',self.board[10],'won the game*********')
            self.res=1
        elif self.board[1]==self.board[4]==self.board[7]!=' ':
            print('*********user',self.board[10],'won the game*********')
            self.res=1
        elif self.board[2]==self.board[5]==self.board[8]!=' ':
            print('*********user',self.board[10],'won the game*********')
            self.res=1
        elif self.board[3]==self.board[6]==self.board[9]!=' ':
            print('*********user',self.board[10],'won the game*********')
            self.res=1
        elif self.board[1]==self.board[5]==self.board[9]!=' ':
            print('*********user',self.board[10],'won the game*********')
            self.res=1
        elif self.board[3]==self.board[5]==self.board[7]!=' ':
            print('*********user',self.board[10],'won the game*********')
            self.res=1
    
    # show the board through show()
    # ask for inputs through check()
    # check for winner through winner().res
    # ask to play again through playagain()
    def play(self):

        game.winner(self)
        game.show(self)        
        game.checkX(self)

        for z in range(2,6):
            game.winner(self)
            if self.res==1:
                game.playagain(self)
                exit(0)
            game.checkO(self)
            game.winner(self)
            if self.res==1:
                game.playagain(self)
                exit(0)
            game.checkX(self)
    
    # ask to play again
    # if yes then reset the board
    # call the play funtion
    def playagain(self):
        ans=input('Do you wish to play again? y/n ')
        if ans.lower()=='y':
            for i in range(1,11):
                self.board[i]=' '
            # self.board[10]=' '
            game.reset(self)
            game.play(self)

    # reset the dictionary to null values
    # print board{} in the form of a grid
    def reset(self):
        for i in range(1,11):
            self.board[i]=' '
        self.res=0
        print('\n\n')
        print('========================')
        print('========NEW GAME========')
        print('========================')
        # game.show(self)

if __name__=='__main__':
    gameboard={}
    obj=game(gameboard,0)
    obj.play()
    # print(obj.res)
print('Thanks for playing')
