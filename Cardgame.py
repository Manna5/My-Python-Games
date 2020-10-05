from random import randint,choice

hand=[0,0,0,11]
playing=True
score=0

message="""
You currently have {} points.
When you have 42 points, you will win the game.
There is four cards in your hand:
{}
Select a card that you want to use or type zero to quit: """
hypercardInfo="""
There is a [H] card in your hand.
It allows you to do a hyperjump.
When you use it your score will be set to a random number from 1 to 100,"""


def fillHand():
	global hand
	for i in range(4):
		if hand[i]==0:
			hand[i]=randint(-10,11)
			if hand[i]==11:
				hand[i]="H"
	if 0 in hand:
		fillHand()

def revokeCard(value):
	global hand
	if not value in hand:
		return False
	for i in range(4):
		if hand[i]==value:
			hand[i]=0
	return True

def displayCards():
	output=""
	for card in hand:
		if card==11:
			output+="[H]\t"
		else:
			output+="[{}]\t".format(card)
	if 11 in hand:
		output+=hypercardInfo
	return output

while playing:
	if score==42:
		print "\nYOU WIN!"
		playAgain=raw_input("Do you want to play again? [y/n] ").lower()[0]
		if playAgain=="y":
			hand=[0,0,0,11]
			score=0
		elif playAgain=="n":
			playing=False
		else:
			pass
		continue
	fillHand()
	wantToUse=raw_input(message.format(score,displayCards()))
	if wantToUse.upper()=="H":
		wantToUse=11
	conversion_error=False
	try:
		wantToUse=int(wantToUse)
	except:
		conversion_error=True
	if wantToUse==0:
		exit()
	elif not wantToUse in hand or conversion_error:
		print "You have not got this card."
		continue
	if wantToUse==11:
		score=randint(1,100)
		if score==42:
			score+=randint(-1,1)
	else:
		score+=wantToUse
	revokeCard(wantToUse)
	if wantToUse==11:
		print "You played hypercard."
	else:
		print "You played [{}].".format(wantToUse)

