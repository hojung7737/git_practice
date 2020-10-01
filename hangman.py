import random


def position_finder():
    global chosen_word
    global word_length
    global guess
    global answer

    index = 0
    count = 0

    for i in (chosen_word):
        if (guess == i):
            index = count
            answer = answer[:(index)] + guess + answer[index + 1:]
        count += 1

    return answer


def Hangman():
    global chosen_word
    global word_length
    global guess
    global answer
    global final_answer
    global count2
    run = True

    count = 0
    count2 = 0
    while (run):
        guess = input("Enter your guess: ")
        if (chosen_word.find(guess) > -1):
            position_finder()
            print(answer)

            if (answer.isalpha()):
                run = False
                count = 6
        else:
            if (count == 0):
                print("""
                _____
                |    
                |  
                |
                |
                |
                |
              __|__
              """)
                count += 1
            elif (count == 1):
                print("""
                _____
                |    | 
                |    |
                |
                |
                |
                |
              __|__
              """)
                count += 1
            elif (count == 2):
                print("""
                _____
                |    | 
                |    |
                |    O
                |
                |
                |
              __|__
              """)
                count += 1
            elif (count == 3):
                print("""
                _____
                |    | 
                |    |
                |    O
                |   /|\
                |
                |
              __|__
              """)
                count += 1
            elif (count == 4):
                print("""
                _____
                |    | 
                |    |
                |    O
                |   /|\
                |   /
                |
              __|__
              """)
                count += 1
            elif (count == 5):
                print("""
                _____
                |    | 
                |    |
                |    O
                |   /|\
                |   /\
                |
              __|__
              """)

                run = False
                print("Wrong guess. You are hanged!!!")

    string = list(chosen_word)
    answer = list(answer)
    final_answer = list(final_answer)

    if (count == 6):
        print("congratulation")
    else:
        for i in range(len(string)):
            if (answer[i] == string[i]):
                final_answer[i] = answer[i]
                answer[i] = "_"

            else:
                answer[i] = string[i]
                count2 += 1

        for i in range(count2):
            final_answer.remove("_")

        print(count2)
        print(final_answer, end = ' ')

        for i in range(len(answer)):
            print(answer[i], end = '')




def main():
    global chosen_word
    global word_length
    global guess
    global answer
    global final_answer
    print("\n")
    print("Let's play Hangman!")

    words_to_guess = [
        "january", "border", "image", "film", "promise", "kids", "lungs",
        "doll", "rhyme", "damage"
    ]
    chosen_word = random.choice(words_to_guess)
    word_length = len(chosen_word)
    final_answer = "_" * word_length
    answer = "_" * word_length


    print(chosen_word)
    Hangman()


chosen_word = ""
word_length = 0
guess = ""
answer = ""
final_answer = ""
count2 = 0
main()

