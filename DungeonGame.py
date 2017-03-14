#Dungeon Game
#flaws
	#when waiting for raw_input, if enter is accidentally pressed the game will break

from sys import exit
from random import randint

#global variables

rooms = [] 
rooms = ['Start', '0', 'Lava', '1', 'Water', '2', 'Trophy', '3', 'Cthulu', '4', 'Nothing', '5', 'Hatter', '6', 'Key', '7', 'Escape', '8']
path = []
room_functions = []
 
def Start():
	path.append(0)
	print path
	
	map(path)
	
	print """
		You are stuck in a dungeon. It will be very difficult to get out.
		Are you excited? Well, you should be.
		You can take door 1 or door 2.
		Which do you choose?
	"""
	choice = raw_input("> ")
	door = int(choice)
	if door == 2:
		Water()
	else:
		Lava()	
		
def Lava():
	path.append(1)
	print path
	
	map(path)
 
	print """
		You have entered the Lava room. Are you ready? Well good.
		There are 2 doors on the other side.
		
		Do you:
		a) Attempt to surf across with a metal surf board
		b) Swing across via a chain. Note: you can't swing or surf back.
		c) Turn back
		d) Make a silly face
	"""
	
	#choice = raw_input("> ")
	
	while True:
		choice = raw_input("> ")
	
		if choice == "a" or choice == "A":
			print """
		You push the surf board into the lava.
		It floats, so you step on.
		You start to move. Then sink. Oh my the metal is melting!!!
		K, so, one cannot surf on a metal surfboard. That was pretty dumb.
			"""
			dead()
	
		elif choice == "b" or choice == "B":
			print """
		Do you want to grab onto the chain with your right hand which has a glove?
		Or with your left hand which is stronger?
				"""
			hand = raw_input("> ")
			if "left" in hand:
				print """
		You grab on and jump!
		You swing and then the chain tightens, jerking you!
		Lucky for you, you can climb down to the walkway.
		So the 2 Doors to choose from! 
		5 on the left or 3 on the right?
				"""

				while True:
				
					choice = raw_input("> ") #prevents and infinite loop however after going to the function we're still in the while loop
					door = int(choice)					
					
					if door == 3:
						Trophy()
					
					elif door == 5:
						Nothing()
					
					else:
						print "Ya, that's not a choice. So pick something."
						choice = raw_input("> ")
			
			elif "right" in hand:
				print """
		You swing, you jerk! Aaaaaaand your hand slips. That glove did NOT help.
		You accidentally kick a level on the wall...and now lava is seeping..everywhere..
		Gah but you're by door 5! jump! go thru! now!!!
				"""
				Nothing()
			
			
	
		elif choice == "c" or choice == "C":
			print "\t\tOkay fine, you can turn back."
			location = path[-2] 
			choice = int(location)
			print "Location: %d" % choice
			pick_a_room(choice)
		
	
		elif choice == "d" or choice == "D":
			print "\t\tSo this is what the Gods think of your silly face:"
			print "\t\tThey don't care. Pick another option."
			
		else:
			print "\t\tYa, that's not a choice. So pick something."
			choice = raw_input("> ")
		

def Water():
	
	path.append(2)
	print path
	
	map(path)
		
	print """
		You're in the Water Room!
		You can see 2 doors on 2 different walls, across the water.
		"""
	print "Your previous room location was: %d" % path[-1]
	
	limit = (len(path))-1
	
	if len(path) > 2:	
		count = 0
		for i in range(0, limit):
			if path[i+1] == 0:
				count = count + 1
			else:
				count = count
	else:
		count = 0
	
	print "Count: %d" % count
	
	if len(path)== 2 or (path[-2] == 0 and count == 1):
		print """
		Do you want to:
		a) swim
		b) dip your toe in (because you often get cold and it would be good to check)
		c) climb the ladder next to you
		"""
	else:
		print """
		Do you want to:
		a) swim
		b) dip your toe in (because you often get cold and it would be good to check)
		"""
	choice = raw_input("> ")
	water_choice(choice)
		
def water_choice(choice):
	
	if choice == "a" or choice == "A":
		print """
		You catch some turbulence out of the corner of your eye.
		A flaccid, pale, grey face emerges from the water.
		Teeth...
		Red sores...
			...another face...then a swarm...
					... the living dead...are coming.
		"""
		dead()
	elif choice == "b" or choice == "B":
		print """
		Man that water is cold. A little turbulence in the corner of the room.
		Do you take your foot out?
		"""
		answer = raw_input("> ")
		if "yes" in answer or "Yes" in answer:
			print "\t\tGooooood choice."
			print "\t\tWould you like to turn back then?"
			choice = raw_input("> ")
			if choice == "yes" or choice == "Yes":
				if path[-2] == "0" or len(path) == 2:
					pick_a_room(0)
				elif path[-2] == "3":
					pick_a_room(3)
				else:
					print "\t\tSo the door behind you is locked...and the room is flooding..."
					dead()
			else:
				water_choice("a")			
		else:
			water_choice("a")
	elif choice == "c" or choice == "C":
		print """
		You climb up the ladder next to you. Behold! A kayak. And oar.
		Lucky you. You make the wise decision of using the kayak to cross the water.
		A turbulence in the corner of the water.
		A flaccid, pale, grey face emerges from the water.
		Teeth...
		Red sores...
			...another face...then a swarm...
		
		Luckily for you, you've got an oar! Whack whack Whack! They receed into the water.
		
		Quickly now, the room is flooding! You won't be able to return!
		Do you kayak over to room 4 or to room 3?
		"""
		
		room = raw_input("> ")
		num = int(room)
		if num == 3:
			Trophy()
		elif num == 4:
			Cthulu()
		else:
			print "Listen, you were offered a chance to save yourself but...too slow."
			dead()
	else:
		print "..."	
		
def Trophy():
	path.append(3)
	print path
	
	map(path)
 
	print "\t\tYou're in the Trophy Room!"
	print "\t\tDo you want to take the Trophy or go through the Door?"
	choice = raw_input("> ")
	if "Trophy" in choice or "trophy" in choice:
		print "\t\tPrepare to warp!!!"
		rand = randint(0,8) #create a random number from 0 to 8
		print "random # %d" % rand
		pick_a_room(rand)
	elif "Door" in choice or "door" in choice:
		print "\t\tWhich door? 2, 7, 6, or 1?"
		direction = raw_input("> ")
		num = int(direction)
		pick_a_room(num)
		
 
def Cthulu():
	path.append(4)
	print path
 
	map(path)
 
	print "\t\tYou're meeting Cthulu!"
	print "\t\tGuess what! You die instantly."
	dead()
 
 
def Nothing():
	path.append(5)
	print path
 
	map(path)
 
	print "\t\tThere's Nothing interesting in this room!"
	print "\t\tEither go through door 1 or through door 6."
	
	while True:
		num = raw_input("\t\tWhich one is it? > ")
		choice = int(num)
		
		if choice == 1 or choice == 6:
			pick_a_room(choice)
		else:
			print "\t\tYou only have 2 options. Try again. 1 or 6?"
 
def Hatter():
	path.append(6)
	print path
 
	map(path)
 
	print "\t\tWelcome to the Mad Hatter and his compadres!"
	print "\t\tSo, you can a) talk to the Mad Hatter, b) sit next to the door mouse, or c) talk to the Cheshire Cat."
	
	while True:
		choice = raw_input("> ")
		if choice == "a" or choice == "A" or "hatter" in choice:
			print "\t\tTea time, tip top! Pick a color (ROYGBIV)"
			color = raw_input("> ")
			rand = randint(1, 7)
			print "\t\tTee hee hee, color doesn't matter!"
			pick_a_room(rand)
	
		elif choice == "b" or choice == "B" or "mouse" in choice:
			print "\t\tTea time, tea time!"
			print "\t\tSome advice, don't pick Red, Orange, or Green."
			print "\t\tRiddle me this riddle me that try again: mad hatter, mouse, or cat?"
	
		elif choice == "c" or choice == "C" or "cat" in choice:
			print "\t\tHow many rooms have you visited, child?"
			total = int(raw_input("> "))
			count = 0
			
			for i in range(0, len(path)):
				for j in range(0, 9):
					if path[i] == j:
						count = count + 1
					else:
						count = count

			if count == total:
				print "\t\tCorrect!"
				visit = 2*count - 4
				if visit > count:
					print "\t\tAnd guess what, you have to visit at least %d more rooms!" % (visit - count)
				elif visit <= count:
					Escape()
			
			else:
				print "\t\tFalse! I get to pick your color!"
				Start()
			
		else:
			print "\t\tRiddle me this riddle me that try again: mad hatter, mouse, or cat?"
 
 
def Key():
	path.append(7)
	print path
 
	map(path)
 
	print "\t\tGuess what! There are Keys in this room."
	print "\t\tA ruby key is hanging in the corner. You can use it on door 4 or the red chest. Which?"
	while True:
		choice = raw_input("> ")
		if "door" in choice or choice == "4":
			pick_a_room(4)
		elif "chest" in choice:
			print """
		There's a saphire key in this chest!
		It opens door 3 and the saphire chest. Which would you like to open?
			"""
			while True:
				choice = raw_input("> ")
				if "door" in choice or choice == "3":
					pick_a_room(3)
				elif "chest" in choice:
					print """
		There's an emerald key in this chest!
		It opens door 8 and the emerald chest. Which would you like to open?
				"""
					while True:
						choice = raw_input("> ")
						if "door" in choice or choice == "8":
							pick_a_room(8)
						elif "chest" in choice:
							print "\t\tThere's nothing actually in the chest...bummer. So what do you want to do?"
						else:
							print "\t\tSorry, you can't do that. What else would you like to do?"
				else:
					print "\t\tSorry, you can't do that. What else would you like to do?"		
		else:
			print "\t\tSorry, you can't do that. What else would you like to do?"
 
 
def Escape():
	path.append(8)
	print path
	
	map(path)
	
	print """
		Hot damm, you won! You've escaped! Go live your life!
		...
		...
		...
		..
		......
		No seriously,
		why are you still here?
		"""
	exit()
 
 
def dead():
	print """
		Yeah, you died. So sad.
		......
		...
		Yea, not really that sad.
		But you're dead.
	"""
	exit()

def pick_a_room(num):
	if num == 0:
		Start()
	elif num == 1:
		Lava()
	elif num == 2:
		Water()
	elif num == 3:
		Trophy()
	elif num == 4:
		Cthulu()
	elif num == 5:
		Nothing()
	elif num == 6:
		Hatter()
	elif num == 7:
		Key()
	elif num == 8:
		Escape()
	else:
		print "Your code is totes broken."


	
def map(path):

	print"\t\t ____________      ____________      ____________"
	print"\t\t|            |    |            |    |            |"
	print"\t\t|            |    |            |    |            |"
	print"\t\t|            |____|            |____|            |"
	print"\t\t|   Start     ____       %s      ____       %s     |" % (room_check(2, path), room_check(4, path)) #(rooms[5], rooms[9])
	print"\t\t|            |    |            |    |            |"
	print"\t\t|            |    |            |    |            |"
	print"\t\t|____    ____|    |____    ____|    |____    ____|"
	print"\t\t     |  |              |  |              |  |"
	print"\t\t ____|  |____      ____|  |____      ____|  |____"
	print"\t\t|            |    |            |    |            |"
	print"\t\t|            |    |            |    |            |"
	print"\t\t|            |____|            |____|            |"
	print"\t\t|     %s       ____       %s      ____       %s     |" % (room_check(1, path), room_check(3, path), room_check(7, path)) #(rooms[3], rooms[7], rooms[15])
	print"\t\t|            |    |            |    |            |"
	print"\t\t|            |    |            |    |            |"
	print"\t\t|____    ____|    |____    ____|    |____    ____|"
	print"\t\t     |  |              |  |              |  |"
	print"\t\t ____|  |____      ____|  |____      ____|  |____"
	print"\t\t|            |    |            |    |            |"
	print"\t\t|            |    |            |    |            |"
	print"\t\t|            |____|            |____|            |"
	print"\t\t|     %s       ____       %s      ____      %s      |" % (room_check(5, path), room_check(6, path), room_check(8, path))#(rooms[11], rooms[13], rooms[17])
	print"\t\t|            |    |            |    |            |"
	print"\t\t|            |    |            |    |            |"
	print"\t\t|____________|    |____________|    |____________|"

def room_check(choice, path):
	check = choice
	
	#print "check: %d " % check
	
	#for i in path(1, 1, len(path)-1):
	i = 0
	
	#print "path length: %d" % len(path)
	
	while i	< len(path):
		if path[i] == check:
			room_number = check
			#print "room # after if: %s " % room_number
			return room_number
		else:
			room_number = ' '
		#print "room # after else: %s " % room_number
		i = i + 1
		#print "i: %d" % i
	return room_number
	
	
#room_functions = [Start(), Lava(), Water(), Cthulu(), Nothing(), Hatter(), Key(), Escape()]	

Start()
