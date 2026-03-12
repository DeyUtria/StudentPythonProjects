print("I have information for the following planets:\n")


print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = float(input("What is your weight on Earth in pounds? "))
planet = input("Which planet are you visiting? ")


# Write an if statement below:
if planet == "Venus":
  gravity = 0.91
  codey_weight = weight * gravity
  print("Codey's weight in Venus is " + str(codey_weight) + " pounds.")


if planet == "Mars":
  gravity = 0.38
  codey_weight = weight * gravity
  print("Codey's weight in Mars is " + str(codey_weight) + " pounds.")


if planet == "Jupiter":
  gravity = 2.34
  codey_weight = weight * gravity
  print("Codey's weight in Jupiter is " + str(codey_weight) + " pounds.")


if planet == "Saturn":
  gravity = 1.06
  codey_weight = weight * gravity
  print("Codey's weight in Saturn is " + str(codey_weight) + " pounds.")


if planet == "Uranus":
  gravity = 0.92
  codey_weight = weight * gravity
  print("Codey's weight in Uranus is " + str(codey_weight) + " pounds.")


if planet == "Neptune":
  gravity = 1.19
  codey_weight = weight * gravity
  print("Codey's weight in Neptune is " + str(codey_weight) + " pounds.")