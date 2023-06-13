import matplotlib.pyplot as plt
#List of every team name used to populate the names for each team in the data class
#theTeams = ["Arizona Cardinals","Atlanta Falcons","Baltimore Ravens","Buffalo Bills","Carolina Panthers","Chicago Bears",
 #   "Cincinnati Bengals","Cleveland Browns","Dallas Cowboys","Denver Broncos","Detroit Lions","Green Bay Packers",
  #  "Houston Texans","Indianapolis Colts","Jacksonville Jaguars","Kansas City Chiefs","Las Vegas Raiders",
   # "Los Angeles Chargers","Los Angeles Rams","Miami Dolphins","Minnesota Vikings","New England Patriots",
   # "New Orleans Saints","New York Giants","New York Jets","Philadelphia Eagles","Pittsburgh Steelers",
   # "San Francisco 49ers","Seattle Seahawks","Tampa Bay Buccaneers","Tennessee Titans","Washington Commanders"]
theTeams = {0:"Arizona Cardinals",1:"Atlanta Falcons",2:"Baltimore Ravens",3:"Buffalo Bills",4:"Carolina Panthers",5:"Chicago Bears",
    6:"Cincinnati Bengals",7:"Cleveland Browns",8:"Dallas Cowboys",9:"Denver Broncos",10:"Detroit Lions",11:"Green Bay Packers",
    12:"Houston Texans",13:"Indianapolis Colts",14:"Jacksonville Jaguars",15:"Kansas City Chiefs",16:"Las Vegas Raiders",
    17:"Los Angeles Chargers",18:"Los Angeles Rams",19:"Miami Dolphins",20:"Minnesota Vikings",21:"New England Patriots",
    22:"New Orleans Saints",23:"New York Giants",24:"New York Jets",25:"Philadelphia Eagles",26:"Pittsburgh Steelers",
    27:"San Francisco 49ers",28:"Seattle Seahawks",29:"Tampa Bay Buccaneers",30:"Tennessee Titans",31:"Washington Commanders"}
#dictionary of team names mapped to a number for each team
#used for parsing the game results data
teams = {"Arizona Cardinals": 0,"Atlanta Falcons":1,"Baltimore Ravens":2,"Baltimore":2,"Buffalo Bills":3,"Carolina Panthers":4,
    "Chicago Bears":5,"Cincinnati Bengals":6,"Cleveland Browns":7,"Dallas Cowboys":8,"Denver Broncos":9,
    "Detroit Lions":10,"Green Bay Packers":11,"Houston Texans":12,"Indianapolis Colts":13,"Jacksonville Jaguars":14,
    "Kansas City Chiefs":15,"Las Vegas Raiders":16,"Oakland Raiders":16,"Los Angeles Chargers":17,"Los Angeles Cargers":17,"San Diego Chargers":17,
    "Los Angeles Rams":18,"St. Louis Rams":18,"Miami Dolphins":19,"Miamai Dolphins":19,"Minnesota Vikings":20,"New England Patriots":21,
    "New Orleans Saints":22,"New York Giants":23,"New York Jets":24,"Philadelphia Eagles":25,"Pittsburgh Steelers":26,
    "San Francisco 49ers":27,"Seattle Seahawks":28,"Tampa Bay Buccaneers":29,"Tennessee Titans":30,"Washington Commanders":31,"Washington Football Team":31,
    "Washington Redskins":31}
#dictionary of team abreviations mapped to the same team number as above
#used for parsing the game lines data
abbFromNum = {0:"ARI",1:"ATL",2:"BAL",3:"BUF",4:"CAR",5:"CHI",6:"CIN",7:"CLE",8:"DAL",9:"DEN",10:"DET",11:"GB",
12:"HOU",13:"IND",14:"JAX",15:"KAN",16:"LVR",17:"LAC",18:"LAR",19:"MIA",20:"MIN",21:"NE",
22:"NO",23:"NYG",24:"NYJ",25:"PHI",26:"PIT",27:"SF",28:"SEA",29:"TB",30:"TEN",31:"WAS"}

abbreviations = {"ARI":0,"ATL":1,"BAL":2,"BUF":3,"CAR":4,"CHI":5,"CIN":6,"CLE":7,"DAL":8,"DEN":9,"DET":10,"GNB":11,
"HOU":12,"IND":13,"JAX":14,"KAN":15,"LVR":16,"OAK":16,"LAC":17,"SDG":17,"LAR":18,"STL":18,"MIA":19,"MIN":20,"NWE":21,
"NOR":22,"NYG":23,"NYJ":24,"PHI":25,"PIT":26,"SFO":27,"SEA":28,"TAM":29,"TEN":30,"WAS":31,

"@ARI":0,"@ATL":1,"@BAL":2,"@BUF":3,"@CAR":4,"@CHI":5,"@CIN":6,"@CLE":7,"@DAL":8,"@DEN":9,"@DET":10,"@GNB":11,
"@HOU":12,"@IND":13,"@JAX":14,"@KAN":15,"@LVR":16,"@OAK":16,"@LAC":17,"@SDG":17,"@LAR":18,"@STL":18,"@MIA":19,"@MIN":20,"@NWE":21,
"@NOR":22,"@NYG":23,"@NYJ":24,"@PHI":25,"@PIT":26,"@SFO":27,"@SEA":28,"@TAM":29,"@TEN":30,"@WAS":31}
#number identifiers for the days of the week in the game results data
#most games occur on Thursday, Sunday, and Monday, other days of the week are mapped to closest common day
days = {"Wed":0,"Thu":0,"Fri":0,"Sat":1,"Sun":1,"Mon":2,"Tue":2}

#Divisions are: AFC NORTH = 1 | AFC EAST   = 2 | AFC SOUTH = 3 | AFC WEST = 4
#NFC NORTH = 5 | NFC EAST = 6 | NFC SOUTH = 7 | NFC WEST = 8
divisions = {0:8,1:7,2:1,3:2,4:7,5:5,6:1,7:1,8:6,9:4,10:5,11:5,12:3,13:3,14:3,15:4,
16:4,17:4,18:8,19:2,20:5,21:2,22:7,23:6,24:2,25:6,26:1,27:8,28:8,29:7,30:3,31:6}
#Dictionary to map Win Loss or Tie to a number
result = {"W":1, "L":0, "T":2,"":3}
#Dictionary to map the playoff games to weeks of the playoffs. Used in parsing thee game results
playoffWeeks = {"Wild Card":1,"Division":2,"Conf. Champ.":3,"SuperBowl":4}

#Stores a team object for every team
class data:
    averageHomeFieldAdvantage = 0
    averageHomeFieldSpreadAdvantage = 0
    def __init__(self):
        self.teams = dict()
        for i in range(0,32):
            self.teams[theTeams[i]] = team(theTeams[i])
    def findTeam(self,name):
        for item in self.teams:
            return self.teams[item]
    #used for parsing the game lines data, adds odds information to the right game
    def addOdds(self,teamNum,year,opponent,week,spread,total):
        theTeam = self.teams[theTeams[teamNum]]
        theSeason = theTeam.findSeason(year)
        theGame = theSeason.findGame(opponent,week)
        theGame.spread = spread
        theGame.total = total
#Stores a season object for every season the team has data for
#Also stores the teams name in string and number form
class team:
    homeAverage = 0
    awayAverage = 0
    homeFieldAdvantage = 0
    homeSpreadAdvantage = 0
    awaySpreadAdvantage = 0
    homeFieldSpreadAdvantage = 0
    def __init__(self,name):
        self.name = name
        self.number = teams[name]
        self.seasons = list()
    def findSeason(self,year):
        for item in self.seasons:
            if(item.year == year):
                return item
#Stores every game that happened in a specific season
#also stores the week the bye week occured and if the team made the playoffs
class season:
    def __init__(self,year):
        self.year = year
        self.games = list()
        self.byeWeek = 0
        self.playoffs = 0
    def findGame(self,opponent,week):
        for agame in self.games:
            modify = 0
            if(week >= self.byeWeek):
                modify = 1
            
            if(agame.isHome):
                if(agame.awayTeam == opponent and agame.week == week + modify):
                    return agame
            else:
                if(agame.homeTeam == opponent and agame.week == week + modify):
                    return agame
    def findAGame(self,week):
        for agame in self.games:
            if(agame.week == week):
                return agame
        return game()
#Stores a bunch of information about an individual game
class game:
    byeWeek = 0 #1 if bye week 0 otherwise
    year = 0
    week = 0 #week of the season the game happened in
    day = 0 #0 for thursday, 1 for sunday afternoon, 2 for sunday night, 3 for monday night
    win = 0 #true for win false for loss
    winLetter = ""
    isHome = False #1 for home 0 for away
    opponent = 0 #number of the opponent
    homeTeam = 0 #number corresponding to the home team
    awayTeam = 0 #number corresponding to the away team
    homePoints = 0 #homeTeam points
    awayPoints = 0 #awayTeam points
    teamWinMargin = 0 #how many points the current team won (+)/lost (-) by
    homeWinMargin = 0 #how many points the home team won (+)/lost(-) by
    teamSpreadMargin = 0 #how many points the team covered (+) or didn't cover (-) by
    cover = 0 # 1 if team covers 0 if they don't 2 if the line pushes
    homePassYards = 0 #home team passing yards
    awayPassYards = 0 #away team passing yards
    homeRushYards = 0 #home team rushing yards
    awayRushYards = 0 #away team rushing yards
    homeTO = 0 #home turnovers
    awayTO = 0 #away turnovers
    spread = 0
    total = 0
    rest = 0
    oppRest = 0
    winStreak = 0
    gameOutcome = 0 #0 for normal | 1 for unexpected blowout loss | 2 for unexpected blowout win | 3 for close upset win | 4 close heavy underdog loss | 5 loss as heavy favorite
    restAdvantage = 0 #more positive means more advantage more negative means more disadvantage
    isRivalry = False
    toPrint = ""
    #compiles most of the information about the game into a comma separated line and returns it
    def print(self):
        if(self.year == 0):
            return ""
        if(self.win == 0):
            self.winLetter = "L"
        elif(self.win == 1):
            self.winLetter = "W"
        else:
            self.winLetter = "T"
        self.calcRivalry()
        toPrint = str("," + str(self.year) + "," + str(self.week) + "," + str(self.day) + "," 
        + str(self.winLetter) + "," + str(self.winStreak) + "," + str(self.isHome) + "," + str(self.homeTeam) + "," + str(self.awayTeam) + "," + str(self.isRivalry) + ","
        + str(self.homePoints) + "," + str(self.awayPoints) + "," + str(self.spread) + "," + str(self.total) + ","
        + str(self.homePassYards) + "," + str(self.homeRushYards) + "," + str(self.homeTO) + ","
        + str(self.awayPassYards) + "," + str(self.awayRushYards) + "," + str(self.awayTO) + "," + str(self.rest) + ","
        + str(self.oppRest) + "," + str(self.restAdvantage))
        return toPrint
    #calculates various win margins
    def calcData(self):
        if(self.year == 0):
            return
        self.homeWinMargin = self.homePoints - self.awayPoints
        if(self.isHome):
            self.teamWinMargin = self.homeWinMargin
        else:
            self.teamWinMargin = -self.homeWinMargin
        self.teamSpreadMargin = self.teamWinMargin + self.spread
        if(self.teamSpreadMargin > 0):
            self.cover = 1
        elif(self.teamSpreadMargin < 0):
            self.cover = 0
        else:
            self.cover = 2
        if(self.spread <= 0):
            if(self.teamSpreadMargin >= 14 or self.teamWinMargin >= 21):
            #blowout win
                self.gameOutcome = 2
            if(self.spread >= 7 and self.win == 0):
                self.gameOutcome = 5   
        else:
            if(self.teamSpreadMargin >= 6.5 and self.teamWinMargin > -4 and self.win == False):
                #close underdog loss
                self.gameOutcome = 4
            if(self.teamSpreadMargin <= -6.5 and self.win == True):
                self.gameOutcome = 3
        if(self.teamSpreadMargin <= -7 and self.teamWinMargin <= -14):
            self.gameOutcome = 1

        self.calcRivalry()

    #determines if a game is a rivalry game
    def calcRivalry(self):
        if(divisions[self.homeTeam] == divisions[self.awayTeam]):
            self.isRivalry = True
    def calcRest(self,prevGame,oppPrevGame):
        if(self.win == 1):
            self.winStreak = prevGame.winStreak + 1
        elif(self.win == 0):
            self.winStreak = 0
        if(self.day == 0 and prevGame.day != 0):
            self.rest = -1
        elif(self.day != 0 and prevGame.day == 0):
            self.rest = 1
        elif(prevGame.byeWeek == 1):
            self.rest = 1
        if(self.day == 0 and oppPrevGame.day != 0):
            self.oppRest = -1
        elif(self.day != 0 and oppPrevGame.day == 0):
            self.oppRest = 1
        elif(oppPrevGame.byeWeek == 1):
            self.oppRest = 1
        self.restAdvantage = self.rest - self.oppRest
    
#open all the files
resultsFile = open("NFL_Game_Results_By_Year.csv", "r") 
oddsFile = open("NFL_Game_Lines_By_Year.csv", "r")
parsedDataFile = open("parsedData.csv","w")

#reads in all the data from the files
results = (resultsFile.read()).splitlines()
odds = (oddsFile.read()).splitlines()

#the variable where all the data goes
teamData = data()

#the name of the current team, year, week, and season
teamName = ""
year = 0
week = 0
currentSeason = season(0)
#makes sure it only adds the current season once
done = 0
playoffs = 0
wildcard = 0
for aLine in results:
    line = aLine.split(",")
    #the line contains the name of the team and year
    if(len(line) == 2):
        playoffs = 0
        wildcard = 0
        done = 1
        teamName = line[0]
        year = int(line[1])
        #ignores all data after last season
        if(year > 2021):
            break
        currentSeason = season(year)
    #if line is empty then that season is done so write it but only once (see done variable)
    elif(len(line) < 2 and done == 1):
        done = 0
        teamData.teams[theTeams[teams[teamName]]].seasons.append(currentSeason)
    #skip empty lines
    elif(len(line) < 2):
        continue
    #store the bye week
    elif(line[10] == "Bye Week"):
        currentSeason.byeWeek = int(float(line[1]))
        byeGame = game()
        byeGame.byeWeek = 1
        currentSeason.games.append(byeGame)
    #store if team made playoffs
    elif(line[3] == "Playoffs"):
        playoffs = int(float(line[0]))
        currentSeason.playoffs = playoffs
        byeGame = game()
        byeGame.byeWeek = 1
        currentSeason.games.append(byeGame)
    #collects the game info and stores it in a game object
    else:
        if(playoffs == 0):
            try:
                week = int(line[1])
            except ValueError:
                continue
        else:
            playoffWeek = playoffWeeks[line[1]]
            if(playoffWeek == 1):
                wildcard = 1
            if(wildcard == 1):
                week = playoffWeek + playoffs
            else:
                week = playoffWeek + playoffs - 1

        theGame = game()
        theGame.year = year
        theGame.week = week
        theGame.day = days[line[2]]
        theGame.win = result[line[6]]
        theGame.opponent = teams[line[10]]
        if(line[9] != '@'):
            theGame.isHome = True
            theGame.homeTeam = teams[teamName]
            theGame.awayTeam = teams[line[10]]
            theGame.homePoints = int(float(line[11]))
            theGame.awayPoints = int(float(line[12]))
            theGame.homePassYards = int(float(line[15]))
            theGame.homeRushYards = int(float(line[16]))
            theGame.awayPassYards = int(float(line[20]))
            theGame.awayRushYards = int(float(line[21]))
        else:
            theGame.isHome = False
            theGame.homeTeam = teams[line[10]]
            theGame.awayTeam = teams[teamName]
            theGame.homePoints = int(float(line[12]))
            theGame.awayPoints = int(float(line[11]))
            theGame.homePassYards = int(float(line[15]))
            theGame.homeRushYards = int(float(line[16]))
            theGame.awayPassYards = int(float(line[20]))
            theGame.awayRushYards = int(float(line[21]))
        currentSeason.games.append(theGame)



#reads in the game lines data
for aLine in odds:
    line = aLine.split(",")
    #gets the team name and year
    if(len(line) == 2):
        teamName = line[0]
        year = int(line[1])
        if(year > 2021):
            break
    #skips empty lines
    elif(len(line) < 2):
        continue
    #reads in game line and totals
    else:
        try:
            week = int(line[0])+1

        except ValueError:
            continue
        opponent = abbreviations[line[2]]
        spread = float(line[3])
        total = float(line[4])
        teamData.addOdds(teams[teamName],year,opponent,week,spread,total)


winMargins = dict()
winMarginsByTeam = dict()
rivalryWinMargins = dict()
spreads = dict()
spreadWinPercent = dict()
rivalrySpreadWinMargins = list()
spreadWinMargins = list()
nonRivSpreadMargins = list()
restAdvantage = dict()
restAdvantageWins = dict()
restAdvantageSpreadWins = dict()
entries = {0:"Home",1:"Away",2:"Home Spread",3:"Away Spread"}
#collects win margins both in general and by team (home/away)
gamesAgainstSteelers = list()
wins = 0
losses = 0
for theSeason in teamData.teams["Atlanta Falcons"].seasons:
    for theGame in theSeason.games:
        if(theGame.opponent == 26):
            gamesAgainstSteelers.append(theGame)
            if(theGame.win == 1):
                wins += 1
            elif(theGame.win == 0):
                losses += 1
print("The Falcons won " + str(wins) + " games against the Steelers and lost " +str(losses))
for ateam in teamData.teams:
    winMarginsByTeam[ateam] = {0:dict(),1:dict(),2:dict(),3:dict()}
    # 0 HomeMargin | 1 AwayMargin | 2 HomeSpreadMargin | 3 AwaySpreadMargin
    for aseason in teamData.teams[ateam].seasons:
        prevGame = game()
        for agame in aseason.games:
            if(agame.byeWeek == 1):
                prevGame = agame
                continue
            agame.calcData()
            oppPrevGame = teamData.teams[theTeams[agame.opponent]].findSeason(aseason.year).findAGame(agame.week - 1)
            agame.calcRest(prevGame,oppPrevGame)
            try:
                winMargins[agame.teamWinMargin] += 1
            except KeyError:
                winMargins[agame.teamWinMargin] = 1
            if(agame.restAdvantage != 0):
                try:
                    restAdvantage[agame.restAdvantage] += 1
                except KeyError:
                    restAdvantage[agame.restAdvantage] = 1
                    restAdvantageWins[agame.restAdvantage] = 0
                    restAdvantageSpreadWins[agame.restAdvantage] = 0
                if(agame.teamWinMargin > 0):
                    try:
                        restAdvantageWins[agame.restAdvantage] += 1
                    except KeyError:
                        restAdvantageWins[agame.restAdvantage] = 1
                if(agame.teamSpreadMargin > 0):
                    try:
                        restAdvantageSpreadWins[agame.restAdvantage] += 1
                    except KeyError:
                        restAdvantageSpreadWins[agame.restAdvantage] = 1
            if(agame.spread < 0):
                theSpread = agame.spread
                if(theSpread.is_integer()):
                    theSpread -= 0.5
                try:
                    spreads[theSpread] += 1
                except KeyError:
                    spreads[theSpread] = 1
                    spreadWinPercent[agame.spread] = 0
                if(agame.cover == 1):
                    try: 
                        spreadWinPercent[theSpread] += 1
                    except KeyError:
                        spreadWinPercent[theSpread] = 1
                spreadWinMargins.append(agame.teamSpreadMargin)
                if(agame.isRivalry == False):
                    nonRivSpreadMargins.append(agame.teamSpreadMargin)
            if(agame.isRivalry == True):
                try:
                    rivalryWinMargins[agame.teamWinMargin] += 1
                except KeyError:
                    rivalryWinMargins[agame.teamWinMargin] = 1
                if(agame.spread < 0):
                    rivalrySpreadWinMargins.append(agame.teamSpreadMargin)
            if(agame.isHome):
                try:
                    winMarginsByTeam[ateam][0][agame.teamWinMargin] += 1
                except KeyError:
                    winMarginsByTeam[ateam][0][agame.teamWinMargin] = 1
                try:
                    winMarginsByTeam[ateam][2][agame.teamSpreadMargin] += 1
                except KeyError:
                    winMarginsByTeam[ateam][2][agame.teamSpreadMargin] = 1
            else:
                try:
                    winMarginsByTeam[ateam][1][agame.teamWinMargin] += 1
                except KeyError:
                    winMarginsByTeam[ateam][1][agame.teamWinMargin] = 1
                try:
                    winMarginsByTeam[ateam][3][agame.teamSpreadMargin] += 1
                except KeyError:
                    winMarginsByTeam[ateam][3][agame.teamSpreadMargin] = 1
            prevGame = agame
keys = list()
values = list()
homeAverage = 0
homeNumGames = 0
awayAverage = 0
awayNumGames = 0
homeSpreadAverage = 0
awaySpreadAverage = 0
#set to false to avoid having to close out 60+ graphs
plot = False
#creates bar graphs of win margins for home and away games
#calculates average win margin both home and away
abbs = list()
advs = list()
spreadAdvs = list()
totAdvantage = 0
totSpreadAdvantage = 0
for theTeam in winMarginsByTeam:
    for home in sorted(winMarginsByTeam[theTeam].keys()):
        for item in sorted(winMarginsByTeam[theTeam][home].keys()):
            keys.append(item)
            values.append(winMarginsByTeam[theTeam][home][item])
        if(plot):
            plt.bar(keys, values, tick_label = keys, width = 1,color = ['red','green'])
            plt.xlabel('Win Margins')
            plt.ylabel('Number of Occurances')
            plt.title(theTeam + entries[home])
            plt.show()
        if(home == 0):    
            for i in range(0,len(keys)):
                homeAverage += keys[i] * values[i]
                homeNumGames += values[i]
            homeAverage /= homeNumGames
        elif(home == 1):
            for i in range(0,len(keys)):
                awayAverage += keys[i] * values[i]
                awayNumGames += values[i]
            awayAverage /= awayNumGames
        elif(home == 2):
            for i in range(0,len(keys)):
                homeSpreadAverage += keys[i] * values[i]
            homeSpreadAverage /= homeNumGames
        elif(home == 3):
            for i in range(0,len(keys)):
                awaySpreadAverage += keys[i] * values[i]
            awaySpreadAverage /= awayNumGames
        keys.clear()
        values.clear()
    homeFieldAdvantage = (homeAverage - awayAverage)/2
    homeFieldSpreadAdvantage = (homeSpreadAverage - awaySpreadAverage)/2
    teamData.teams[theTeam].homeAverage = homeAverage
    teamData.teams[theTeam].awayAverage = awayAverage
    teamData.teams[theTeam].homeSpreadAverage = homeSpreadAverage
    teamData.teams[theTeam].awaySpreadAverage = awaySpreadAverage
    teamData.teams[theTeam].homeFieldAdvantage = homeFieldAdvantage/2
    teamData.teams[theTeam].homeFieldSpreadAdvantage = homeFieldSpreadAdvantage/2
    totAdvantage += homeFieldAdvantage
    totSpreadAdvantage += homeFieldSpreadAdvantage
    abbs.append(abbFromNum[teams[theTeam]])
    advs.append(homeFieldAdvantage)
    spreadAdvs.append(homeFieldSpreadAdvantage)

    homeAverage = 0
    awayAverage = 0
    homeSpreadAverage = 0
    awaySpreadAverage = 0
    homeNumGames = 0
    awayNumGames = 0
teamData.averageHomeFieldAdvantage = totAdvantage / 32
teamData.averageHomeFieldSpreadAdvantage = totSpreadAdvantage / 32
a = list(set(advs))
a.sort()
res = []
for i in a:
    for j in range(0, len(advs)):
        if(advs[j] == i):
            res.append(abbs[j])


plt.bar(range(0,32), a, tick_label = res, width = 1,color = ['red','blue','green'])
plt.xlabel('Team Names')
plt.ylabel('Home Field Advantage')
plt.title("Home Field Advantages | Average: " + str(totAdvantage/32))
plt.show()

a = list(set(spreadAdvs))
a.sort()
res = []
for i in a:
    for j in range(0, len(spreadAdvs)):
        if(spreadAdvs[j] == i):
            res.append(abbs[j])
plt.bar(range(0,32), a, tick_label = res, width = 1,color = ['red','blue','green'])
plt.xlabel('Team Names')
plt.ylabel('Home Field Spread Advantage')
plt.title("Home Field Spread Advantages | Average: " + str(totSpreadAdvantage/32))
plt.show()
keys.clear()
values.clear()
#plot the win margins for all games
for item in sorted(winMargins.keys()):
    if(item >= 0 and winMargins[item] > 5):
        keys.append(item)
        values.append(winMargins[item])
plt.bar(keys, values, tick_label = keys, width = 1,color = ['red','green'])
plt.xlabel('Win Margins')
plt.ylabel('Number of Occurances')
plt.title('Win Margin Frequency')
plt.show()
keys.clear()
values.clear()
#plot the percentage that spreads hit for the favorite
totalFavoritePercent = 0
totalItems = 0
totalWins = 0
for item in sorted(spreads.keys()):
    totalItems += spreads[item]
    totalWins += spreadWinPercent[item]
    totalFavoritePercent = totalWins/totalItems
    if(spreadWinPercent[item] > 1):
        keys.append(item)
        values.append(spreadWinPercent[item] / spreads[item])
plt.bar(keys, values, tick_label = keys, width = 0.5,color = ['red','green','blue'])
plt.xlabel('Spreads')
plt.ylabel('Win Percentage')
plt.title("Spread Win Percentage | Average: " + str(round(totalFavoritePercent,4)))
plt.show()
keys.clear()
values.clear()
#plot the percentage that a team wins after rest advantage
for item in sorted(restAdvantage.keys()):
    keys.append(item)
    values.append(restAdvantageWins[item] / restAdvantage[item])
plt.bar(keys, values, tick_label = keys, width = 0.5,color = ['red','green','blue'])
plt.xlabel('Rest Advantage')
plt.ylabel('Win Percentage')
plt.title("Rest Advantage Win Percentage")
plt.show()
keys.clear()
values.clear()
#plot the percentage that a team covers the spread after a rest advantage
for item in sorted(restAdvantage.keys()):
    keys.append(item)
    values.append(restAdvantageSpreadWins[item] / restAdvantage[item])
plt.bar(keys, values, tick_label = keys, width = 0.5,color = ['red','green','blue'])
plt.xlabel('Rest Advantage')
plt.ylabel('Win Percentage')
plt.title("Rest Advantage Spread Win Percentage")
plt.show()
keys.clear()
values.clear()
#plot rivalry win margins
for item in sorted(rivalryWinMargins.keys()):
    if(item >= 0 and rivalryWinMargins[item] > 1):
        keys.append(item)
        values.append(rivalryWinMargins[item])
plt.bar(keys, values, tick_label = keys, width = 1,color = ['red','blue','green'])
plt.xlabel('Rivalry Win Margins')
plt.ylabel('Number of Occurances')
plt.title('Win Margin Frequency')
plt.show()
keys.clear()
values.clear()
#plot spread rivalry win margins

plt.hist(rivalrySpreadWinMargins, 20, (-30,30), color = 'green',
        histtype = 'bar', rwidth = 0.8)
plt.xlabel('Rivalry Spread Win Margins')
plt.ylabel('Number of Occurances')
average = sum(rivalrySpreadWinMargins) / len(rivalrySpreadWinMargins)
plt.title("Rivalry Spread Margin Frequency | Average: " + str(round(average,4)))
plt.show()
#plot spread win margins
plt.hist(spreadWinMargins, 30, (-30,30), color = 'green',
        histtype = 'bar', rwidth = 0.8)
plt.xlabel('Spread Win Margins')
plt.ylabel('Number of Occurances')
average = sum(spreadWinMargins) / len(spreadWinMargins)
plt.title("Spread Margin Frequency | Average: " + str(round(average,4)))
plt.show()

#plot non-rivalry spread win margins
plt.hist(nonRivSpreadMargins, 30, (-30,30), color = 'green',
        histtype = 'bar', rwidth = 0.8)
plt.xlabel('Non Rivalry Spread Win Margins')
plt.ylabel('Number of Occurances')
average = sum(nonRivSpreadMargins) / len(nonRivSpreadMargins)
plt.title("Non-Rivalry Spread Margin Frequency | Average: " + str(round(average,4)))
plt.show()


22,29
gamesAgainstBuccaneers = list()
wins = 0
losses = 0
for theSeason in teamData.teams["New Orleans Saints"].seasons:
    for theGame in theSeason.games:
        if(theGame.opponent == 29 ):
            gamesAgainstBuccaneers.append(theGame)
            if(int(theGame.teamSpreadMargin) > 0 ):
                wins += 1
            
            if(int(theGame.teamSpreadMargin) == 0 ):
                wins +=1

print("The Saints Covered " + str(wins) + " games against the Buccaneers")


#write data to the parsed data csv file
toWrite = ""
for ateam in teamData.teams:
    toWrite += ateam + "\n"
    for aseason in teamData.teams[ateam].seasons:
        toWrite += (ateam + " " + str(aseason.byeWeek) + "," + str(aseason.year) + ",Week,Day,W/L,WinStreak,Home?,Home Team,Away Team,Is Rivalry,Home Points," +
        "Away Points,Spread,Total,Home Pass yards, Home Rush Yards,Home TOs,Away Pass Yards,Away Rush Yards,Away TOs,Team Rest,Opp Rest,Rest Diff\n")
        for agame in aseason.games:
            toWrite += agame.print() + "\n"
        toWrite += "\n"
    toWrite += "\n"




parsedDataFile.write(toWrite)
resultsFile.close()
oddsFile.close()
parsedDataFile.close()
