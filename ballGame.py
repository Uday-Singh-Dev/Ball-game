from tkinter import *
import time
import random








#global variables
orb_currency = 0
orb_increase = 1

#leaderboard variables

#variables for all of the upgrades
upgrade_speed_price = 25
upgrade_healthorb_price = 50

#teleporting orb invis checking
teleporting_orb_state = "normal"


#healing orb
healing_orb_heal = 10
#player variables
username = ""
password = ""
#character variables
color = "grey5"
speed = 6
x = 0
y = 0
health = 182

#enemy variables
enemy_damage = 2
enemy_speed = 4 

#text engine variables
Text = "hello"
max_len = 60
Next_line = False
text_length = 0
act_text = ""
Time = 0.05



#triangle variables
X_tri = 0
y_tri = 0


#the screen of the game
screen = Tk()
screen.title("Game")
screen.geometry("600x330")
screen.config(bg = "grey5")

#canvas UI contain health and orb amount
canvas_UI = Canvas(screen,bg = "grey6",width = 480,height = 50,highlightbackground="green")

#canvas game is where the gameplay happens
canvas_game = Canvas(screen,bg = "black",width=480,height=280,highlightbackground="green")
#canvas button is where you can save,leave,shop
canvas_buttons= Canvas(screen,bg = "grey6",width = 116,height = 325,highlightbackground="green")

#you can buy upgrades for your character
canvas_shop= Canvas(screen,bg = "grey6",width = 595,height = 325)

#to display text for the user
canvas_text = Canvas(screen,bg = "black",width=550,height=330)

#mainmenu of the game
canvas_mainmenu = Canvas(screen,bg = "grey6",width = 550,height = 330)

#canvas to create new game
canvas_newgame = Canvas(screen,bg = "grey4",width = 550,height = 330)

#canvas to load existing game
canvas_loadgame = Canvas(screen,bg = "grey4",width = 550,height = 330)

#to show the scores of all players
canvas_leaderboard = Canvas(screen,bg =  "grey4",width = 595,height = 325)

#canvas to choose color of player
canvas_customize = Canvas(screen,bg = "grey4",width = 595,height = 325)

#all of the canvases
#**********************************
#the text engine subroutines


#will play a animation when entering game
def game_enter_transition_animation():
  time.sleep(0.5)
  ext_ent = 360
  canvas_text.itemconfig(game_transition,state = "normal")
  for i in range(1,179):
    ext_ent -= 2
    canvas_text.itemconfig(game_transition,extent=ext_ent)
    canvas_text.update()
    time.sleep(0.001)
  canvas_text.itemconfig(game_transition,state = "hidden")

def text_start():
  #will start the text
  canvas_UI.place_forget()
  canvas_buttons.place_forget()
  canvas_game.place_forget()
  canvas_text.pack()
  
def update():
  #updates
  canvas_text.update()
  screen.update()

def skip_line(event):
  #if space clicked during animation it will put time to 0 bypassing the animation
  global Time
  Time = 0
  update()

def next_line(event):
  global Next_line
  Next_line = True



def Next_line_waiting():
  #waiting for keyboard input to go to next line.
  global Next_line
  Next_line = False
  while Next_line == False:
    screen.bind("<space>",next_line)
    triangle_animation()
    update()
  #unbinds keyboard input
  screen.unbind("<space>")
  triangle_animation_stop()


def skip_text_waiting():
  #waiitng for user to skip text while text is being written
  global text_length,act_text,Time
  if len(act_text) < text_length:
    screen.bind("<space>",skip_line)
    update()
  return Time

def skip_text_false():
  #if skip text wasnt fufilled while animation was playing
  global Time
  Time = 0.05
  screen.unbind("<space>")




def text_animation(speaker,text,line,true,text_color):
  #displays text in an animation
  global max_len,Next_line,text_length,act_text,Time
  if true == 1:
    #checks if the editor wants a person saying the text or the narrator saying it
    text = speaker+": "+text
  text_length = len(text)
  if text_length > max_len:
    #checks if text is over max length
    print("too many character in the string")
    return
  if line ==1:
    act_text = ""
    text1.place(x=5,y=1)
    for i in range(0,text_length):
      #getting the characters of the text one by one to display an animation
      text_p = text[i]
      act_text += text_p
      #checking if person wants to skip the text animation
      skip_text_waiting()
      #changes the text and colors it based on the editors parameters
      text1.config(text = act_text,fg = text_color)
      #updates the game to display the new text
      canvas_text.update()
      #waiting time so there is a delay between each letter
      time.sleep(Time)
    #skip text is now false because animation has finished
    skip_text_false()
    triangle_xycoords(1)
    #waiting for user to press space so it can move onto the next line
    Next_line_waiting()
  if line == 2:
    act_text = ""
    text2.place(x=5,y=30)
    for i in range(0,text_length):
      text_p = text[i]
      act_text += text_p
      skip_text_waiting()
      text2.config(text = act_text,fg = text_color)
      canvas_text.update()
      time.sleep(Time)
    skip_text_false()
    triangle_xycoords(30)
    Next_line_waiting()

  if line == 3:
    act_text = ""
    text3.place(x=5,y=60)
    for i in range(0,text_length):
      text_p = text[i]
      act_text += text_p
      skip_text_waiting()
      text3.config(text = act_text,fg = text_color)
      canvas_text.update()
      time.sleep(Time)
    skip_text_false()
    triangle_xycoords(60)
    Next_line_waiting()


  if line == 4:
    act_text = ""
    text4.place(x=5,y=90)
    for i in range(0,text_length):
      text_p = text[i]
      act_text += text_p
      skip_text_waiting()
      text4.config(text = act_text,fg = text_color)
      canvas_text.update()
      time.sleep(Time)
    skip_text_false()
    triangle_xycoords(90)
    Next_line_waiting()

  if line == 5:
    act_text = ""
    text5.place(x=5,y=120)
    for i in range(0,text_length):
      text_p = text[i]
      act_text += text_p
      skip_text_waiting()
      text5.config(text = act_text,fg = text_color)
      canvas_text.update()
      time.sleep(Time)
    skip_text_false()
    triangle_xycoords(120)
    Next_line_waiting()

  if line == 6:
    act_text = ""
    text6.place(x=5,y=150)
    for i in range(0,text_length):
      text_p = text[i]
      act_text += text_p
      skip_text_waiting()
      text6.config(text = act_text,fg = text_color)
      canvas_text.update()
      time.sleep(Time)
    skip_text_false()
    triangle_xycoords(150)
    Next_line_waiting()

  if line == 7:
    act_text = ""
    text7.place(x=5,y=180)
    for i in range(0,text_length):
      text_p = text[i]
      act_text += text_p
      skip_text_waiting()
      text7.config(text = act_text,fg = text_color)
      canvas_text.update()
      time.sleep(Time)
    skip_text_false()
    triangle_xycoords(180)
    Next_line_waiting()

  if line == 8:
    act_text = ""
    text8.place(x=5,y=210)
    for i in range(0,text_length):
      text_p = text[i]
      act_text += text_p
      skip_text_waiting()
      text8.config(text = act_text,fg = text_color)
      canvas_text.update()
      time.sleep(Time)
    skip_text_false()
    triangle_xycoords(210)
    Next_line_waiting()

  if line == 9:
    act_text = ""
    text9.place(x=5,y=240)
    for i in range(0,text_length):
      text_p = text[i]
      act_text += text_p
      skip_text_waiting()
      text9.config(text = act_text,fg = text_color)
      canvas_text.update()
      time.sleep(Time)
    skip_text_false()
    triangle_xycoords(240)
    Next_line_waiting()

  if line == 10:
    act_text = ""
    text10.place(x=5,y=270)
    for i in range(0,text_length):
      text_p = text[i]
      act_text += text_p
      skip_text_waiting()
      text10.config(text = act_text,fg = text_color)
      canvas_text.update()
      time.sleep(Time)
    skip_text_false()
    triangle_xycoords(270)
    Next_line_waiting()



  pass


def talking(speaker,text,line,true,text_color):
  text_animation(speaker,text,line,true,text_color)

def reset_lines():
  #reset all of the text lines
  text1.place_forget()
  text1.config(text = "")

  text2.place_forget()
  text2.config(text = "")

  text3.place_forget()
  text3.config(text = "")

  text4.place_forget()
  text4.config(text = "")

  text5.place_forget()
  text5.config(text = "")

  text6.place_forget()
  text6.config(text = "") 

  text7.place_forget()
  text7.config(text = "")

  text8.place_forget()
  text8.config(text = "")

  text9.place_forget()
  text9.config(text = "")

  text10.place_forget()
  text10.config(text = "")
  

def triangle_xycoords(Y):
  #find the coordinates of the triangle pointer
  global text_length,X_tri,y_tri
  amount = 0
  amount  = X_tri *2
  X_tri -= amount
  amount = 0
  amount = y_tri * 2
  y_tri -= amount
  canvas_text.move(triangle,X_tri,y_tri)
  canvas_text.itemconfig(triangle,state = "normal")
  if text_length > 30 and text_length<=40:
    X_tri = text_length * 8.2
  elif text_length >40 and text_length <=45:
    X_tri = text_length * 8.6
  elif text_length >45 and text_length <= 50:
    X_tri = text_length * 8.1
  elif text_length >50 and text_length<=60:
    X_tri = text_length * 7.5
  else:
    X_tri = text_length * 8.7
  Y -= 11
  y_tri = Y
  canvas_text.move(triangle,X_tri,Y)

def triangle_animation():
  #plays a bobbing animation on the triangle
  canvas_text.move(triangle,0,+3)
  canvas_text.update()
  time.sleep(0.1)
  canvas_text.move(triangle,0,-3)
  canvas_text.update()
  time.sleep(0.1)

def triangle_animation_stop():
  #hides the triangle
  canvas_text.itemconfig(triangle,state = "hidden")








#***********************************
def game_start():
  #starts the canvasUI canvasButtons and CavnasGame
  canvas_game.place(x = 0,y =45)
  canvas_buttons.place(x=482,y=0)
  canvas_UI.place(x=0,y=0)
  orb_place_random()
  healing_orb_random()
  Teleporting_orb_random()
  character_controller()
  
  
def character_up(event):
  #makes character go up
  global speed,x,y
  y=0
  y -= speed
  x=x
  canvas_game.move(player,0,y)
  canvas_game.update()
  time.sleep(0)
  enemy_movement()
  checking_player_enemy_collision()
  checking_player_border_collision()
  player_orb_checking()
  player_healthorb_checking()
  player_teleporting_orb_checking()

def character_left(event):
  #makes character go left
  global speed,x,y
  x=0
  x -= speed
  canvas_game.move(player,x,0)
  canvas_game.update()
  time.sleep(0)
  enemy_movement()
  checking_player_enemy_collision()
  checking_player_border_collision()
  player_orb_checking()
  player_healthorb_checking()
  player_teleporting_orb_checking()

def character_down(event):
  #makes character go down
  global speed,x,y
  y=0
  y += speed
  canvas_game.move(player,0,y)
  canvas_game.update()
  time.sleep(0)
  enemy_movement()
  checking_player_enemy_collision()
  checking_player_border_collision()
  player_orb_checking()
  player_healthorb_checking()
  player_teleporting_orb_checking()

def character_right(event):
  #makes character go right
  global speed,x,y
  x=0
  x += int(speed)
  canvas_game.move(player,x,0)
  canvas_game.update()
  time.sleep(0)
  enemy_movement()
  checking_player_enemy_collision()
  checking_player_border_collision()
  player_orb_checking()
  player_healthorb_checking()
  player_teleporting_orb_checking()



def character_controller():
  #binds all of the keys for the movement
  screen.bind("<w>",character_up)
  screen.bind("<a>",character_left)
  screen.bind("<s>",character_down)
  screen.bind("<d>",character_right)

def character_controller_unbind():
  #unbinds all of the keys for the movement
  screen.unbind("<w>")
  screen.unbind("<a>")
  screen.unbind("<s>")
  screen.unbind("<d>")

def checking_player_enemy_collision():
  #checks if player and enemy are colliding to know when the player is being damaged
  player_c = canvas_game.coords(player)
  enemy_c = canvas_game.coords(enemy)
  orb_c = canvas_game.coords(orb)
  healing_orb_c = canvas_game.coords(healing_orb)
  coll = canvas_game.find_overlapping(player_c[0],player_c[1],player_c[2],player_c[3])
  enemy_coll =canvas_game.find_overlapping(enemy_c[0],enemy_c[1],enemy_c[2],enemy_c[3])
  orb_coll = canvas_game.find_overlapping(orb_c[0],orb_c[1],orb_c[2],orb_c[3],)
  healing_orb_coll = canvas_game.find_overlapping(healing_orb_c[0],healing_orb_c[1],healing_orb_c[2],healing_orb_c[3])
  coll = list(coll)
  coll.remove(player)
  enemy_coll = list(enemy_coll)
  enemy_coll.remove(enemy)
  orb_coll = list(orb_coll)
  orb_coll.remove(orb)
  healing_orb_coll = list(healing_orb_coll)
  healing_orb_coll.remove(healing_orb)
  if coll == [2] or enemy_coll == [1] or coll ==[2,3] or coll ==[2,4] or coll == [2,5] or coll == [2,6] or coll == [2,9]:
    Player_Damage()

def checking_player_border_collision():
  #checks if player is colliding with the border if so the players x or y coordiante will be reduced to previous to keep player inside of screen.
  global speed
  player_c = canvas_game.coords(player)
  left_border_c = canvas_game.coords(left_border)
  right_border_c = canvas_game.coords(right_border)
  top_border_c = canvas_game.coords(top_border)
  bottom_border_c = canvas_game.coords(bottom_border)
  player_coll = canvas_game.find_overlapping(player_c[0],player_c[1],player_c[2],player_c[3])
  left_border_coll = canvas_game.find_overlapping(left_border_c[0],left_border_c[1],left_border_c[2],left_border_c[3])
  right_border_coll = canvas_game.find_overlapping(right_border_c[0],right_border_c[1],right_border_c[2],right_border_c[3])
  top_border_coll = canvas_game.find_overlapping(top_border_c[0],top_border_c[1],top_border_c[2],top_border_c[3])
  bottom_border_coll =canvas_game.find_overlapping(bottom_border_c[0],bottom_border_c[1],bottom_border_c[2],bottom_border_c[3])
  player_coll = list(player_coll)
  player_coll.remove(player)
  left_border_coll = list(left_border_coll)
  left_border_coll.remove(left_border)
  right_border_coll = list(right_border_coll)
  right_border_coll.remove(right_border)
  top_border_coll = list(top_border_coll)
  top_border_coll.remove(top_border)
  bottom_border_coll = list(bottom_border_coll)
  bottom_border_coll.remove(bottom_border)
  
  if player_coll == [3] or left_border_coll == [1] or left_border_coll == [1,2]:
    canvas_game.move(player,speed,0)
    
  if player_coll == [4] or right_border_coll == [1] or right_border_coll == [1,2]:
    canvas_game.move(player,-speed,0)
    
  if player_coll == [5] or top_border_coll == [1] or top_border_coll == [1,2]:
    canvas_game.move(player,0,speed)
    
  if player_coll == [6] or bottom_border_coll == [1] or bottom_border_coll == [1,2]:
    canvas_game.move(player,0,-speed)

def player_Health_UI_color():
  #changes the color of the health and the borders of all of the "game_start" canvases depending on the health of the player
  global health
  if health == 182 or health >=120:
    canvas_UI.itemconfig(Health,fill = "green")
    canvas_game.config(highlightbackground="green")
    canvas_UI.config(highlightbackground="green")
    canvas_buttons.config(highlightbackground="green")
  if health < 120 and health>=60:
    canvas_UI.itemconfig(Health,fill = "yellow")
    canvas_game.config(highlightbackground="yellow")
    canvas_UI.config(highlightbackground="yellow")
    canvas_buttons.config(highlightbackground="yellow")
  if health <60:
    canvas_UI.itemconfig(Health,fill = "dark red")
    canvas_game.config(highlightbackground="dark red")
    canvas_UI.config(highlightbackground="dark red")
    canvas_buttons.config(highlightbackground="dark red")

def Player_Damage():
  #damages the player
  global enemy_damage,health
  #gets the coordiantes
  x0,y0,x1,y1 = canvas_UI.coords(Health)
  health -= enemy_damage
  #reduces health based on the enemys damage
  x1 = health
  canvas_UI.coords(Health,x0,y0,x1,y1)
  #checks if player is dead
  Player_dead_checking()
  #checks what color the health should be depending on the amount of health you have
  player_Health_UI_color()
  
def Player_Heal():
  #heals the player
  global health,healing_orb_heal
  x0,y0,x1,y1 = canvas_UI.coords(Health)
  if health <= 172:
    #checking if health is already max or >10 to max
    health += healing_orb_heal
  if health > 172:
    #else
    health = 192
  x1 = health
  canvas_UI.coords(Health,x0,y0,x1,y1)
  #checks if color has changed based on health amount
  player_Health_UI_color()
  


def Player_dead_checking():
  #checking if the player had died if so will play the death animation
  global health
  if health <= 0:
    health = 182
    text_start()
    death_animation()

def orb_place_random():
  #randomly place the orb
  x = random.randint(1,450)
  y = random.randint(1,250)
  canvas_game.moveto(orb,x,y)
  
def player_healthorb_checking():
  #checking if the player is colliding with the healthorb, if so it will heal the player
  global health,enemy_coll
  player_c = canvas_game.coords(player)
  healing_orb_c = canvas_game.coords(healing_orb)
  enemy_c = canvas_game.coords(enemy)
  player_coll = canvas_game.find_overlapping(player_c[0],player_c[1],player_c[2],player_c[3])
  
  enemy_coll =canvas_game.find_overlapping(enemy_c[0],enemy_c[1],enemy_c[2],enemy_c[3])

  healing_orb_coll = canvas_game.find_overlapping(healing_orb_c[0],healing_orb_c[1],healing_orb_c[2],healing_orb_c[3])

  player_coll = list(player_coll)
  player_coll.remove(player)
  healing_orb_coll = list(healing_orb_coll)
  healing_orb_coll.remove(healing_orb)
  enemy_coll = list(enemy_coll)
  enemy_coll.remove(enemy)
  if player_coll == [8] or healing_orb_coll == [1] or player_coll ==[2,8] or healing_orb_coll ==[1,2] or player_coll ==[7,8]:

    Player_Heal()
    healing_orb_random()
    

def player_orb_checking():
  #checking if the player is colliding with the orb, if so it will increase the orb_currency by orb_amount
  global orb_currency,enemy_coll,orb_increase
  player_c = canvas_game.coords(player)
  orb_c = canvas_game.coords(orb)
  enemy_c = canvas_game.coords(enemy)
  
  player_coll = canvas_game.find_overlapping(player_c[0],player_c[1],player_c[2],player_c[3])
  
  orb_coll = canvas_game.find_overlapping(orb_c[0],orb_c[1],orb_c[2],orb_c[3],)
  
  enemy_coll =canvas_game.find_overlapping(enemy_c[0],enemy_c[1],enemy_c[2],enemy_c[3])
  
  player_coll = list(player_coll)
  player_coll.remove(player)
  orb_coll = list(orb_coll)
  orb_coll.remove(orb)
  enemy_coll = list(enemy_coll)
  enemy_coll.remove(enemy)
  if player_coll == [7] or orb_coll == [1] or player_coll ==[2,7] or orb_coll ==[1,2] or player_coll ==[7,8]:
    orb_currency += orb_increase
    orb_amount.config(text = orb_currency)
    orb_place_random()

def player_teleporting_orb_checking():
  #checking if player is colliding with teleporting orb, if so it will teleport the player somewhere random
  global teleporting_orb_state
  if teleporting_orb_state == "normal":
    player_c = canvas_game.coords(player)
    teleporting_orb_c = canvas_game.coords(teleporting_orb)
    enemy_c = canvas_game.coords(enemy)
  
    player_coll = canvas_game.find_overlapping(player_c[0],player_c[1],player_c[2],player_c[3])
  
    teleporting_orb_coll = canvas_game.find_overlapping(teleporting_orb_c[0],teleporting_orb_c[1],teleporting_orb_c[2],teleporting_orb_c[3])
    
    enemy_coll =canvas_game.find_overlapping(enemy_c[0],enemy_c[1],enemy_c[2],enemy_c[3])
  
  
    player_coll = list(player_coll)
    player_coll.remove(player)
    teleporting_orb_coll = list(teleporting_orb_coll)
    teleporting_orb_coll.remove(teleporting_orb)
  
    enemy_coll = list(enemy_coll)
    enemy_coll.remove(enemy)
  
    if player_coll == [9] or teleporting_orb_coll == [1] or player_coll == [2,9] or teleporting_orb_coll == [1,7] or teleporting_orb_coll == [1,8]:
      teleporting_orb_function()
      Teleporting_orb_random()
  
  

def enemy_movement():
  #the movement of the enemy
  global enemy_speed
  #gets the coordiantes of the player and enemy
  player_c = canvas_game.coords(player)
  enemy_c = canvas_game.coords(enemy)

  
  player_x = player_c[0]
  player_y = player_c[1]
  
  enemy_x = enemy_c[0]
  enemy_y = enemy_c[1]
  
  diff_x = player_x - enemy_x
  diff_y = player_y - enemy_y

  #calculates the distance
  distance = (diff_x**2 + diff_y**2)**0.5
  #finds the normal
  normal_x = diff_x/distance
  normal_y = diff_y/distance

  #changes it depending on the enemy speed
  normal_x *= enemy_speed
  normal_y *= enemy_speed
  #moves enemy based on the players position
  canvas_game.move(enemy,normal_x,normal_y)

def healing_orb_random():
  #randomly places healing orb
  x = random.randint(1,450)
  y = random.randint(1,250)
  canvas_game.moveto(healing_orb,x,y)

def Teleporting_orb_random():
  #randomly places teleporting orb
  x = random.randint(1,450)
  y = random.randint(1,250)
  canvas_game.moveto(teleporting_orb,x,y)
  
def Game_Shop_Button():
  #takes user to the shop
  canvas_game.place_forget()
  canvas_UI.place_forget()
  canvas_buttons.place_forget()
  canvas_shop.pack()
  character_controller_unbind()
  
  orb_amount_shop.config(text=orb_currency)

def Shop_toGame_button():
  #takes user to the game
  canvas_shop.pack_forget()
  game_start()
  
def update_all():
  global upgrade_healthorb_price,upgrade_speed_price,orb_currency,orb_increase,healing_orb_heal,speed,orb_currency,color
  #updates all of the variables and the player
  upgrade_healthOrb_button_label.config(text = str(upgrade_healthorb_price)+"-ORB\nUpgrades the health the\n health-orbs gives")
  upgrade_speed_button_label.config(text = str(upgrade_speed_price)+"-ORB\nUpgrades the\n speed of the \nplayer")
  orb_amount_shop.config(text=orb_currency)
  orb_amount_increase.config(text ="ORB:"+str(orb_increase))
  Health_orb_amount.config(text = "HEALTHORB:"+str(healing_orb_heal))
  Player_speed.config(text = "SPEED:"+str(speed))
  orb_amount.config(text = orb_currency)
  canvas_game.itemconfig(player,fill=color)


def upgrade_speed_button():
  #button to upgrade speed of player
  global orb_currency,speed,upgrade_speed_price
  if orb_currency >= upgrade_speed_price:
    #checks if money is enough
    orb_currency -= upgrade_speed_price
    #then takes away the money
    speed += 1
    #then makes next upgrade cost more
    upgrade_speed_price *= 2
    update_all()

def upgrade_health_orb():
  global orb_currency,healing_orb_heal,upgrade_healthorb_price
  #upgrades health orb
  if orb_currency >= upgrade_healthorb_price:
    orb_currency -=upgrade_healthorb_price
    healing_orb_heal += 5
    upgrade_healthorb_price *= 2
    update_all()
    
def heal_button():
  #fully heals the player for 10 orbs
  global orb_currency,health
  if orb_currency >= 10:
    orb_currency -=10
    health = 192
    x0,y0,x1,y1 = canvas_UI.coords(Health)
    x1 = health
    canvas_UI.coords(Health,x0,y0,x1,y1)
    player_Health_UI_color()
    update_all()

def next_level_button():
  #puts user to the next level which will increase orb_increase and the enemy_speed and damage
  global enemy_speed,enemy_damage,orb_increase
  enemy_speed += 1
  enemy_damage += 0.2
  orb_increase += 1
  update_all()
  text_start()
  level_increase_text()
  reset_lines()
  game_enter_transition_animation()
  canvas_text.pack_forget()
  game_start()
  
def reset():
  global health,speed,enemy_speed,enemy_damage,orb_increase,orb_currency,upgrade_speed_price,upgrade_healthorb_price
  #resets everything for when you die
  health = 186
  x0,y0,x1,y1 = canvas_UI.coords(Health)
  x1 = health
  canvas_UI.coords(Health,x0,y0,x1,y1)
  canvas_UI.move(Health,5,0)
  player_Health_UI_color()
  

  speed = 6
  enemy_speed = 4
  enemy_damage = 2
  orb_increase = 1
  orb_currency = orb_currency // 2
  upgrade_speed_price = 50
  upgrade_healthorb_price = 50
  update_all()

def new_game_animation():
  #the text that displays upon starting a new game
  text_start()
  talking("???","Try not to touch the red orb",1,0,"red")
  talking("???","The green orb will heal you",2,0,"green")
  talking("???","Collect the blue orb and buy upgrades for yourself",3,0,"blue")
  talking("","If you think you are strong enough",4,0,"red")
  talking("","You can go to the next level, be carefull though",5,0,"red")
  reset_lines()
  game_enter_transition_animation()
  canvas_text.pack_forget()
  game_start()
  canvas_game.moveto(player,0,0)
  canvas_game.moveto(enemy,300,260)

def death_animation():
  #the text that appears when the players health reaches 0 (dies)
  talking("???","So, you have died",1,1,"red")
  talking("???","Well i cannot bring you back to where you just were",2,1,"red")
  talking("???","But, i can bring you back to the start",3,1,"red")
  talking("???","Dont die again",4,1,"red")
  reset()
  reset_lines()
  game_enter_transition_animation()
  canvas_text.pack_forget()
  game_start()
  canvas_game.moveto(player,0,0)
  canvas_game.moveto(enemy,300,260)
  
def level_increase_text():
  #the text that will appear when the player level up
  talking("","It seems that red thing has become faster",1,0,"blue")
  talking("","It has become stronger too",2,0,"blue")
  talking("","However it seems each orb is worth "+str(orb_increase)+" now",3,0,"blue")
  
def new_game_button():
  #packs canvas_new game
  canvas_mainmenu.pack_forget()
  canvas_newgame.pack()

def load_game_button():
  #packs canvas_load_game
  canvas_mainmenu.pack_forget()
  canvas_loadgame.pack()

def new_game_create():
  #creates a new game
  global input_user,input_pass,orb_currency,orb_increase,upgrade_speed_price,upgrade_healthorb_price,healing_orb_heal,speed,enemy_damage,enemy_speed,username,password,color
  #get the inputs of the user and password from the user
  username = input_user.get()
  password = input_pass.get()
  invalid_username_label_new.place_forget()
  invalid_password_label_new.place_forget()
  if len(username) <=0:
    invalid_username_label_new.place(x=100,y=55)
  if len(password) <=0:
    invalid_password_label_new.place(x=100,y=105)
  if len(username) >0 and len(password) > 0:
    NewFile = open(username+".txt","w")
   #writes all of the information for the new game 
  NewFile.write(username+"!"+password+"£"+str(orb_currency)+"$"+str(orb_increase)+"%"+str(upgrade_speed_price)+"^"+str(upgrade_healthorb_price)+"&"+str(healing_orb_heal)+"*"+str(speed)+"("+str(enemy_damage)+")"+str(enemy_speed)+"-"+(color))
  NewFile.close()
  canvas_newgame.pack_forget()
  new_game_animation()

  
def load_game():
  #loads a previous game
  global input_user_load,input_pass_load,orb_currency,orb_increase,upgrade_speed_price,upgrade_healthorb_price,healing_orb_heal,speed,enemy_damage,enemy_speed,username,password,color
  fileFound=False
  #gets user inputs
  user_try = input_user_load.get()
  pass_try = input_pass_load.get()
  try:
    #checks if files user exists
    file = open(user_try+".txt","r")
    content = file.read()
    #if file exists fileFound = True
    fileFound = True
  except: FileNotFoundError
    #if the file dosent exist the user is incorrect
  invalid_username_label.place(x=100,y=55)


  if fileFound == True:
    invalid_username_label.place_forget()
    #splits all of the information
    find_pass = content.split("!")[0]
    find_orb_currency= content.split("£")[0]
    find_orb_increase= content.split("$")[0]
    find_upgrade_speed_price= content.split("%")[0]
    find_upgrade_healthorb_price= content.split("^")[0]
    find_healing_orb_heal= content.split("&")[0]
    find_speed= content.split("*")[0]
    find_enemy_damage= content.split("(")[0]
    find_enemy_speed= content.split(")")[0]
    find_player_color = content.split("-")[0]

    username = content[0:len(find_pass)]
    password = content[(len(find_pass)+1):len(find_orb_currency)]
    if pass_try != password:
      #checking if password is correct from the file with correct user
      invalid_password_label.place(x=100,y=105)
      return
    orb_currency = content[(len(find_orb_currency)+1):len(find_orb_increase)]
    orb_increase = content[(len(find_orb_increase)+1):len(find_upgrade_speed_price)]
    upgrade_speed_price =content[(len(find_upgrade_speed_price)+1):len(find_upgrade_healthorb_price)]
    upgrade_healthorb_price =content[(len(find_upgrade_healthorb_price)+1):len(find_healing_orb_heal)]
    healing_orb_heal=content[(len(find_healing_orb_heal)+1):len(find_speed)]
    speed = content[(len(find_speed)+1):len(find_enemy_damage)]
    enemy_damage = content[(len(find_enemy_damage)+1):len(find_enemy_speed)]
    enemy_speed = content[(len(find_enemy_speed)+1):len(find_player_color)]
    color = content[(len(find_player_color)+1):len(content)]
    canvas_loadgame.pack_forget()
    game_start()
    orb_currency = int(orb_currency)
    orb_increase = int(orb_increase)
    upgrade_speed_price = int(upgrade_speed_price)
    upgrade_healthorb_price = int(upgrade_healthorb_price)
    healing_orb_heal = int(healing_orb_heal)
    speed = int(speed)
    enemy_damage = int(enemy_damage)
    enemy_speed = int(enemy_speed)
    update_all()
    game_enter_transition_animation()
    return username,password

def exit_():
  #leave the game and save
  save_function()
  exit()

def save_function():
  #saves the game by updating information
  global input_user,input_pass,orb_currency,orb_increase,upgrade_speed_price,upgrade_healthorb_price,healing_orb_heal,speed,enemy_damage,enemy_speed,username,password,color
  file = open(username+".txt","w")
  file.write(username+"!"+password+"£"+str(orb_currency)+"$"+str(orb_increase)+"%"+str(upgrade_speed_price)+"^"+str(upgrade_healthorb_price)+"&"+str(healing_orb_heal)+"*"+str(speed)+"("+str(enemy_damage)+")"+str(enemy_speed)+"-"+color)
  file.close()


def Leaderboard_button():
  #takes user to leaderboard
  canvas_mainmenu.pack_forget()
  canvas_leaderboard.pack()

def back_to_mainmenu():
  #takes user back to mainmenu
  canvas_leaderboard.pack_forget()
  canvas_newgame.pack_forget()
  canvas_loadgame.pack_forget()
  canvas_mainmenu.pack(pady = 20)


def teleporting_orb_function():
  #the function for the teleporting orb which will randomly place the player
  global teleporting_orb_state
  x = random.randint(1,450)
  y = random.randint(1,250)
  canvas_game.moveto(player,x,y)




#all of the color picking functions

def orignal_player():
  global color
  color = "grey4"
  canvas_game.itemconfig(player,fill=color)
def yellow_player():
  global color
  color = "yellow"
  canvas_game.itemconfig(player,fill=color)
def blue_player():
  global color
  color = "blue"
  canvas_game.itemconfig(player,fill=color)
def green_player():
  global color
  color = "green"
  canvas_game.itemconfig(player,fill=color)
def orange_player():
  global color
  color = "orange"
  canvas_game.itemconfig(player,fill=color)
def go_to_customize_canvas():
  canvas_shop.pack_forget()
  canvas_customize.pack()
  
def back_to_shop_canvas():
  canvas_customize.pack_forget()
  canvas_shop.pack()
#*******************************
#canvas game objects

#the player
player =canvas_game.create_oval(12,12,50,50,fill = color,outline = "white")

#the enemy
enemy = canvas_game.create_oval(12,12,45,45,fill ="red",outline = "black")
canvas_game.move(enemy,100,200)

#all of the border*********
left_border = canvas_game.create_rectangle(12,12,20,290,fill ="grey5")
canvas_game.move(left_border,-20,0)

right_border = canvas_game.create_rectangle(12,12,20,360,fill ="grey5")
canvas_game.move(right_border,470,0)

top_border = canvas_game.create_rectangle(12,12,500,22.5,fill = "grey5")
canvas_game.move(top_border,-12,-21)

bottom_border = canvas_game.create_rectangle(12,12,470,22.5,fill = "grey5")
canvas_game.move(bottom_border,-0.5,268)
#************************



orb = canvas_game.create_oval(12,12,25,25,fill = "darkblue",outline = "white")

healing_orb = canvas_game.create_oval(12,12,35,35,fill = "green",outline = "white")

teleporting_orb = canvas_game.create_rectangle(12,12,30,30,fill = "purple",outline = "white")


#***************************
#UI visuals

#placeholder for the health
Health_placeholder = canvas_UI.create_rectangle(12,12,202,50,fill = "grey5",outline = "white")
canvas_UI.move(Health_placeholder,-9,-9)

#the amount of health displayed graphically
Health = canvas_UI.create_rectangle(12,12,200,47.5,fill = "green")
canvas_UI.move(Health,-8,-8)

#the sign to show orb
orb_visual = canvas_UI.create_oval(12,12,50,50,fill ="darkblue",outline = "white")
canvas_UI.moveto(orb_visual,380,1.5)

#the amount of orb you have
orb_amount = Label(canvas_UI,text = orb_currency,font=("Times New Roman",20),bg = "grey5",foreground="white")
orb_amount.place(x = 420,y = 5)


#******************************
#canvas button

#button to go to shop
shop_button = Button(canvas_buttons,text = "SHOP",font =("Times New Romas",10),bg = "grey5",highlightbackground="white",fg = "white",width = 9,command = Game_Shop_Button,cursor = "dot")
shop_button.place(x=4.5,y=2)

#button to save
save_button = Button(canvas_buttons,text = "SAVE",font =("Times New Romas",10),bg = "grey5",highlightbackground="white",fg = "white",width = 9,cursor = "dot",command=save_function)
save_button.place(x=4.5,y=35)

#button to leave
leave_button = Button(canvas_buttons,text = "LEAVE",font =("Times New Romas",10),bg = "grey5",highlightbackground="white",fg = "white",width = 9,cursor = "dot",command=exit_)
leave_button.place(x=4.5,y=68)


#information of the player
Player_speed = Label(canvas_buttons,text = "SPEED:"+str(speed),font =("Times New Romas",10),bg = "grey5",highlightbackground="white",fg = "white",cursor = "dot")
Player_speed.place(x=4.5,y=100)

Health_orb_amount = Label(canvas_buttons,text = "HEALTHORB:"+str(healing_orb_heal),font =("Times New Romas",10),bg = "grey5",highlightbackground="white",fg = "white",cursor = "dot")
Health_orb_amount.place(x=4.5,y=120)

orb_amount_increase = Label(canvas_buttons,text = "ORB:"+str(orb_increase),font =("Times New Romas",10),bg = "grey5",highlightbackground="white",fg = "white",cursor = "dot")
orb_amount_increase.place(x=4.5,y=140)


#button to take player to the next level
Next_level_button = Button(canvas_buttons,text = "NEXT LEVEL",font =("Times New Romas",10),bg = "grey5",highlightbackground="white",fg = "white",width = 9,cursor = "dot",command=next_level_button)
Next_level_button.place(x=4.5,y=295)


#***********************************
#canvas shop
design_pattern1 = canvas_shop.create_line(0,12,600,12,fill = "white",width = 20)
canvas_shop.moveto(design_pattern1,-20,-10)

design_pattern2 = canvas_shop.create_line(0,12,600,12,fill = "white",width = 20)
canvas_shop.moveto(design_pattern2,-20,25)

design_pattern3 = canvas_shop.create_line(0,12,600,12,fill = "white",width = 20)
canvas_shop.moveto(design_pattern3,-20,60)


shop_label = Label(canvas_shop,text = "SHOP",font=("Times New Roman",30),bg = "black",fg = "white")
shop_label.place(x=225,y=10)


orb_visual_shop = canvas_shop.create_oval(12,12,50,50,fill ="darkblue",outline = "white")
canvas_shop.moveto(orb_visual_shop,500,1.5)

orb_amount_shop = Label(canvas_shop,text = orb_currency,font=("Times New Roman",20),bg = "grey5",foreground="white")
orb_amount_shop.place(x = 535,y = 5)

leave_button_shop = Button(canvas_shop,text = "LEAVE",font =("Times New Romas",10),bg = "grey5",highlightbackground="white",fg = "white",width = 10,command=Shop_toGame_button,cursor = "dot")
leave_button_shop.place(x=0,y=295)



upgrade_speed_button = Button(canvas_shop,text = "UPGRADE SPEED",font=("Times New Roman",10),bg= "grey5",highlightbackground="white",fg="white",cursor = "dot",command=upgrade_speed_button)
upgrade_speed_button.place(x=35,y=100)

upgrade_speed_button_label = Label(canvas_shop,text = str(upgrade_speed_price)+"-ORB\nUpgrades the\n speed of the \nplayer",font=("Times New Roman",10),highlightbackground="white",fg = "white",bg = "grey6")
upgrade_speed_button_label.place(x=60,y=140)




upgrade_healthOrb_button = Button(canvas_shop,text = "UPGRADE HEALTHORB",font=("Times New Roman",10),bg= "grey5",highlightbackground="white",fg="white",cursor = "dot",command=upgrade_health_orb)
upgrade_healthOrb_button.place(x=200,y=100)

upgrade_healthOrb_button_label = Label(canvas_shop,text = str(upgrade_healthorb_price)+"-ORB\nUpgrades the health the\n health-orbs gives",font=("Times New Roman",10),highlightbackground="white",fg = "white",bg = "grey6")
upgrade_healthOrb_button_label.place(x=215,y=140)




heal_button = Button(canvas_shop,text = "HEAL",font=("Times New Roman",10),bg= "grey5",highlightbackground="white",fg="white",cursor = "dot",command=heal_button)
heal_button.place(x=420,y=100)

heal_button_label = Label(canvas_shop,text = "10-ORB\n Heal player",font=("Times New Roman",10),highlightbackground="white",fg = "white",bg = "grey6")
heal_button_label.place(x=415,y=140)

Customize_button = Button(canvas_shop,text = "CUSTOMIZE",font=("Times New Roman",10),bg= "grey5",highlightbackground="white",fg="white",cursor = "dot",command = go_to_customize_canvas,width = 10)
Customize_button.place(x=480,y=295)

#****************************************
#the label for the text engine
text1 = Label(canvas_text,text = "",font=("Times New Roman",12),bg = "black")
#text1.place(x=5,y=0)

text2 = Label(canvas_text,text = "",font=("Times New Roman",12),bg = "black")
#text2.place(x=5,y=30)

text3 = Label(canvas_text,text = "",font=("Times New Roman",12),bg = "black")
#text3.place(x=5,y=60)

text4 = Label(canvas_text,text = "",font=("Times New Roman",12),bg = "black")
#text4.place(x=5,y=90)

text5 = Label(canvas_text,text = "",font=("Times New Roman",12),bg = "black")
#text5.place(x=5,y=120)

text6 = Label(canvas_text,text = "",font=("Times New Roman",12),bg = "black")
#text6.place(x=5,y=150)

text7 = Label(canvas_text,text = "",font=("Times New Roman",12),bg = "black")
#text7.place(x=5,y=180)

text8 = Label(canvas_text,text = "",font=("Times New Roman",12),bg = "black")
#text8.place(x=5,y=210)

text9 = Label(canvas_text,text = "",font=("Times New Roman",12),bg = "black")
#text9.place(x=5,y=240)

text10 = Label(canvas_text,text = "",font=("Times New Roman",12),bg = "black")
#text10.place(x=5,y=270)

triangle = canvas_text.create_polygon(25,27.5,30,17.5,17.5,17.5,fill = "grey10")
canvas_text.itemconfig(triangle,state = "hidden")

game_transition = canvas_text.create_arc(12,12,685,685,fill = "white",extent = 359.99999999999,outline = "white")
canvas_text.move(game_transition,-85,-200)
canvas_text.itemconfig(game_transition,state = "hidden")

#************************************
#canvas mainmenu objects

New_game_button = Button(canvas_mainmenu,text = "NEW GAME",font=("Times New Roman",10),bg= "grey5",highlightbackground="white",fg="white",cursor = "dot",width = 10,command=new_game_button)
New_game_button.pack(pady = 1)

Load_game_button = Button(canvas_mainmenu,text = "LOAD GAME",font=("Times New Roman",10),bg= "grey5",highlightbackground="white",fg="white",cursor = "dot",width = 10,command=load_game_button)
Load_game_button.pack(pady = 1)

Leaderboard_game_button = Button(canvas_mainmenu,text = "SCORES",font=("Times New Roman",10),bg= "grey5",highlightbackground="white",fg="white",cursor = "dot",width = 10,command=Leaderboard_button)
Leaderboard_game_button.pack(pady = 1)

Leave_game_button = Button(canvas_mainmenu,text = "EXIT GAME",font=("Times New Roman",10),bg= "grey5",highlightbackground="white",fg="white",cursor = "dot",width = 10,command=exit)
Leave_game_button.pack(pady = 1)
#*************************************
#canvas new game objects
Label_newgame = Label(canvas_newgame,text = "NEW GAME",font=("Times New Roman",15),bg="grey5",highlightbackground="white",fg="white",underline = True)
Label_newgame.place(x=5,y=3)

Label_username = Label(canvas_newgame,text = "INPUT A NEW USERNAME:",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white")
Label_username.place(x=5,y=30)

invalid_username_label_new= Label(canvas_newgame,text = "INVALID USERNAME",font=("Times New Roman",10),bg="grey4",highlightbackground="white",fg="dark red")

input_user = Entry(canvas_newgame,width = 10)
input_user.focus_set()
input_user.place(x=5,y=55)

Label_password = Label(canvas_newgame,text = "INPUT A NEW PASSWORD:",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white")
Label_password.place(x=5,y=80)

input_pass = Entry(canvas_newgame,width = 10)
input_pass.focus_set()
input_pass.place(x=5,y=105)

invalid_password_label_new = Label(canvas_newgame,text = "INVALID PASSWORD",font=("Times New Roman",10),bg="grey4",highlightbackground="white",fg="dark red")
#invalid_password_label_new.place(x=100,y=105)



Submit_button_newgame = Button(canvas_newgame,text = "SUBMIT",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white",command=new_game_create)
Submit_button_newgame.place(x=5,y=130)

Newgame_back_button = Button(canvas_newgame,text = "BACK",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white",command=back_to_mainmenu)
Newgame_back_button.place(x=2.5,y=295)

#***************************************
#load game objects
Label_loadgame = Label(canvas_loadgame,text = "LOAD GAME",font=("Times New Roman",15),bg="grey5",highlightbackground="white",fg="white",underline = True)
Label_loadgame.place(x=5,y=3)

Label_username = Label(canvas_loadgame,text = "INPUT YOUR USERNAME:",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white")
Label_username.place(x=5,y=30)

input_user_load = Entry(canvas_loadgame,width = 10)
input_user_load.place(x=5,y=55)

invalid_username_label = Label(canvas_loadgame,text = "INVALID USERNAME",font=("Times New Roman",10),bg="grey4",highlightbackground="white",fg="dark red")
#invalid_username_label.place(x=100,y=55)


Label_password = Label(canvas_loadgame,text = "INPUT YOUR PASSWORD:",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white")
Label_password.place(x=5,y=80)

invalid_password_label = Label(canvas_loadgame,text = "INVALID PASSWORD",font=("Times New Roman",10),bg="grey4",highlightbackground="white",fg="dark red")
#invialid_password_label.place(x=100,y=105)

input_pass_load = Entry(canvas_loadgame,width = 10)
input_pass_load.place(x=5,y=105)



Submit_button_loadgame = Button(canvas_loadgame,text = "SUBMIT",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white",command=load_game)
Submit_button_loadgame.place(x=5,y=130)

Loadgame_back_button = Button(canvas_loadgame,text = "BACK",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white",command=back_to_mainmenu)
Loadgame_back_button.place(x=2.5,y=295)







#**************************************
#canvas leaderboard

Label_Leaderboard = Label(canvas_leaderboard,text = "LEADER BOARD",font=("Times New Roman",20),bg="grey5",highlightbackground="white",fg="white")
Label_Leaderboard.place(x=175,y=5)


Scores_back_button = Button(canvas_leaderboard,text = "BACK",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white",command=back_to_mainmenu)
Scores_back_button.place(x=2.5,y=295)


Label_orbs_1 = Label(canvas_leaderboard,text = "1. Uday-1,000,000 ORBS",font=("Times New Roman",15),bg="grey5",fg="white")

Label_orbs_1.place(x=5,y=70)

Label_orbs_2 = Label(canvas_leaderboard,text = "2.",font=("Times New Roman",15),bg="grey5",fg="white")

Label_orbs_2.place(x=5,y=100)

Label_orbs_3 = Label(canvas_leaderboard,text = "3.",font=("Times New Roman",15),bg="grey5",fg="white")

Label_orbs_3.place(x=5,y=130)

Label_orbs_4 = Label(canvas_leaderboard,text = "4.",font=("Times New Roman",15),bg="grey5",fg="white")

Label_orbs_4.place(x=5,y=160)

Label_orbs_5 = Label(canvas_leaderboard,text = "5.",font=("Times New Roman",15),bg="grey5",fg="white")

Label_orbs_5.place(x=5,y=190)

#************************************
#canvas customize

canvas_customize_label = Label(canvas_customize,text = "CUSTOMIZE",font=("Times New Roman",25))
canvas_customize_label.place(x=175,y=5)

player_model_placeholder = canvas_customize.create_rectangle(12,12,105,105,fill = "white",outline = "grey2")
canvas_customize.moveto(player_model_placeholder,50,65)

player_model = canvas_customize.create_oval(12,12,100,100,fill = "grey5",outline = "white")
canvas_customize.moveto(player_model,53,68)

orignal_button = Button(canvas_customize,text = "CHOOSE",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white",command=orignal_player)

orignal_button.place(x=53,y=160)


player_model_placeholder2 = canvas_customize.create_rectangle(12,12,105,105,fill = "white",outline = "grey2")
canvas_customize.moveto(player_model_placeholder2,150,65)

player_model_yellow = canvas_customize.create_oval(12,12,100,100,fill = "yellow",outline = "white")
canvas_customize.moveto(player_model_yellow,153,68)

button_yellow = Button(canvas_customize,text = "CHOOSE",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white",command=yellow_player)

button_yellow.place(x=153,y=160)

player_model_placeholder3 = canvas_customize.create_rectangle(12,12,105,105,fill = "white",outline = "grey2")
canvas_customize.moveto(player_model_placeholder3,250,65)

player_model_blue = canvas_customize.create_oval(12,12,100,100,fill = "blue",outline = "white")
canvas_customize.moveto(player_model_blue,253,68)

button_blue = Button(canvas_customize,text = "CHOOSE",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white",command=blue_player)

button_blue.place(x=253,y=160)

player_model_placeholder4 = canvas_customize.create_rectangle(12,12,105,105,fill = "white",outline = "grey2")
canvas_customize.moveto(player_model_placeholder4,350,65)

player_model_green = canvas_customize.create_oval(12,12,100,100,fill = "green",outline = "white")
canvas_customize.moveto(player_model_green,353,68)

button_green = Button(canvas_customize,text = "CHOOSE",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white",command=green_player)

button_green.place(x=353,y=160)

player_model_placeholder5 = canvas_customize.create_rectangle(12,12,105,105,fill = "white",outline = "grey2")
canvas_customize.moveto(player_model_placeholder5,450,65)

player_model_orange = canvas_customize.create_oval(12,12,100,100,fill = "orange",outline = "white")
canvas_customize.moveto(player_model_orange,453,68)

button_orange = Button(canvas_customize,text = "CHOOSE",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white",command=orange_player)

button_orange.place(x=453,y=160)

button_back_customize = Button(canvas_customize,text = "BACK",font=("Times New Roman",10),bg="grey5",highlightbackground="white",fg="white",command = back_to_shop_canvas)
button_back_customize.place(x=0,y=295)


#canvas_customize.pack()

canvas_mainmenu.pack(pady = 20)
