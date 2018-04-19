#ZACKS inc.
#Dungeon
# Komal Zadiq SHARON CHENNNN Christos
# you are the player and your goal is to collect three parts of the key in each level to escape from a dungeon. you have to pass each level(dungenon floor) until the last floor where you face the boss.

from gamelib import*

game = Game(1000,600,"dungeon")

onmed = False
onsmall = True

#logos
logo = Image("image//logo.png",game)
logo.resizeBy(+75)

play = Image("image//play.png",game)

over = Image("image//over.png",game)

#background image 
bk = Image("image//dungeon bk.jpg",game)
bk.resizeTo(1000,600)

#hero
hero = Animation("image//knight.jpg",6,game,433/6,111, 6)
hero.resizeBy(-20)
#platform
platform = Image("image//fire floor.png",game)
platform.resizeBy(+30)
platform.moveTo(400,550)

jumping = False
landed = False
factor = 1

#small platform
small =  Image("image//fireS.png",game)
small.resizeBy(-50)
small.moveTo(800,250)

small2 =  Image("image//fireS.png",game)
small2.resizeBy(-50)
small2.moveTo(500,250)

small3 =  Image("image//fireS.png",game)
small3.resizeBy(-50)
small3.moveTo(200,250)
#spikes
spike =  Image("image//spike.jpg",game)
spike.resizeBy(50)
spike.moveTo(860,450)

spike2 =  Image("image//spike.jpg",game)
spike2.resizeBy(50)
spike2.moveTo(540,450)

spike3 =  Image("image//spike.jpg",game)
spike3.resizeBy(50)
spike3.moveTo(700,450)

spike4 =  Image("image//spike.jpg",game)
spike4.resizeBy(50)
spike4.moveTo(370,450)

spike5 =  Image("image//spike.jpg",game)
spike5.resizeBy(50)
spike5.moveTo(200,450)

#medium platform
med = Image("image//fireM.png",game)
med.resizeBy(-50)
med.moveTo(300,250)
small.setSpeed(2,90)
med.setSpeed(2,90)

#key parts
head = Image("image//key1.png",game)
body = Image("image//key2.png",game)
tail = Image("image//key3.png",game)

head.resizeBy(-50)
body.resizeBy(-50)
tail.resizeBy(-50)

head.moveTo(500,450)
body.moveTo(300,200)
tail.moveTo(800,200)

#dragon

dragon=(Animation("image\\dragon.jpg",9,game,205/3,172/3,5))
dragon.resizeBy(150)
dragon.moveTo(800,100)
dragon.setSpeed(10,90)


dragon2=(Animation("image\\dragon2.jpg",9,game,205/3,172/3,5))
dragon2.resizeBy(125)
dragon2.moveTo(100,350)
dragon2.setSpeed(9,90)

Head = []#why do you need a list?
for index in range(1):
    Head.append(Animation("image//key1.png",1,game,173/1,177/1))

for index in range(1):
    x = randint(100,280)
    y = randint(-320,-300)
    Head[index].moveTo(x, y)
    Head[index].setSpeed(4,180)
    Head[index].resizeBy(-50)

Body = []#why do you need a list?
for index in range(1):
    Body.append(Animation("image//key2.png",1,game,159/1,100/1))

for index in range(1):
    x = randint(450,600)
    y = randint(-600,-500)
    Body[index].moveTo(x, y)
    Body[index].setSpeed(4,180)
    Body[index].resizeBy(-50)


Tail = []
for index in range(1):
    Tail.append(Animation("image//key3.png",1,game,112/1,92/1))

for index in range(1):#why do you need a list?
    x = randint(750,1000)
    y = randint(-950,-800)
    Tail[index].moveTo(x, y)
    Tail[index].setSpeed(4,180)
    Tail[index].resizeBy(-50)

#story
story = Image("image//story.png",game)

#font
f= Font(yellow,24,white,"Comic sans MS")



#villains
villain1 = Animation("image//villain 1.png",4,game,380/4,256/1,10)
villain1.setSpeed(11,90)

villain2 = Animation("image//villain 1.png",4,game,380/4,256/1,10)
villain2.setSpeed(10,90)

#fire1
fire = []
for index in range(100):
    fire.append(Animation("image//fire1.png",9,game,700/9,156/1))

for index in range(100):
    x = randint(100,1000)
    y = randint(100,4000)
    fire[index].moveTo(x, -y)
    fire[index].setSpeed(6,180)

#SOUNDS
key = Sound("image//glassping.wav",1)#added sound for Key click
collision = Sound("image//collision.wav",2)#added sound for collisions
theme = Sound("image//zelda.wav",3)#added sound for theme

win = Image("image//w.jpg",game)

#TITLE SCREEN
game.over = False
hero.moveTo(500,150)
hero.resizeBy(+75)

logo.moveTo(500,275)
play.moveTo(500,375)
story.moveTo(500,475)

while not game.over:
    game.processInput()

    bk.draw()
    hero.draw()
    play.draw()
    logo.draw()
    story.draw()
    theme.play()

    if play.collidedWith(mouse) and mouse.LeftButton:
        game.over = True
    if story.collidedWith(mouse) and mouse.LeftButton:
        bk.draw()
        game.drawText("STORY:",70,90,f)
        game.drawText("YOU ARE A HERO THAT HAS BEEN PLACED IN A DUNGEON. YOUR GOAL",70,120,f)
        game.drawText("IS TO SLAY THE BOSS(THE DEVIL) IN ORDER TO ESCAPE.",70,150,f)
        game.drawText("YOU MUST PASS EACH FLOOR(LEVEL) OF THE DUNGEON TO PROGRESS.",70,200,f)
        game.drawText("TO THE NEXT. IN ORDER TO GO TO THE NEXT FLOOR, YOU MUST COLLECT",70,230,f)
        game.drawText("3 PARTS OF A KEY UNTIL YOU REACH THE LAST FLOOR: THE BOSS FLOOR ",70,260,f)
        game.drawText("IN EVERY LEVEL THERE WILL BE A DIFFERENT OBSTACLE YOU FACE.",70,310,f)
        game.drawText("YOU WILL ENCOUNTER VILLAINS THAT KEEP YOU FROM TAKING THE KEYS ",70,340,f)
        game.drawText("Use the left/right arrow to move back and forth",70,500,f)
        game.drawText("Use the up arrow to jump",70,530,f)

    game.update(60)



#level 1 game loop
game.over = False
hero.moveTo(50,470)
keypartscollected = 0
hero.resizeBy(-15)
villain1.moveTo(950,460)
lives = 50
villain2.moveTo(950,460)
villain2.visible = False

while not game.over:
    game.processInput()

    bk.draw()
    hero.draw()
    game.drawText("LEVEL ONE",10,10,f)#to make the level stand out more
    game.drawText("Collect the three key parts",10,50)#less text
    platform.draw()
    small.draw()
    med.draw()
    head.draw()
    body.draw()
    tail.draw()
    hero.draw()
    villain1.move(True)
    

    if keys.Pressed[K_RIGHT]:
       hero.x+=3

    if keys.Pressed[K_LEFT]:
       hero.x-=3

    if hero.y< 450:
        landed = False

    else:
        landed = True

    if keys.Pressed [K_UP] and landed and not jumping:
        jumping = True

    if jumping:
        hero.nextFrame()
        hero.y -=28*factor
        factor*=.95
        landed = False
    if factor < .18:
        jumping = False
        factor = 1
            
    if not landed: 
        hero.y +=3
        hero.nextFrame()

    if hero.collidedWith(head):
        head.visible = False
        keypartscollected+=1
        key.play()

    if hero.collidedWith(body):
        body.visible = False
        keypartscollected+=1
        key.play()#doesnt work?

    if hero.collidedWith(tail):
        tail.visible = False
        keypartscollected+=1
        key.play()

    if hero.collidedWith(villain1):
        lives-=3
        #villain2.move(True)
        hero.moveTo(50,470)
        villain2.moveTo(950,460)
        villain2.visible = True
        collision.play()

    villain2.move(True)

    if hero.collidedWith(villain2):
        lives-=3
        hero.moveTo(50,470)
        collision.play()
        


    game.drawText("KEY PARTS COLLECTED: " + str(keypartscollected),hero.x-50,hero.y-70,)#CAPS
    game.drawText("LIVES: " + str(lives),hero.x-50,hero.y-90,)


    if keypartscollected >=3:
        game.over = True

    if lives<=0:
        bk.draw()
        over.draw()

    game.update(60)


game.over = False

#LEVEL 2 GAME LOOP

keypartscollected = 0
scrollbk = Animation("image\scrollbk.jpg",1,game,1200/1,750/1) 
#game.setBackground(scrollbk)
hero.moveTo(50,470)
lives = 50
passable = 0

while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)had to remove
    scrollbk.draw()#to fix background issue
    game.drawText("LEVEL TWO",10,10,f)#INCREAE FONT SIZE
    game.drawText("Avoid the fire.  Dont let the keys fall off the screen",10,50)#changed wording a bit
    platform.draw()
    hero.draw()

    if keys.Pressed[K_RIGHT]:
       hero.x+=3

    if keys.Pressed[K_LEFT]:
       hero.x-=3

    if keys.Pressed[K_DOWN]:
        hero.y+=3
        
    if hero.y< 450:
        landed = False

    else:
        landed = True

    if keys.Pressed [K_UP] and landed and not jumping:
        jumping = True

    if jumping:
        hero.nextFrame()
        hero.y -=28*factor
        factor*=.95
        landed = False
    if factor < .18:
        jumping = False
        factor = 1
            
    if not landed: 
        hero.y +=3
        hero.nextFrame()

    for index in range(1):
        Head[index].move()
        Body[index].move()
        Tail[index].move()

    if Head[index].collidedWith(hero):
        Head[index].visible = False
        keypartscollected+=1
        passable +=1
        key.play()

    if Body[index].collidedWith(hero):
        Body[index].visible = False
        keypartscollected+=1
        passable +=1
        key.play()

    if Tail[index].collidedWith(hero):
        Tail[index].visible = False
        keypartscollected+=1
        passable +=1
        key.play()
    #if Head[index].isOffScreen("bottom") and Body[index].isOffScreen("bottom") and Tail[index].isOffScreen("bottom") and passable<3:#one if statement to end game.
        #over.draw()
        

#these if statements do what to the game??
    if Head[index].isOffScreen("bottom") and passable<1:
        game.setBackground(bk)
       
        over.draw()

    if Body[index].isOffScreen("bottom") and passable<2:
        game.setBackground(bk)
      
        over.draw()

    if Tail[index].isOffScreen("bottom") and passable<3:
        game.setBackground(bk)
        
        over.draw()

    for index in range(100):
        fire[index].move()
        if fire[index].collidedWith(hero):
            lives -= 5
            fire[index].visible = False
     
    game.drawText("key parts collected: " + str(keypartscollected),hero.x-50,hero.y-70)
    game.drawText("lives: " + str(lives),hero.x-50,hero.y-90)

    if keypartscollected >=3 and lives>0:#added condition of lives >0
        game.over = True

    if lives<=0:
        hero.visible = False#to stop negatvie values for lives?
        #game.setBackground(bk)took out due to background issue
       
        over.draw()
        

    game.update(60)
        
    
game.over = False

#LEVEL 3
head.moveTo(500,180)
body.moveTo(200,200)
tail.moveTo(800,200)

keypartscollected = 0
lives = 50
hero.moveTo(50,470)


head.visible = True
body.visible = True
tail.visible = True

while not game.over:
    game.processInput()

    bk.draw()
    hero.draw()
    game.drawText("LEVEL THREE",10,10,f)#changed font
    game.drawText("Avoid the Dragons and the Spikes",10,50)
    platform.draw()
    dragon.draw()
    small.draw()
    small2.draw()
    small3.draw()
    head.draw()
    body.draw()
    tail.draw()
    hero.draw()
    spike.draw()
    spike2.draw()
    spike3.draw()
    spike4.draw()
    spike5.draw()
    dragon.move(True)
    dragon2.move(True)

    if keys.Pressed[K_RIGHT]:
       hero.x+=3

    if keys.Pressed[K_LEFT]:
       hero.x-=3

    if hero.y< 450:
        landed = False

    else:
        landed = True

    if keys.Pressed [K_UP] and landed and not jumping:
        jumping = True

    if jumping:
        hero.nextFrame()
        hero.y -=28*factor
        factor*=.95
        landed = False
    if factor < .18:
        jumping = False
        factor = 1
            
    if not landed: 
        hero.y +=3
        hero.nextFrame()

    if hero.collidedWith(spike):
        lives-=5
        hero.moveTo(100,450)
        
    if hero.collidedWith(spike2):
        lives-=5
        hero.moveTo(100,450)
        
    if hero.collidedWith(spike3):
        lives-=5
        hero.moveTo(100,450)
        
    if hero.collidedWith(spike4):
        lives-=5
        hero.moveTo(100,450)
        
    if hero.collidedWith(spike5):
        lives-=5
        hero.moveTo(100,450)

    if hero.collidedWith(dragon):
        lives-=5
        hero.moveTo(100,450)

    if hero.collidedWith(dragon2):
        lives-=5
        hero.moveTo(100,450)
    
    if hero.collidedWith(head):
        head.visible = False
        keypartscollected+=1
        key.play()
        
    if hero.collidedWith(body):
        body.visible = False
        keypartscollected+=1
        key.play()
        
    if hero.collidedWith(tail):
        tail.visible = False
        keypartscollected+=1
        key.play()
    
    game.drawText("key parts collected: " + str(keypartscollected),hero.x-50,hero.y-70)
    game.drawText("lives: " + str(lives),hero.x-50,hero.y-90)


    if lives<=0:
        bk.draw()
        over.draw()

    if keypartscollected>=3:
        win.draw()
        win.resizeBy(6)
        
        
 
    game.update(60)


game.quit()
