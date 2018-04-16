from gamelib import *

game=Game(1280,720, "Eternal Darkness")

bk=Image("background.png",game)
game.setBackground(bk)
bk.resizeTo(1280,720)

#TITLE
ed = Image('Eternal-Darkness.png', game)
ed.y-=100


#HOW TO PLAY
htp = Image("How-To-Play.png", game)
key=Image("kb.png",game)

#STORY
story = Image("Story.png", game)
story.y+=100

ts = Image("TS.png", game)
ts.y+=100
#PLAY
play = Image("Play.png", game)
play.y+=200

#Hero
hero=Animation("herorun.png",12,game,487/12,40)
hero.stop()
heror=Animation("herorunright.png",12,game,487/12,40)
heror.stop()
heros=Animation("hero-shoot.png",10,game,471/10,48)
heros.stop()
herosr=Animation("hero-shootr.png",10,game,471/10,48)
herosr.stop()


#CONTAINMENT ZONE
cont=Image("containement.png",game)
cont.moveTo(1061,168)

#Zombies
zombies=[]
for index in range(50):
    zombies.append(Animation("zimbie-walk.png",3,game,80/3,46))
    x=randint(-10,1290)
    y=randint(-10,730)
    zombies[index].moveTo(x,y)

zombiew1=[]
for index in range(15):
    zombiew1.append(Animation("zimbie-walk.png",3,game,80/3,46))
    x=randint(-10,1290)
    y=randint(-10,730)
    zombiew1[index].moveTo(x,y)

minions=[]
for index in range(5):
    minions.append(Animation("zimbie-walk.png",3,game,80/3,46))
    x=randint(-10,1290)
    y=randint(-10,730)
    minions[index].moveTo(x,y)

minions2=[]
for index in range(6):
    minions2.append(Animation("zimbie-walk.png",3,game,80/3,46))
    x=randint(-10,1290)
    y=randint(-10,730)
    minions2[index].moveTo(x,y)

minions3=[]
for index in range(7):
    minions3.append(Animation("zimbie-walk.png",3,game,80/3,46))
    x=randint(-10,1290)
    y=randint(-10,730)
    minions3[index].moveTo(x,y)

minions4=[]
for index in range(8):
    minions4.append(Animation("zimbie-walk.png",3,game,80/3,46))
    x=randint(-10,1290)
    y=randint(-10,730)
    minions4[index].moveTo(x,y)


#Bullet
bullet=Image("bullet.png",game)
bullet.resizeBy(-90)
bullet.visible=False
bulletl=Image("bulletl.png",game)
bulletl.resizeBy(-90)
bulletl.visible=False

#BOSS
boss=Animation("boss.png",9,game,561/9,66)
boss.stop()
boss.resizeBy(150)
bossr=Animation("bossr.png",9,game,561/9,66)
bossr.stop()
bossr.resizeBy(150)
slapr=Animation("slapr.png",6,game,384/6,58)
slapr.stop()
slapr.resizeBy(150)
slapl=Animation("slapl.png",6,game,378/6,59)
slapl.stop()
slapl.resizeBy(150)
plasma=Animation("plasmaball2.png",10,game,640/10,64)

#Sounds
gun=Sound("Gun.wav",1)
ZombieDie=Sound("ZombieDie.wav",2)

#TITLE SCREEN
while not game.over:
    game.processInput()
    
    bk.draw()
    ed.draw()
    htp.draw()
    story.draw()
    play.draw()
    key.draw()
    ts.draw()
    key.visible=False
    ts.visible= False

    if play.collidedWith(mouse)and mouse.LeftClick:
        game.over=True
    if htp.collidedWith(mouse,"rectangle"):
        key.visible=True

    if story.collidedWith(mouse,"rectangle"):
        ts.visible=True
    
    game.update(30)

game.over=False
#LEVEL 1 GAME LOOP
x = hero.x
y = hero.y
status = "walkleft"

zombiesContained=0
while not game.over:
    game.processInput()
    bk.draw()
    cont.draw()

    for index in range(50):
        zombies[index].moveTowards(hero,2.5)
        if zombies[index].collidedWith(cont):
            zombies[index].moveTo(1061,168)
            zombiesContained+=1
            zombies[index].visible=False
        if zombies[index].collidedWith(hero):
            hero.health -=5

    if zombiesContained>=50:
        game.over=True
    print(zombiesContained)

   
    #Hero Controls
    if status == "walkright":
        heror.draw()
    if status == "walkleft" :
        hero.draw()
    if keys.Pressed[K_a]:
        hero.moveTo(x,y)
        hero.nextFrame()
        hero.visible=True
        x -=4
        status = "walkleft"
    elif keys.Pressed[K_d]:
        heror.moveTo(x,y)
        heror.nextFrame()
        hero.moveTo(heror.x,heror.y)
        hero.visible=False
        x +=4
        status = "walkright"
    if keys.Pressed[K_w]:
        hero.moveTo(x,y)
        hero.nextFrame()
        hero.visible=True
        y -=4
        status = "walkleft"
    elif keys.Pressed[K_s]:
        heror.moveTo(x,y)
        heror.nextFrame()
        hero.moveTo(heror.x,heror.y)
        hero.visible=False
        y +=4
        status = "walkright"


      

    if hero.health<=0:
        game.over = True
    game.drawText("Health: " + str(hero.health),hero.x, hero.y + 50)



    game.update(30)
  
game.over=False
#LEVEL2 GAME LOOP
zombiesw1=0
x = hero.x
y = hero.y
status = "walkleft"
while not game.over:
    game.processInput()
    bk.draw()
    cont.draw()

    bulletl.move()
    bullet.move()
    
        

        #Hero Controls
    if keys.Pressed[K_a]:
        hero.moveTo(x,y)
        hero.nextFrame()
        hero.visible=True
        x -=4
        status = "walkleft"
    elif keys.Pressed[K_d]:
        heror.moveTo(x,y)
        heror.nextFrame()
        hero.moveTo(heror.x,heror.y)
        hero.visible=False
        x +=4
        status = "walkright"
    else:
        if status == "walkleft" and keys.Pressed[K_SPACE]:
            heros.moveTo(x,y)
            heros.nextFrame()
            bulletl.moveTo(x, y)
            bulletl.setSpeed(24,90)
            bulletl.visible = True
            gun.play()
        elif status == "walkleft" :
            hero.draw()
        if status == "walkright" and keys.Pressed[K_SPACE]:
            herosr.moveTo(x,y)
            herosr.nextFrame()
            bullet.moveTo(x,y)
            bullet.setSpeed(24,270)
            bullet.visible=True
            gun.play() 
        elif status == "walkright":
            heror.draw()
        if keys.Pressed[K_w]:
            hero.moveTo(x,y)
            hero.nextFrame()
            hero.visible=True
            y -=4
            status = "walkleft"
        elif keys.Pressed[K_s]:
            heror.moveTo(x,y)
            heror.nextFrame()
            hero.moveTo(heror.x,heror.y)
            hero.visible=False
            y +=4
            status = "walkright"

    #Zombie Control
    for index in range(15):
        zombiew1[index].moveTowards(hero,2)
        if zombiew1[index].collidedWith(hero):
            hero.health -=5
        if bullet.collidedWith(zombiew1[index]) or bulletl.collidedWith(zombiew1[index]):
            zombiew1[index].health-=100
            bullet.visible=False
            bulletl.visible=False
            zombiesw1+=1
            ZombieDie.play()
        if zombiew1[index].health<=0:
            zombiew1[index].visible=False
    if zombiesw1>=15:
        game.over=True
    print(zombiesw1)
        
        
    if hero.health<=0:
        game.over = True
    game.drawText("Health: " + str(hero.health),hero.x, hero.y + 50)



    game.update(30)
    

#LEVEL 3
game.over=False
x = hero.x
y = hero.y
status = "walkleft"
invincible = False
miniondead = 0
miniondead2 = 0
miniondead3 = 0
miniondead4 = 0
hero.health=1000
while not game.over:
    game.processInput()
    bk.draw()

    bulletl.move()
    bullet.move()
    plasma.forward(8)
    plasma.move()
    

    boss.draw()
    
    if (bullet.collidedWith(boss) or bulletl.collidedWith(boss)) and not invincible:
        boss.health-=5
        bullet.visible=False
        bulletl.visible=False
    if boss.health<=0:
        game.over=True

    game.drawText("Boss Health: " + str(boss.health),boss.x,boss.y)

 


        

    if boss.health<=80 and boss.health > 60:
        if miniondead == 0:
            invincible = True
        for index in range(5):
            minions[index].moveTowards(hero,2)
            if minions[index].collidedWith(hero):
                hero.health -=5
            if bullet.collidedWith( minions[index]) or bulletl.collidedWith( minions[index]):
                 minions[index].visible=False
                 bullet.visible=False
                 bulletl.visible=False
                 miniondead+=1
                 ZombieDie.play()
        
        if miniondead >= 5:
            invincible = False
            
                


    if boss.health<=60 and boss.health > 40:
        if miniondead2 == 0:
            invincible = True
        for index in range(6):
            minions2[index].moveTowards(hero,2)
            if minions2[index].collidedWith(hero):
                hero.health -=5
            if bullet.collidedWith( minions2[index]) or bulletl.collidedWith( minions2[index]):
                 minions2[index].visible=False
                 bullet.visible=False
                 bulletl.visible=False
                 miniondead2+=1
                 ZombieDie.play()
                 
        
        if miniondead2 >= 6:
            invincible = False
                
    '''
    if boss.health<=40:
        if miniondead3 == 0:
            invincible = True
        for index in range(7):
            minions3[index].moveTowards(hero,2)
            if minions3[index].collidedWith(hero):
                hero.health -=5
            if bullet.collidedWith( minions3[index]) or bulletl.collidedWith( minions3[index]):
                 minions3[index].visible=False
                 bullet.visible=False
                 bulletl.visible=False
                 miniondead3 += 1
                 ZombieDie.play()

        if miniondead3 >= 7:
            invincible = False

    if boss.health<=20:
        for index in range(8):
            minions4[index].moveTowards(hero,2)
            if minions4[index].collidedWith(hero):
                hero.health -=5
            if bullet.collidedWith( minions4[index]) or bulletl.collidedWith( minions4[index]):
                 minions4[index].health-=100
                 bullet.visible=False
                 bulletl.visible=False
            if  minions4[index].health<=0:
                minions4[index].visible=False
        
    '''
    if plasma.collidedWith(hero) or plasma.collidedWith(heror):
        hero.health-=10
        
    if plasma.isOffScreen() or plasma.collidedWith(hero) or plasma.collidedWith(heror):
        plasma.moveTo( boss.x, boss.y )
        a = boss.angleTo(hero)
        plasma.rotateTo(a)   

        #Hero Controls
    if keys.Pressed[K_a]:
        hero.moveTo(x,y)
        hero.nextFrame()
        hero.visible=True
        x -=4
        status = "walkleft"
    elif keys.Pressed[K_d]:
        heror.moveTo(x,y)
        heror.nextFrame()
        hero.moveTo(heror.x,heror.y)
        hero.visible=False
        x +=4
        status = "walkright"
    else:
        if status == "walkleft" and keys.Pressed[K_SPACE]:
            heros.moveTo(x,y)
            heros.nextFrame()
            bulletl.moveTo(x, y)
            bulletl.setSpeed(24,90)
            bulletl.visible = True
            gun.play()
        elif status == "walkleft" :
            hero.draw()
        if status == "walkright" and keys.Pressed[K_SPACE]:
            herosr.moveTo(x,y)
            herosr.nextFrame()
            bullet.moveTo(x,y)
            bullet.setSpeed(24,270)
            bullet.visible=True
            gun.play()
        elif status == "walkright":
            heror.draw()
        if keys.Pressed[K_w]:
            hero.moveTo(x,y)
            hero.nextFrame()
            hero.visible=True
            y -=4
            status = "walkleft"
        elif keys.Pressed[K_s]:
            heror.moveTo(x,y)
            heror.nextFrame()
            hero.moveTo(heror.x,heror.y)
            hero.visible=False
            y +=4
            status = "walkright"

        game.drawText("Health: " + str(hero.health),hero.x, hero.y + 50)

        if hero.health<=0:
            game.over=True

    game.update(30)
game.quit()
