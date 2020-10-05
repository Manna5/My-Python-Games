import Tkinter
from random import randint

window=Tkinter.Tk()
window.title("Flappy Bird by Manna5")
canvas=Tkinter.Canvas(width=500,height=600,bg="lightblue")
canvas.pack()

flappyHeight=300
flappyObjects=[0,0]
gameOver=False
gameOverText=0
obstaclePosition=500
obstacleHeight=300
obstacleObjects=[0,0]

def drawFlappy():
	global canvas,flappyObjects
	for i in flappyObjects:
		canvas.delete(i)
	flappyObjects[0]=canvas.create_rectangle(200,600-flappyHeight,230,600-flappyHeight-30,fill="blue")
	flappyObjects[1]=canvas.create_polygon([230,570-flappyHeight,260,585-flappyHeight,230,600-flappyHeight,230,570-flappyHeight],fill="yellow")

def drawObstacles():
	global canvas
	for i in obstacleObjects:
		canvas.delete(i)
	obstacleObjects[0]=canvas.create_rectangle(obstaclePosition,600-obstacleHeight,obstaclePosition+80,600,fill="darkgreen")
	obstacleObjects[1]=canvas.create_rectangle(obstaclePosition,0,obstaclePosition+80,600-obstacleHeight-100,fill="darkgreen")

def checkGameOver():
	global gameOver
	if flappyHeight>570 or flappyHeight<1:
		gameOver=True
	elif obstaclePosition<260 and obstaclePosition>160 and ( flappyHeight<obstacleHeight or flappyHeight>obstacleHeight+70):
		gameOver=True
	return gameOver

def animateObstacles():
	global canvas,obstaclePosition,obstacleHeight
	obstaclePosition-=1
	if obstaclePosition<(-40):
		obstaclePosition=500
		obstacleHeight=randint(100,500)
	drawObstacles()
	if not gameOver:
		window.after(10,animateObstacles)

def flappyFall():
	global flappyHeight,window,canvas,gameOverText
	flappyHeight-=2
	drawFlappy()
	if checkGameOver():
		gameOverText=canvas.create_text(100,200,text="GAME OVER\nRIGHT CLICK TO RESTART",fill="black")
		return
	window.after(12,flappyFall)

def flappyUp(event):
	global flappyHeight
	if gameOver:
		return
	flappyHeight+=25
	drawFlappy()
	
def restartGame(event):
	global flappyHeight,obstaclePosition,obstacleHeight,gameOver,gameOverText,canvas
	if gameOver:
		canvas.delete(gameOverText)
		flappyHeight=300
		gameOver=False
		obstaclePosition=500
		obstacleHeight=300
		flappyFall()
		drawObstacles()
		animateObstacles()
		window.bind("<space>",flappyUp)
		window.bind("<Button-3>",restartGame)


flappyFall()
drawObstacles()
animateObstacles()
window.bind("<space>",flappyUp)
window.bind("<Button-3>",restartGame)
window.mainloop()
