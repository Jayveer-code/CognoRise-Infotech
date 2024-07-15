import random
def user_input():
    side=int(input("Enter The Number of side in dice.."))
    rolls=int(input("Enter The Number of rolls.."))
    return side,rolls
def rol_dice(side,rolls):
    result=[random.randint(1,side)for _ in range(rolls)]
    return result
def dis_result(result):
    print("Dice roll result is...",result)
def final():
    while True:
         side,rolls=user_input()
         result=rol_dice(side,rolls)
         dis_result(result)

         palyagain=input("Do You want to play Again (yes/no):").lower()
         if not  palyagain.startswith('y'):
             break
final()

