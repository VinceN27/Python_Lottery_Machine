# Imports:
import random # For quick pick numbers and drawn numbers.
import time # For a visual delay for code in the console. -- Vince
import os # For interacting with python's operating system/console. -- Sky

# Variables:
prize = 1000000 # Default prize money.
replay = 'y' # To control gameplay.

# Lists:
userNumbers = [] # Needed to collect the user's numbers.
powerBall = [] # Needed to collect the powerball or mega ball if necessary.

###### Main Menu: ######
# Credit: Vince/Sky

# The message below will only appear during the initial run of the code:
print("Thanks for checking out our lottery machine. We hope that you will have fun testing your luck at no cost!\n")

def main(): # This function, main(), is used for the entire game.
  try: # A try/except block is wrapped around the entire code to handle value error exceptions in the menus.
    userNumbers.clear()
    powerBall.clear()
# ^ Upon each game run, whether by manually clicking the run button or by replay, the lists userNumbers and powerBall are cleared out. This is placed in the beginning of the code.

# The main menu appears below, and gives the user options. The user must enter a number between 1 and 6, which corresponds to the five games and the help menu. The input the user provides must be an integer, and is assigned to a variable called 'selection.'
    print("=== Main Menu: ===\n")
    print("Here is a list of available games to play:\n"
            "1: Numbers\n"
            "2: Win4\n"
            "3: Take 5\n"
            "4: Powerball\n"
            "5: Mega Millions\n")

    selection = int(input("Please select a game by typing the corresponding number. For more information on how each game works, type in '6':\n"))

# Input validation below. If a number less than 1 or greater than 6 is selected (0, 7, 8, etc), the program will not continue until a valid input is received. If the user inputs any other character than a number, the program will end with an error.
      
    while selection < 1 or selection > 6:
        print("The input you provided was invalid. Please try again.\n")
        selection = int(input("Please select a game by typing the corresponding number. For more information on how each game works, type in '6':\n"))

###### Game Selection and Inputs: ######
# Credit: Vince/Jeiby

    if selection == 1 or selection == 2: # If the game selection is 1 or 2, the user will play Numbers or Win4.
      os.system("clear") # (Sky) This command is used to clear the console output, so it looks more cleaner.
      print("Game selected: Numbers/Win4\n")   
      gameMode = input("Please select a gamemode. Type 'qp' for quick pick, or 'own' for your own numbers:\n")

# A new variable, called gameMode, is used for each of the games, and allows the user to either quick pick (randomly generate numbers), or select their own numbers.
# Just like the main menu, if the user inputs anything else than what is asked, the program will not continue until a valid input is received.
      
      while gameMode != 'qp' and gameMode != 'own':
        print("The input you provided was invalid. Please try again.\n")
        gameMode = input("Please select a valid mode:\n")

# If Numbers (selection #1) is selected as the game:
  # (Vince) If Quick Pick is selected as the gamemode:
    # - We only see "Drawing..." in the console, as a visual indicator for the user to see that their numbers are being randomly picked, and that the code below is being run.
    # - A for loop is used with a range of 3. Since Numbers requires three numbers from 0 to 9 to play, a new variable called 'x' is used to randomly select numbers from 0 to 9.
    # - When one number is selected, it is appended to the list userNumbers. This for loop will keep running until three numbers are collected in the list. Once all numbers have been collected, the program will skip to the calculation portion.
  
      if selection == 1:
        if gameMode == 'qp':
          print()
          print("Drawing...\n")
          for count in range(3): 
            x = random.randint(0, 9)
            userNumbers.append(x)

  # (Jeiby - Revamped by Vince) Else, if the user wants to input their own numbers:
    # - A for loop is used with a range of 3, just like the quick pick.
    # - The variable 'x' is used to collect three numbers from the user. Every time the user inputs a number, it is appended to the list userNumbers.
    # - (Sky) A visual aid is provided to the user to understand which slot of the list they are inputting their numbers in to, by returning the length of the list userNumbers, and converting that value into a string. When the user inputs a number, that value is increased by one until all numbers are collected.
    # - Just like the main menu and the gamemode selection, if the user inputs a number less than 0 or greater than 9, the program will not continue. If the user inputs any other character than a number, the program will end with an error.
  
        elif gameMode == 'own':
          print()
          for count in range(3):
            x = int(input("Please enter a number between 0 and 9 for slot " + str(len(userNumbers) +1) + ": "))
            while x < 0 or x > 9:
              print("The input you provided was invalid. Please try again.\n")
              x = int(input("Please enter a number between 0 and 9 for slot " + str(len(userNumbers) +1) + ": "))
            userNumbers.append(x)
          print()

# The same code happens for if Win4 (selection #2) is selected as the game, except there are four numbers required to play.
      
      elif selection == 2:
        if gameMode == 'qp':
          print()
          print("Drawing...\n")
          for count in range(4):
            x = random.randint(0, 9)
            userNumbers.append(x)
    
        elif gameMode == 'own':
          print()
          for count in range(4):
            x = int(input("Please enter a number between 0 and 9 for slot " + str(len(userNumbers) +1) + ": "))
            while x < 0 or x > 9:
              print("The input you provided was invalid. Please try again.\n")
              x = int(input("Please enter a number between 0 and 9 for slot " + str(len(userNumbers) +1) + ": "))
            userNumbers.append(x)
          print()

# Same thing for Take 5 (selection #3), except there are five numbers required to play, from 1 to 39.
          
    elif selection == 3:
      os.system("clear")
      print("Game selected: Take 5\n")
      gameMode = input("Please select a gamemode. Type 'qp' for quick pick, or 'own' for your own numbers:\n")
      while gameMode != 'qp' and gameMode != 'own':
        print("The input you provided was invalid. Please try again.\n")
        gameMode = input("Please select a valid mode: ")

      if gameMode == 'qp':
        print()
        print("Drawing...\n")
        for count in range(5):
          x = random.randint(1, 39)
          userNumbers.append(x)
    
      elif gameMode == 'own':
        print()
        for count in range(5):
          x = int(input("Please enter a number between 1 and 39 for slot " + str(len(userNumbers) +1) + ": "))
          while x < 1 or x > 39:
            print("The input you provided was invalid. Please try again.\n")
            x = int(input("Please enter a number between 1 and 39 for slot " + str(len(userNumbers) +1) + ": "))
          userNumbers.append(x)
        print()
    
# Again, same thing for Powerball (selection #4) or Mega Millions (selection #5).
# A powerball/mega ball is required for both games, and they both use the list powerBall.

    if selection == 4 or selection == 5:
      os.system("clear")
      print("Game selected: Powerball/Mega Millions\n")
      gameMode = input("Please select a gamemode. Type 'qp' for quick pick, or 'own' for your own numbers:\n")
      while gameMode != 'qp' and gameMode != 'own':
        print("The input you provided was invalid. Please try again.\n")
        gameMode = input("Please select a valid mode: ")

# If Powerball is selected as the game, the same code runs, and there are five numbers required between 1 and 69.
      if selection == 4: 
        if gameMode == 'qp':
          print()
          print("Drawing...\n")
          for count in range(5):
            x = random.randint(1, 69)
            while x in userNumbers:
              x = random.randint(1, 69)
            userNumbers.append(x)
          print()

# A for loop which only executes randomly assigns one number between 1 and 26 for the powerball, and appends it to the list powerBall.
          for count in range(1):
            x = random.randint(1,26)
            powerBall.append(x)

        elif gameMode == 'own':
          print()
          for count in range(5):
            x = int(input("Please enter a number between 1 and 69 for slot " + str(len(userNumbers) +1) + ": "))
            while x < 1 or x > 69:
              print("The input you provided was invalid. Please try again.\n")
              x = int(input("Please enter a number between 1 and 69 for slot " + str(len(userNumbers) +1) + ": "))
            userNumbers.append(x)

# Same thing as above, with the powerball.
          for count in range(1):
            x = int(input("Please enter a number between 1 and 26 for the powerball: "))
            while x < 1 or x > 26:
              print("The input you provided was invalid. Please try again.\n")
              x = int(input("Please enter a number between 1 and 26 for the powerball: "))
            powerBall.append(x)
          print()
     
# For mega millions, the same thing, yet again, except the user numbers can be between 1 and 70, and the mega ball can be between 1 and 25. The same lists, userNumbers and powerBall, are used for all games.        
      elif selection == 5:
        if gameMode == 'qp':
          print()
          print("Drawing...\n")
          for count in range(5):
            x = random.randint(1, 70)
            while x in userNumbers:
              x = random.randint(1, 70)
            userNumbers.append(x)
    
          for count in range(1):
            x = random.randint(1, 25)
            powerBall.append(x)
    
        elif gameMode == 'own':
          print()
          for count in range(5):
            x = int(input("Please enter a number between 1 and 70 for slot " + str(len(userNumbers) +1) + ": "))
            while x < 1 or x > 70:
              print("The input you provided was invalid. Please try again.\n")
              x = int(input("Please enter a number between 1 and 70 for slot " + str(len(userNumbers) +1) + ": "))
            userNumbers.append(x)
    
          for count in range(1):
            x = int(input("Please enter a number between 1 and 25 for the mega ball: "))
            while x < 1 or x > 25:
              print("The input you provided was invalid. Please try again.\n")
              x = int(input("Please enter a number between 1 and 25 for the mega ball: "))
            powerBall.append(x)
          print()

# (Vince) - Else, if the selection is 6, which is the help menu, a function called help_menu() is called, and is defined near the end of the code.
# Once the help menu is selected, as an extra precaution, the list userNumbers and powerBall are once again cleared.
            
    elif selection == 6:
      os.system("clear")
      help_menu()
      userNumbers.clear()
      powerBall.clear()

###### Drawings: ######
# Credit: Sky

# Once all the input from the user from the received, for each game, it passes through more if statements. All drawn numbers are assigned below.
# If the game selected is either Numbers (selection #1) or Win4 (selection #2):
  # - A new variable called drawnNumbers is created, with a list that contains a nested loop. Random numbers between 0 and 9 will be appended to each slot in the list, in the range of the already existing list, userNumbers. A list cannot be passed directly to be calculated, so its length is returned.
  # - This code is represented in the console output, showing the user's numbers and the drawn numbers, to provide a visual comparison between both.

    if selection == 1 or selection == 2:
      # For testing purposes only - drawnNumbers = [6, 3, 5, 2]
      drawnNumbers = [random.randint(0, 9) for x in range(len(userNumbers))]
      print("The numbers you selected were:", userNumbers)
      time.sleep(2)
      print("The numbers drawn were:", drawnNumbers)

# The same code executes for Take 5 (selection #3), except there are five numbers, once again:
    elif selection == 3:
      # For testing purposes only - drawnNumbers = [8, 34, 23, 14, 28]
      drawnNumbers = [random.randint(1, 39) for x in range(len(userNumbers))]
      print("The numbers you selected were:", userNumbers)
      time.sleep(2)
      print("The numbers drawn were:", drawnNumbers)
      
# Same thing for Powerball and Mega Millions, except we're including the powerball/mega ball again, using a new list called drawnPowerBall, setting its range accordingly, and reflecting that into the console output.
  # Powerball:
    elif selection == 4:
      # For testing purposes only - drawnNumbers = [54, 13, 27, 68, 9]
      # ''''''''''''''''''''''''' - drawnPowerBall = [10]
      drawnNumbers = [random.randint(1, 69) for x in range(len(userNumbers))]
      drawnPowerBall = [random.randint(1, 26) for x in range(len(powerBall))]
      print("The numbers you selected were:", userNumbers, "with a powerball of", powerBall)
      time.sleep(2)
      print("The numbers drawn were:", drawnNumbers, "with a powerball of", drawnPowerBall)

  # Mega Millions:
    elif selection == 5:
      # For testing purposes only - drawnNumbers = [65, 41, 29, 8, 30]
      # ''''''''''''''''''''''''' - drawnPowerBall = [22]
      drawnNumbers = [random.randint(1, 70) for x in range(len(userNumbers))]
      drawnPowerBall = [random.randint(1, 25) for x in range(len(powerBall))]
      print("The numbers you selected were:", userNumbers, "with a mega ball of", powerBall)
      time.sleep(2)
      print("The numbers drawn were:", drawnNumbers, "with a mega ball of", drawnPowerBall)

###### Calculations: ######
# Credit: Sky
  
# For the calculations to run, the code checks the selection variable to verify it matches a game.
# The calculations will not run if:
  # - The selection is '6' for the help menu
  # - The user makes an invalid selection in the main menu or help menu
  # - The user makes an input that causes the code to stop and provide a value error exception

  # If the selection matches a gamemode, the code pauses for one second before beginning calculations, to provide a visual effect in the console.
  
    if selection == 1 or selection == 2 or selection == 3 or selection == 4 or selection == 5:
      print()
      time.sleep(1)
      print("Calculating...\n")
      time.sleep(0.5)
    
  # If the game selected is Numbers (selection #1):  
  # A user can win straight, box, front pair, or back pair. All of this is explained in the help menu.
    if selection == 1:
      
  # Straight Play Win:
  # If all the user numbers matches the drawn numbers in the exact order, they win a straight prize of $500.
      if userNumbers == drawnNumbers:
        print("Straight Win: All of your numbers matched!")
        print("Congratulations, you won $500!\n")
        
  # Box Play:
  # Else, if all of the user numbers matches the drawn numbers but not in the exact order, they win a box prize of $80.
  # In order to compare numbers, a new variable called compareNumbers is created, using set().intersection().
    # - A set() converts the list userNumbers into a set, or an unordered "list" or collection of items. It is used here to be able to compare every number in the lists userNumbers and drawnNumbers together, identifying which numbers match. I had to do some research on this as I couldn't figure out how to compare individual values within lists.
    # - intersection() returns what is common or what values "match" between two lists. For example, we are comparing both the lists userNumbers and drawnNumbers, to figure out what numbers match, and to determine what the player's prize will be.
    # - An alternative to set() and intersection() to compare lists would be to use the list.sort() function. set().intersection() is used here for every calculation.
    # - If the length of numberComparison returns a value of 3 -- or simply, if the player matched all of their numbers, but not in the right order, they win a box prize of $80.

      elif userNumbers != drawnNumbers:
        compareNumbers = set(userNumbers).intersection(drawnNumbers)
        if len(compareNumbers) == 3:
          print("Box Win: All of your numbers matched, but were not in the exact order.")
          print("Congratulations, you won $80!\n")

  # Front Pair Play: 
  # Else, if the first two indexes of the list userNumbers match with the first two indexes of the list drawnNumbers, the player wins a front pair prize of $50.
        elif [userNumbers[0], userNumbers[1]] == [drawnNumbers[0], drawnNumbers[1]]:
          print("Front Pair Win: The first two numbers you drew matched.")
          print("Congratulations, you won $50!\n")

  # Back Pair Play:
  # Else, if the last two indexes of the list userNumbers match with the last two indexes of the list drawnNumbers, the player wins a back pair prize of $50.
        elif [userNumbers[1], userNumbers[2]] == [drawnNumbers[1], drawnNumbers[2]]:
          print("Back Pair Win: The last two numbers you drew matched.")
          print("Congratulations, you won $50!\n")
          
  # Else, if the user numbers don't match any of the conditions above, it results in no money won. :(
        else:
          print("None of your numbers matched the winning criteria.")
          print("Sorry, you didn't win any money. Please try again.\n")

# Same thing as above for calculating Win 4 (selection #2) prizes:
    elif selection == 2:

  # Straight Play:
      if userNumbers == drawnNumbers:
        print("Straight Win: All of your numbers matched!")
        print("Congratulations, you won $5,000!\n")
        
  # Box Play:
      elif userNumbers != drawnNumbers:
        compareNumbers = set(userNumbers).intersection(drawnNumbers)
        if len(compareNumbers) == 4:
          print("Box Win: All of your numbers matched, but were not in the exact order.")
          print("Congratulations, you won $200!\n")

  # Front Pair Play:      
        elif [userNumbers[0], userNumbers[1]] == [drawnNumbers[0], drawnNumbers[1]]:
          print("Front Pair Win: The first two numbers you drew matched.")
          print("Congratulations, you won $50!\n")

  # Back Pair Play:
        elif [userNumbers[2], userNumbers[3]] == [drawnNumbers[2], drawnNumbers[3]]:
          print("Back Pair Win: The last two numbers you drew matched.")
          print("Congratulations, you won $50!\n")

  # No money:
        else:
          print("None of your numbers matched the winning criteria.")
          print("Sorry, you didn't win any money. Please try again.\n")

# Same thing for Take 5 (selection #3), but there are different prize amounts, explained in the help menu.
# If all of the numbers match, the user wins the jackpot.
    elif selection == 3:
      if userNumbers == drawnNumbers:
        print("All of your numbers matched!")
        print("Congratulations, you won the jackpot!\n")

  # Else, if all numbers match, but are not in the exact order:    
      elif userNumbers != drawnNumbers:
        compareNumbers = set(userNumbers).intersection(drawnNumbers)
        if len(compareNumbers) == 5:
          print("All of your numbers matched!")
          print("Congratulations, you won the jackpot!\n")

  # Else, if four numbers match, the player wins a prize of $508.
    # A new variable, called amountWon, deducts money from prize, the variable we defined as having a value of 1,000,000, at the beginning of the code.
    # It is then used in awarding the user their prize money.
        elif len(compareNumbers) == 4:
          print("Four of your numbers matched!")
          amountWon = prize - 999492
          print("Congratulations, you won", amountWon, "dollars!\n")

  # Else, if three numbers match:      
        elif len(compareNumbers) == 3:
          print("Three of your numbers matched!")
          amountWon = prize - 999975
          print("Congratulations, you won", amountWon, "dollars!\n")
          
  # No money:
        else:
          print("None of your numbers matched the winning criteria.")
          print("Sorry, you didn't win any money. Please try again.\n")

# Powerball (selection #4) and Mega Millions (selection #5):
# Same thing, considering the powerball/mega ball as well. Everything is explained in the help menu.
  # - If all of the numbers match with the powerball/mega ball, the user wins the jackpot.
  # - If all of the numbers match, but the powerball/mega ball does not, the user wins $1,000,000.

    elif selection == 4 or selection == 5:
      if userNumbers == drawnNumbers and powerBall == drawnPowerBall:
        print("All of your numbers matched!")
        print("Congratulations, you won the jackpot!\n")
      elif userNumbers == drawnNumbers and powerBall != drawnPowerBall:
        print("All of your numbers matched, but your powerball or mega ball did not match.")
        print("Congratulations, you won", prize, "dollars!\n")

  # Else, if both number lists don't match, but the powerball matches:
      elif userNumbers != drawnNumbers and powerBall == drawnPowerBall:
        compareNumbers = set(userNumbers).intersection(drawnNumbers)

  # If all numbers match:
        if len(compareNumbers) == 5:
          print("All of your numbers matched!")
          print("Congratulations, you won the jackpot!\n")

  # If four numbers and the powerball/megaball match:
        if len(compareNumbers) == 4:
          print("Four of your numbers matched!")
          if selection == 4:
            amountWon = prize - 950000
            print("Congratulations, you won", amountWon, "dollars!\n")
          elif selection == 5:
            amountWon = prize - 990000
            print("Congratulations, you won", amountWon, "dollars!\n")

  # If three numbers and the powerball/megaball match:
        elif len(compareNumbers) == 3:
          print("Three of your numbers matched!")
          if selection == 4:
            amountWon = prize - 999900
            print("Congratulations, you won", amountWon, "dollars!\n")
          elif selection == 5:
            amountWon = prize - 999800
            print("Congratulations, you won", amountWon, "dollars!\n")
    
  # If two numbers and the powerball/megaball match:
        elif len(compareNumbers) == 2:
          print("Two of your numbers matched!")
          if selection == 4:
            amountWon = prize - 999993
            print("Congratulations, you won", amountWon, "dollars!\n")
          elif selection == 5:
            amountWon = prize - 999990
            print("Congratulations, you won", amountWon, "dollars!\n")
        
  # If one or no numbers match, and the powerball/megaball also matches:
        elif len(compareNumbers) == 1 or len(compareNumbers) == 0:
          if selection == 4:
            print("Either one or none of your numbers matched with the powerball.")
            amountWon = prize - 999996
            print("Congratulations, you won", amountWon, "dollars!\n")
          elif selection == 5:
            if len(compareNumbers) == 1:
              print("One of your numbers matched!")
              amountWon = prize - 999996
              print("Congratulations, you won", amountWon, "dollars!\n")
            elif len(compareNumbers) == 0:
              print("None of your numbers matched with the mega ball.")
              amountWon = prize - 999998
              print("Congratulations, you won", amountWon, "dollars!\n")
    
  # The exact same code above will play down below, except this time, the powerball does not match.
      elif userNumbers != drawnNumbers and powerBall != drawnPowerBall:
        compareNumbers = set(userNumbers).intersection(drawnNumbers)

  # If five numbers match:
        if len(compareNumbers) == 5:
          print("All of your numbers matched, but your powerball or mega ball did not match.")
          amountWon = prize
          print("Congratulations, you won", prize, "dollars!\n")

  # If four numbers match:
        elif len(compareNumbers) == 4:
          print("Four of your numbers matched, but your powerball or mega ball did not match.")
          if selection == 4:
            amountWon = prize - 999900
            print("Congratulations, you won", amountWon, "dollars!\n")
          elif selection == 5:
            amountWon = prize - 999500
            print("Congratulations, you won", amountWon, "dollars!\n")

  # If three numbers match:
        elif len(compareNumbers) == 3:
          print("Three of your numbers matched, but your powerball or mega ball did not match.")
          if selection == 4:
            amountWon = prize - 999993
            print("Congratulations, you won", amountWon, "dollars!\n")
          elif selection == 5:
            amountWon = prize - 999990
            print("Congratulations, you won", amountWon, "dollars!\n")
            
  # No money:
        else:
          print("None of your numbers matched the winning criteria.")
          print("Sorry, you didn't win any money. Please try again.\n")

# (Vince) - If a game was selected and a successful calculation was determined, the user will be prompted if they want to play again or not.
    if selection == 1 or selection == 2 or selection == 3 or selection == 4 or selection == 5:
      replay = str(input("Would you like to play again? Enter 'y' for yes, or 'n' for no:\n"))

  # Input validation once more, will keep asking until a valid input is received.

      while replay != 'y' and replay != 'Y' and replay != 'n' and replay != 'N':
        print("The input you provided was invalid. Please try again.\n")
        replay = str(input("Please enter a valid response:\n"))

  # If the user selects to replay, then the console output is cleared, all lists are cleared, and the function main() is called again.
      if replay == 'y' or replay == 'Y':
        os.system("clear")
        userNumbers.clear()
        powerBall.clear()
        time.sleep(0.5)
        print("Success: New game started. Good luck!\n")
        main()

  # Else, if the user doesn't want to replay, the program will end.
      elif replay == 'n' or replay == 'N':
        print()
        print("Thank you for playing, and have a nice day! To replay at any time, please type 'main().'")

# If at any time the user inputs an invalid value such as a letter when the program is asking for a number, this code will execute instead of an exception, and provide a suggestion to the user.
  except ValueError:
    print()
    print("Value Error: An error occurred while processing your request.\n"
          "Reason: Please make sure you are entering numeric values into the program when prompted.\n\n"
          "To restart the program, type 'main().'")

###### Help Menu Functions: ###### 
# Credit: Vince / Revised/Enhanced by Sky

# This function, help_menu(), is called if the user's selection is '6' from the main menu.
# The help menu works the exact same way as the main menu.
def help_menu():
  print("=== Help Menu: ===\n")
  print("Here is a list of all of the gamemodes available for info:")
  print('1: Numbers\n'
        '2: Win4\n'
        '3: Take 5\n'
        '4: Powerball\n'
        '5: Mega Millions\n')

  helpChoice = int(input("For help on a gamemode, enter its corresponding number. To return to the main menu, type in '6':\n"))

# A new variable, called helpChoice, is used for each of the games.
# Just like the main menu, if the user inputs anything else than what is asked, the program will not continue until a valid input is received.
  
  while helpChoice < 1 or helpChoice > 6:
    print("The input you provided was invalid. Please try again.\n")
    helpChoice = int(input("For help on a gamemode, enter its corresponding number. To return to the main menu, type in '6':\n"))

# More functions are called below for each of the games.
  # - If Numbers or Win4 are selected (help choices #1 and #2), the function numbers_win4_help() is called.
  # - Else, if Take 5 is selected (help choice #3), the function take5_help() is called.
  # - Else, if Powerball or Mega Millions are selected (help choices #4 and #5), the function power_mega_help() is called.
  # - Else, if the user wants to return back to the main menu (help choice #6), the function main() is called, taking the user back to the main menu.
  if helpChoice == 1 or helpChoice == 2:
    os.system("clear")
    numbers_win4_help()
  elif helpChoice == 3:
    os.system("clear")
    take5_help()
  elif helpChoice == 4 or helpChoice == 5:
    os.system("clear")
    power_mega_help()
  elif helpChoice == 6:
    os.system("clear")
    main()

# This function explains how Numbers and Win4 works, including the prize money, and odds of winning each gamemode.
def numbers_win4_help():
  print("=== How to win Numbers or Win 4: ===\n\n"
        "Numbers and Win4 have similar rules, but have a difference of one number, with Win4 offering a larger prize. There are four ways to win Numbers or Win4:\n\n"
        "1) Straight Play: To win a straight play, a player must match their numbers with the winning numbers, in the *exact order* they are drawn in.\n\n"
        "For example, if the winning number is [4, 9, 3, 2], the player wins a straight prize if their chosen numbers are 4, 9, 3, and 2, in that exact order.\n\n"
        "The prize for winning a straight play is *$500 for Numbers, and $5,000 for Win4.* The odds of winning a straight play is roughly 1 in 1,000 for Numbers, and 1 in 10,000 for Win4.\n")
  
  print("---------\n")
    
  print("2) Box Play: To win a box play, a player must select three numbers that match the winning number, in *any order.*\n\n"
        "For example, if the winning number is [2, 7, 3], the player wins a box prize if their chosen numbers are either 279, 327, 372, 723, or 732.\n\n"
        "The prize for winning a box play is *$80 for Numbers, and $200 for Win4.* The odds of winning a box play is roughly 1 in 167 for Numbers, and 1 in 417 for Win4.\n")
  
  print("---------\n")
      
  print("3) Front Pair/Back Pair Play: To win a front pair play, a player must match their first and second number with the first two digits of the winning number. Adversely, to win a back pair play, the last two numbers must match with the last two digits of the winning number.\n\n"
        "For example, if the winning number is [5, 8, 6, 1], the player wins a front pair prize if the first two digits of their number are 5 and 8, in that exact order. Adversely, a back pair win requires the numbers 6 and 1 in that exact order, for the last two digits.\n\n"
        "The prize for winning a front pair or back pair play is *$50 for both Numbers and Win4.* The odds of winning a pair play is roughly 1 in 100 for both games.\n")
  
  print("---------\n")

  menuControl = input("To return to the main menu, type 'main'. To return to the help menu, type 'help':\n")

# (Sky) - New menu control variable which prompts the user whether they want to return to the main menu or want more help. Again, if anything else is inputted than what is asked, the program will not continue.
  
  while menuControl != 'main' and menuControl != 'help':
    print("The input you provided was invalid. Please try again.\n")
    menuControl = input("To return to the main menu, type 'main'. To return to the help menu, type 'help':\n")

# If the user selects to return to the main menu, the console is cleared, and the function main() is called again. Same thing happens with the help menu, except the function help_menu() is called.
  if menuControl == 'main':
    os.system("clear")
    main()
  elif menuControl == 'help':
    os.system("clear")
    help_menu()

# Same thing as above, except for Take 5.
def take5_help():
  print("=== How to win Take 5: ===\n")
  print("Take 5 is a simple and straightforward lottery game which can gives you the chance of earning tens of thousands of dollars every day.\n\n"
        "The only way to win a Take 5 game is by matching five numbers. Matches of three or more numbers in any order guarantees a prize win. Refer to the following table below:\n\n"
        "Prize Tier\t| Odds of Winning\t| Estimated Prize\n"
        "Match 5  \t  1 in 575,757   \t  $57,575 / Jackpot\n"
        "Match 4  \t  1 in 3,386     \t  $508\n"
        "Match 3  \t  1 in 102       \t  $25\n\n"
        "Matches of zero, one, or two numbers offer no prize.\n")
  
  print("---------\n")
  
  menuControl = input("To return to the main menu, type 'main'. To return to the help menu, type 'help':\n")
    
  while menuControl != 'main' and menuControl != 'help':
    print("The input you provided was invalid. Please try again.\n")
    menuControl = input("To return to the main menu, type 'main'. To return to the help menu, type 'help':\n")
      
  if menuControl == 'main':
    os.system("clear")
    main()
  if menuControl == 'help':
    os.system("clear")
    help_menu()

# Lastly, same thing as above, but for Powerball and Mega Millions.
def power_mega_help():
  print("=== How to Win Powerball or Mega Millions: ===\n\n"
        "Powerball and Mega Millions have similar rules, but have a difference of one number. Both games offer similar prizes with up to billions of dollars if the jackpot is hit.\n\n"
        "It is statistically much harder to win a mega millions jackpot than it is to win a powerball jackpot, as your odds of winning are ten million times less likely.\n\n"
        "The only way to win a powerball or mega millions game is by matching five white ball numbers, and one red powerball or megaball. Refer to the following tables below:\n\n"
  
        "---------\n\n"
    
        "Powerball Odds and Prizes:\n\n"
        "Prize Tier \t\t\t|\t Odds of Winning\t| Prize Money\n"
        "Match 5 + Powerball \t 1 in 292,201,338 \t  Jackpot\n"
        "Match 5 \t\t\t\t 1 in 11,688,054 \t  $1 million\n"
        "Match 4 + Powerball \t 1 in 913,129 \t\t  $50,000\n"
        "Match 4 \t\t\t\t 1 in 36,525 \t\t  $100\n"
        "Match 3 + Powerball \t 1 in 14,494 \t\t  $100\n"
        "Match 3 \t\t\t\t 1 in 580 \t\t\t  $7\n"
        "Match 2 + Powerball \t 1 in 701 \t\t\t  $7\n"
        "Match 1 + Powerball \t 1 in 92 \t\t\t  $4\n"
        "Match 0 + Powerball \t 1 in 38 \t\t\t  $4\n\n"
  
        "---------\n\n"
  
        "Mega Millions Odds and Prizes:\n\n"
        "Prize Tier \t\t\t|\t Odds of Winning\t| Prize Money\n"
        "Match 5 + Mega Ball \t 1 in 302,575,350 \t  Jackpot\n"
        "Match 5 \t\t\t\t 1 in 12,607,306 \t  $1 million\n"
        "Match 4 + Mega Ball \t 1 in 931,001 \t\t  $10,000\n"
        "Match 4 \t\t\t\t 1 in 38,792 \t\t  $500\n"
        "Match 3 + Mega Ball \t 1 in 14,547 \t\t  $200\n"
        "Match 3 \t\t\t\t 1 in 606 \t\t\t  $10\n"
        "Match 2 + Mega Ball \t 1 in 693 \t\t\t  $10\n"
        "Match 1 + Mega Ball \t 1 in 89 \t\t\t  $4\n"
        "Match 0 + Mega Ball \t 1 in 37 \t\t\t  $2\n")
  
  print("---------\n")
  
  menuControl = input("To return to the main menu, type 'main'. To return to the help menu, type 'help':\n")
    
  while menuControl != 'main' and menuControl != 'help':
    print("The input you provided was invalid. Please try again.\n")
    menuControl = input("To return to the main menu, type 'main'. To return to the help menu, type 'help':\n")
      
  if menuControl == 'main':
    os.system("clear")
    main()
  if menuControl == 'help':
    os.system("clear")
    help_menu()

# Calling the main function - this is required for initializing the code.
main()
