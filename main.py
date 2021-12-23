# a = [1, 2, 3, 4, 5, 6]
# b = a
# b[2] = 100

# import time
# a = list(map(int, input().split()))
# b=0
# for i in a:
#     if i>-1:
#         b+=1
#     else:
#         continue
# print(b)
# time.sleep(2)
# print("1000 - 7")
# b = 0
# a = list(map(int,input().split()))
# for i in range (1, len(a)):
#     if a[i]>a[i-1] and a[i]>a[i+1]:
#         b+=1
# print(b)
# a = [[1,2,3], [4,5,6],[7,8,9]]
#
# for i in a:
#     print[*a]
# n, m = map(int, input().split())
# a = []
# for i in range(a):
#     a.append(list(map(int, input().split())))
# n, m = map(int, input().split())
# scores = []
# potential_winners = []
# for i in range:
#     scores.append(list(map(int, input())))
#
#
# for players_scores in score:
# def razrad(n):
#     if n/10<1:
#         return 1
#     else:
#         s=1+razrad(n//10)
#         return s
# a=int(input())
# print(razrad(a))
print("**********"" Игра Крестики-нолики для двух игроков ""**********")

board = list(range(1,10))

def draw_board(board):
   print("-------------")
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-------------")

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Ты число то не ввёл!")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Клетка занята!")
      else:
        print("Неверно. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

