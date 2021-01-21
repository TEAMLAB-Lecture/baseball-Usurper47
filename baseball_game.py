# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(val):
  return val.isdigit()

def is_between_100_and_999(val:str):
  if 100 <= int(val) < 1000:
    return True
  return False

def is_duplicated_number(val:str):
  from collections import Counter
  if len(Counter(val)) == 3:
    return True
  return False

def is_validated_number(val:str):
  if is_digit(val):
    if is_between_100_and_999(val):
      if is_duplicated_number(val):
        return True
  return False

def get_not_duplicated_three_digit_number()->int:
  while 1:
    tmp = get_random_number()
    if is_validated_number(tmp):
      return int(tmp)

def get_strikes_or_ball(player:str, computer:str):
  strikes = 0
  balls = len(set(player) & set(computer))
  for p, c in zip(player, computer):
    if p == c:
      strikes += 1
      balls -= 1
  return [strikes, balls]

def is_yes(s):
  if s.lower() in ('yes','y'):
    return True
  return False

def is_no(s):
  if s.lower() in ('no','n'):
    return True
  return False


def main():
    print("Play Baseball")
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    
    flag = 1
    while flag:
      user_input = input('Input guess number : ')

      if user_input == '0':
        break
      
      if not is_validated_number(user_input):
        print("Wrong Input, Input again") # Input again
        continue

      s, b = get_strikes_or_ball(user_input, random_number)
      print(f'Strikes : {s} , Balls : {b}')

      if s == 3:
        while 1:
          ans = input("You win, one more(Y/N)?")
          
          if is_yes(ans):
            random_number = str(get_not_duplicated_three_digit_number())
            print("Random Number is : ", random_number)
            break

          elif is_no(ans):
            flag = 0
            break
          else:
            print("Wrong Input, Input again")
    
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
