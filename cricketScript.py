import sys, os, time
from pycricbuzz import Cricbuzz
c = Cricbuzz()
matches = c.matches()
noOfMatches = len(matches)

inProgress = 0



#Add features for selecting matche-types & also for checking match schedules

print("Cricket Time".center(60, '='))
print("\nMenu:-\n\n01. LiveScore\n02. Match Schedule")
menuOption = int(input())

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


		print("\nMatch ID: ", end = "  ")
		i = input()
		i = int(i)
		print("\n")

		battingTeam = c.livescore(matches[i]['id'])['batting']['team']
		bowlingTeam = c.livescore(matches[i]['id'])['bowling']['team']

		batsman1 = c.livescore(matches[i]['id'])['batting']['batsman'][0]['name']
		batsman2 = c.livescore(matches[i]['id'])['batting']['batsman'][1]['name']

		bat1runs = c.livescore(matches[i]['id'])['batting']['batsman'][0]['runs']
		bat2runs = c.livescore(matches[i]['id'])['batting']['batsman'][1]['runs']

		bat1balls = c.livescore(matches[i]['id'])['batting']['batsman'][0]['balls']
		bat2balls = c.livescore(matches[i]['id'])['batting']['batsman'][1]['balls']

		bowler = c.livescore(matches[i]['id'])['bowling']['bowler'][0]['name']

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
		clear()
		print((c.livescore(matches[i]['id'])['batting']['team'] + ' vs ' + c.livescore(matches[i]['id'])['bowling']['team']).center(callign, '='))
		print("")
		print((matches[i]['status']).center(callign, '-'))
		print("\n")
		while True:
			oldOvers = checkOvers()
			while oldOvers == checkOvers:
				pass
			print((((battingTeam + ': ' + str(checkScore()) + '/' + str(checkWickets()) +"   (" + str(checkOvers()) + " Overs)").center(callign, " ")) + (("\n  "+batsman1 + '* ').ljust(20, '-') + '  ' + bat1runs + " RUNS in " + bat1balls + " Balls" + "\n"+ ("  "+batsman2 + "  ").ljust(20, '-') + '  ' + bat2runs + " RUNS in " + bat2balls + " Balls" + "\n\n"+ "  Bowler : ".ljust(20, '.')+"  "+ bowler + "\n" )), end = '\r')
			time.sleep(1)
			clear()
			sys.stdout.flush()

else:
	for i in range(noOfMatches):
		print(matches[i]['team1']['name'] +" vs "+ matches[i]['team2']['name'] +" "+ matches[i]['status'])

	