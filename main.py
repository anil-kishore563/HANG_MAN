from replit import clear
import Hangman_art
import word_list
print(Hangman_art.logo)

ask=input(r'Want to start the game(y\n) :').lower()
while not ask=='y' and not ask =='n':
  print('What the heck you just typed,Its invalid.Type again')
  ask=input(r'Want to start the game(y\n) :').lower()
if ask=='y':
    print("Let's start the game without any late ")        
    import copy
    import random
    lives=6
    chosen_word = random.choice(word_list.word_list)
    letter_list=[]
    guessed_list=[]
    for i in chosen_word:
        letter_list.append(i)  

    end_of_game=False
    completed=False

    list=[]
    for i in range(len(chosen_word)):
      list.append('_')

    while end_of_game==False:
        guess=input('Enter a letter :')
        clear()

        guessed_list.append(guess)
        if guess in list:
            print('You already guessed this letter')

        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                list[i]=guess

        list_=copy.deepcopy(list)

        if guess not in list:
          lives-=1
          print(f'The letter you guessed "{guess}" is not the word')
        print(''.join(list))
        print(Hangman_art.stages[lives])

        while not completed:
            if lives==1:
                hint=input(r'Want a hint ? y\n :').lower()

                while not hint =='y' and not hint =='n':
                    print('What the heck you just typed,Its invalid.Type again') 
                    hint=input(r'Want a hint ? y\n :').lower() 

                if hint=='y': 
                    once_more=True
                    while  once_more==True:
                            arbitary_hint_index=random.randint(0,len(letter_list)-1)              
                            if list_[arbitary_hint_index]=='_':
                                list_[arbitary_hint_index]=letter_list[arbitary_hint_index]
                                once_more=False
                                completed=True
                            else:
                                arbitary_hint_index=random.randint(0,len(word_list.word_list)-1)        
                    print(''.join(list_))
                else:
                  completed=True
                  break    
            else:
                break    

        if '_' not in list or lives==0:
          end_of_game=True

    if '_' in list:
      print(f'The word is {chosen_word}')
      print(f"The series of letters you guessed are {','.join(guessed_list)} " )
      print('YOU LOST')
    else:
      print(f'Yes,the word is {chosen_word}')   
      print(f"The series of letters you guessed are {','.join(guessed_list)} " )
      print('YOU WIN')
     
else:
  clear()
  print('Feeling sad for leaving before you start the game')


  



