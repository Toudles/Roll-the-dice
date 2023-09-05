In games with two dice (such as Monopoly), rolling two 6-sided dice and getting the same side or number on both dice is called "doubles" (i.e. the first die rolls a 5 and the second die rolls a 5 at the same time). One special type of "doubles" roll is called "snake eyes," which is rolling two 1's at the same time.

The most common size of dice used in games today is the 6-sided dice, but there are plenty of other sizes available. For example, popular role-playing games such as Dungeons and Dragons use dice with a variety of sizes, such as 4, 12 and 20 sided dice.

For this assignment you will be writing a program which first prompts the user for the number of sides to the dice they will be rolling. Your user should be limited to selecting dice with the following number of sides:
  - 4 sides
  - 6 sides
  - 8 sides
  - 10 sides
  - 12 sides
  - 20 sides
You can assume that that your user will enter integers when prompted. You will need to validate their input before you continue (i.e. entering -10 should cause your program to tell the user that their input is invalid). You should re-prompt the user to enter a value if they supply bad data.

Next, your program should keep "rolling the dice" until the program generates a "snake eyes" roll (1 and 1). This means that you will roll two virtual dice of the specified size at a time. The program should "announce" every pair rolled and tell the user if the roll qualifies as one of the following:
  - A double roll (i.e. (2 and 2), (4 and 4), (6 and 6))
  - A high roll (i.e. on a six sided die, (6 and 6) )
  - A high/low roll (i.e. on a six sided die, (1 and 6) or (6 and 1)
  - An even roll (i.e. both die values are even: (2 and 2), (4 and 4))
  - An odd roll (i.e. both die values are odd: (3 and 3), (5 and 5))
  - A sum value (i.e. adding both die values together equals the size of the current die
  - Snake Eyes (1 and 1) - this should end the rolling portion of the program
At the end of the game you will want to calculate the average roll for each die and present this information to the user. See the sample program below to see what this should look like. You should format this number to twodecimal places.
