import random
f = open("words.txt","r")
data = f.readline()
words = data.split()
word = random.choice(words)
word = word.upper()
total_chances = 5
guessed_word = "-"*len(word)

while total_chances !=0 :
     print(guessed_word)
     letter = input("Guess a correct word:-").upper()
     if letter in word:
          for index in range (len(word)):
               if word[index]==letter:
                   guessed_word=guessed_word[:index]+letter+guessed_word[index+1:]
               if guessed_word == word :
                    print("Congratulession!!! YOU WON!!!")
                    print ("guessed_word",word) 
                    break
     else:
          total_chances -=1
          print("Incorrect guess, try again")
          print("the remaining chances :",total_chances)
else:
     print('''
              Game Over
              You Lose
     You lost all the chances ''')
     print("guessed_word",word)     







