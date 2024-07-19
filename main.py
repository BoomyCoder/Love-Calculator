print("Welcome to the Love score Calcualator, You will enter yours and your partners name to find out your love score. Please enter Your name.")
name1 = input("Your name is?: ")

print("Thank you, Now please enter Their name.")
name2 = input("Their name is?: ")
      

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e


l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))


if (love_score < 25):
  print(f"Your score is {love_score} you go together like Tornato in a trailer park. ")
  
elif (love_score >= 25) and (love_score <= 50):
  print(f"Your score is {love_score} out of 100, you are alright together. ")
  
elif (love_score >= 51) and (love_score <=74):
  print(f" Your score is {love_score} out of 100, you go together like Tornato in a trailer park. ")

elif (love_score >= 75):
   print(f" Your Love score is {love_score} out of 100, You are PERFECT for eachother. ")
        
else: 
  print(f"Your score is {love_score}.")
