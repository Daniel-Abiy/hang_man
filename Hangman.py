import random
words = ["knight","night","life","mother","father","coffee","parent","play",'try','help','luck','good','bad','nice']
random_index = random.randint(0,len(words) - 1)
word = words[random_index].upper()
amount = ["_"]
guess = amount * len(word)
seen = []
try1 = 1
while try1 < 6:
    if "".join(guess) == word:
        print("Congratulation you have found the word")
        break
    else:
        print(" ".join(guess))
        gi = input("Enter the Your alphabet: " )
        gi = gi.upper()
        j = 0
        while j < len(word):
            if  gi == word[j] and gi not in seen:
                guess[j] = word[j].upper()
                try1 -= 1
            j += 1
        seen.append(gi)
        try1 += 1
        
    if try1 == 6:
        print("Sorry you have finished all of your chances")
        print("The word was: ",word)
print(" ".join(guess))

