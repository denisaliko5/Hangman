import turtle
import random
import string
print("\nWelcome to HANGMAN!\n")

#Variables
w = turtle.Turtle() #writer
hm = turtle.Turtle() #hangman
w.ht()
hm.ht()
w.speed(0)
hm.speed(0)
hm.pensize(5)

#Title
w.pu()
w.goto(-20, 80)
w.pd()
w.write("HANGMAN", font=("Times New Roman", 40, "bold"))

#Draw Hangman's gallow
hm.pu()
hm.goto(-215, -100)
hm.pd()
hm.bk(50)
hm.fd(100)
hm.bk(50)
hm.lt(90)
hm.fd(200)
hm.rt(90)
hm.fd(130)
hm.rt(90)
hm.fd(30)

#Draw hangman
def draw_head():
  hm.rt(90)
  hm.circle(20, 540)
def draw_body():
  hm.rt(90)
  hm.fd(60)
def draw_legs():
  hm.rt(35)
  hm.fd(30)
  hm.bk(30)
  hm.lt(70)
  hm.fd(30)
  hm.bk(30)
def draw_hands():
  hm.rt(35)
  hm.bk(40)
  hm.rt(70)
  hm.fd(30)
  hm.bk(30)
  hm.lt(140)
  hm.fd(30)
  hm.bk(30)
  hm.rt(70)
draw_hangman = [draw_head, draw_body, draw_legs, draw_hands]
  
#Secret word
names = ['apple', 'orange', 'potato', 'tomato', 'meat', 'bread']
name = list(random.choice(names))
length = len(name)
set_length = len(set(name))
len_list = []
for i in range(length):
  len_list.append(i)
  
#Create letters' placeholders
placeholder = []
for i in range(length):
  i = turtle.Turtle()
  placeholder.append(i)
  i.ht()
  i.pensize(5)
  i.speed(0)

#Draw letters' placeholders
placeholder_cor = []
def letters_placeholders_drawer():
  a = 15
  b = 35
  x = 0
  for i, e in enumerate(len_list):
    placeholder[i].pu()
    placeholder[i].goto(x, -100)
    e = placeholder[i].xcor()
    placeholder_cor.append(e)
    placeholder[i].pd()
    placeholder[i].fd(a)
    x += b
letters_placeholders_drawer()

#Writer
def writer(letter):
  for i in index_list:
    w.pu()
    if letter == 'm':
      w.goto(placeholder_cor[i]-10, -100)
    else:
      w.goto(placeholder_cor[i], -100)
    w.pd()
    w.write(letter, font=("Times New Roman", 30, "normal"))

#Answer revealer1
def writer2():
  index_list2 = []
  for i in range(len(name)):
    if i not in co_index_list:
      index_list2.append(i)
  for i in index_list2:
    w.pu()
    if name[i] == 'm':
      w.goto(placeholder_cor[i]-10, -100)
    else:
      w.goto(placeholder_cor[i], -100)
    w.pd()
    w.write(name[i], font=("Times New Roman", 30, "normal"))
    
#Answer revealer2
def show_answer():
  w.pu()
  w.goto(0, -100)
  w.pd()
  x = 0
  for i in name:
    if i == 'm':
      w.pu()
      w.goto(x-10, -100)
      w.pd()
    w.write(i, font=("Times New Roman", 30, "normal"))
    x+=35
    w.pu()
    w.goto(x, -100)
    w.pd()

#The main algorithm
alphabet = list(string.ascii_lowercase)
guess_list = []
guess_limit = 4
guess_cnt = 0
cor_cnt = 0
index_list = []
co_index_list = []
while guess_cnt <= guess_limit-1:
  while True:
    guess = input("Guess a letter: ").lower()
    if guess in alphabet:
        break
    else:
      print("Invalid Input!")
  while guess in guess_list:
    guess = input("Guess another letter: ").lower()
  guess_list.append(guess)
  if guess in name:
    for i in range(len(name)):
      if name[i] == guess:
        index_list.append(i)
        co_index_list.append(i)
        writer(guess)
    index_list.clear()
    cor_cnt += 1
    print("Correct!")
  else:
    print("Incorrect!")
    draw_hangman[guess_cnt]()
    guess_cnt += 1
  if cor_cnt == set_length:
    print("\nYou win!\n")
    w.color("green")
    w.pu()
    w.goto(-20, 30)
    w.pd()
    w.write("You win!", font=("Times New Roman", 30, "normal"))
    show_answer()
    w.color("black")
    break
else:
  print("\nYou lose!\n")
  hm.color("red")
  hm.speed(10)
  hm.pu()
  hm.goto(-85, 70)
  hm.pd()
  for f in draw_hangman:
    f()
  w.color("red")
  w.pu()
  w.goto(-20, 30)
  w.pd()
  w.write("You lose!", font=("Times New Roman", 30, "normal"))
  writer2()
  if cor_cnt == 0:
    show_answer()