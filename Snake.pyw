import Tkinter
from random import randint

window=Tkinter.Tk()
window.title("Snake by Manna5")
canvas=Tkinter.Canvas(width=600,height=300,bg="white")

#Borders
canvas.create_rectangle(0,0,600,20,fill="blue",outline="blue")
canvas.create_rectangle(0,280,600,300,fill="blue",outline="blue")
canvas.create_rectangle(0,0,20,300,fill="blue",outline="blue")
canvas.create_rectangle(580,0,600,300,fill="blue",outline="blue")

snakePartCoords=[[3,3],[4,3],[5,3]]
snakePartObjects=list()
snakeDirection=3 #0=left, 1=right, 2=up, 3=down
appleBases=[]
applePos=0
appleObject=0

for i in range(25):
	ax=randint(1,27)
	ay=randint(1,12)
	appleBases.append([ax,ay])

def drawSnakePart(coords):
	global canvas
	x=coords[0]
	y=coords[1]
	return canvas.create_rectangle(x*20+20,y*20+20,x*20+40,y*20+40,fill="red")
	
def drawApple():
	global canvas,appleObject
	canvas.delete(appleObject)
	x=appleBases[applePos][0]
	y=appleBases[applePos][1]
	appleObject=canvas.create_rectangle(x*20+20,y*20+20,x*20+40,y*20+40,fill="green")

def eraseSnake():
	global canvas,snakePartObjects
	for obj in snakePartObjects:
		canvas.delete(obj)
	snakePartObjects=list()
		
def renderSnake():
	eraseSnake()
	drawApple()
	global snakePartCoords,snakePartObjects
	for i in snakePartCoords:
		snakePartObjects.append(drawSnakePart(i))

def keyPress(event):
	global snakeDirection
	event=event.char.lower()
	if event in ["q","a","o","p"]:
		if event=="q":
			print "UP"
			snakeDirection=2
		elif event=="a":
			print "DOWN"
			snakeDirection=3
		elif event=="o":
			print "LEFT"
			snakeDirection=0
		elif event=="p":
			print "RIGHT"
			snakeDirection=1
	renderSnake()
	
def checkGameOver():
	#If you want to make the snake invicible, remove these loops:
	for part in snakePartCoords:
		if part[0]>27 or part[0]<0:
			return True
		elif part[1]>12 or part[1]<0:
			return True
	for i in range(len(snakePartCoords)): #Check if snake do not touch itself
		part=snakePartCoords[i]
		if snakePartCoords.index(part)!=i:
			return True
	return False
		

def moveSnake():
	global applePos
	print "MOVE"
	snakeHead=snakePartCoords[0][:]
	if snakeDirection==0: #left
		snakeHead[0]-=1
	elif snakeDirection==1: #right
		snakeHead[0]+=1
	elif snakeDirection==2: #up
		snakeHead[1]-=1
	elif snakeDirection==3: #down
		snakeHead[1]+=1
	else:
		print "ERROR"
		return
	snakePartCoords.insert(0,snakeHead)
	if snakeHead==appleBases[applePos]:
		print "APPLE_EATED"
		applePos+=1
		if applePos>len(appleBases):
			applePos=0
	else:
		del snakePartCoords[-1] #remove tail
	if checkGameOver():
		print "GAME_OVER"
		canvas.create_text(200,100,text="GAME OVER")
		return
	renderSnake()
	window.after(500,moveSnake)
	

window.bind("<Key>",keyPress)
window.after(500,moveSnake)


canvas.pack()
window.mainloop()