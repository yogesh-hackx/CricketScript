import sys, os, time
from pycricbuzz import Cricbuzz
import smtplib



c = Cricbuzz()
matches = c.matches()
noOfMatches = len(matches)

print("Whats your email: ")
email = input()

print("Your password")
password = input()

inProgress = 0

# it will store the message
message = ""

#creating smtp gateway
s = smtplib.SMTP('smtp.gmail.com', '587')

#creating tls for secuity
s.starttls()

s.login(email, password)

#Add features for selecting matche-types & also for checking match schedules
print("Cricket Time".center(60, '='))
print("\nMenu:-\n\n01. LiveScore\n02. Match Schedule")
menuOption = int(input())

#if the input is not 1 or 2 then an error pop up
while menuOption not in range(1,3):
	print("oops.. Please enter valid input: ")
	menuOption = int(input())

series = matches[0]['srs']
tempSeries = series


if menuOption == 1:
	for i in range(noOfMatches):
		if(matches[i]['mchstate'] == 'inprogress'):
			inProgress = 1

	if inProgress == 0:
		print("Looks like No match is going on right now...Check the schedule and come back when it starts..\n")
		
	else:

		print("\nSelect Match: ")
		print("\n"+series.center(60, '-')+"\n")
		for i in range(len(matches)):
			series = matches[i]['srs']
			if series != tempSeries:
				print("\n"+series.center(60, '-')+"\n")
				tempSeries = series

			if(matches[i]['mchstate'] == 'inprogress'):
				battingTeam = c.livescore(matches[i]['id'])['batting']['team']
				bowlingTeam = c.livescore(matches[i]['id'])['bowling']['team']
				print(str(i) + ". " + (battingTeam) + "  vs  " + (bowlingTeam))
				#message = str(i) + ". " + (battingTeam) + "  vs  " + (bowlingTeam)


		print("\nMatch ID: ", end = "  ")
		i = input()
		i = int(i)
		print("\n")

		def battingTeam():
			battingTeam = c.livescore(matches[i]['id'])['batting']['team']
			return battingTeam
		def bowlingTeam():
			bowlingTeam = c.livescore(matches[i]['id'])['bowling']['team']
			return bowlingTeam

		def batsMan1():
			try:
				batsman1 = c.livescore(matches[i]['id'])['batting']['batsman'][0]['name']
				return batsman1
			except:
				batsman1 = "W"
				return batsman1

		def batsMan2():
			try:
				batsman2 = c.livescore(matches[i]['id'])['batting']['batsman'][1]['name']
				return batsman2
			except:
				batsman2 = "w"
				return batsman2

		def bat1Runs():
			try:
				bat1runs = c.livescore(matches[i]['id'])['batting']['batsman'][0]['runs']
				return bat1runs
			except:
				return 'W'

		def bat2Runs():
			try:	
				bat2runs = c.livescore(matches[i]['id'])['batting']['batsman'][1]['runs']
				return bat2runs
			except:
				return 'W'
		def bat1Balls():
			try:
				bat1balls = c.livescore(matches[i]['id'])['batting']['batsman'][0]['balls']
				return bat1balls
			except:
				return "W"
		def bat2Balls():
			try:
				bat2balls = c.livescore(matches[i]['id'])['batting']['batsman'][1]['balls']
				return bat2balls
			except:
				return "W"

		def Bowler():
			bowler = c.livescore(matches[i]['id'])['bowling']['bowler'][0]['name']
			return bowler

		def checkScore():
			score = (c.livescore(matches[i]['id'])['batting']['score'][0]['runs'])
			return int(score)

		def checkWickets():
			wickets = (c.livescore(matches[i]['id'])['batting']['score'][0]['wickets'])
			return int(wickets)

		def checkOvers():
			overs = (c.livescore(matches[i]['id'])['batting']['score'][0]['overs'])
			return float(overs)

		lallign = 30
		rallign = 30
		callign = lallign +rallign
		clear = lambda: os.system('clear')
		battingTeam = battingTeam()
		bwlr = Bowler()

		def printUpdatedScore():
			#batTeam = battingTeam()
			chkScore = str(checkScore())
			chkWickets = str(checkWickets())
			chkOvers = str(checkOvers())
			btsMan1 = batsMan1()
			btsMan2 = batsMan2()
			bt1Runs = bat1Runs()
			bt2Runs = bat2Runs()
			bt1Balls = bat1Balls()
			bt2Balls = bat2Balls()
			if int(float(chkOvers)) == float(chkOvers):
				bwlr = Bowler()
			clear()
			print((((battingTeam + ': ' + chkScore + '/' + chkWickets +"   (" + chkOvers + " Overs)").center(callign, " ")) + (("\n  "+ btsMan1 + '* ').ljust(20, '-') + '  ' + bt1Runs + " RUNS in " + bt1Balls + " Balls" + "\n"+ ("  "+btsMan2 + "  ").ljust(20, '-') + '  ' + bt2Runs + " RUNS in " + bt2Balls + " Balls" + "\n\n"+ "  Bowler : ".ljust(20, '.')+"  "+ bwlr + "\n" )))
			if chkOvers == '50.0':
				print("Match Over...!!")
				time.sleep(4)
				exit()

		
		print((c.livescore(matches[i]['id'])['batting']['team'] + ' vs ' + c.livescore(matches[i]['id'])['bowling']['team']).center(callign, '='))
		print("")
		print((matches[i]['status']).center(callign, '-'))
		print("\n")

		if 'rain' in (matches[i]['status']):
			print("\n:(")
			exit()
		printUpdatedScore()
		while True:
			oldOvers = checkOvers()
			oldOvers1 = checkOvers()
			while oldOvers1 == oldOvers:
				oldOvers1 = checkOvers()

			printUpdatedScore()
			
			

			#sys.stdout.flush()


# if the input is 2
else:
	for i in range(noOfMatches):
		print(matches[i]['team1']['name'] +" vs "+ matches[i]['team2']['name'] +" "+ matches[i]['status'])
		message += matches[i]['team1']['name'] +" vs "+ matches[i]['team2']['name'] +" "+ matches[i]['status']+"\n"
	s.sendmail(email, email, message)
#send the mail 

s.quit()	
