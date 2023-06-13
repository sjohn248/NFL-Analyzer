import pandas as pd
import requests
import time



teams = {'crd':'Arizona Cardinals', 'atl':'Atlanta Falcons','rav':'Baltimore','buf':'Buffalo Bills','car':'Carolina Panthers','chi':'Chicago Bears','cin':'Cincinnati Bengals',
        'cle':'Cleveland Browns','dal':'Dallas Cowboys','den':'Denver Broncos','det':'Detroit Lions','gnb':'Green Bay Packers',
        'htx':'Houston Texans','clt':'Indianapolis Colts','jax':'Jacksonville Jaguars',
         'kan':'Kansas City Chiefs','rai':'Las Vegas Raiders','sdg':'Los Angeles Chargers','ram':'Los Angeles Rams','mia':'Miami Dolphins','min':'Minnesota Vikings',
         'nwe':'New England Patriots','nor':'New Orleans Saints','nyg':'New York Giants','nyj':'New York Jets','phi':'Philadelphia Eagles','pit':'Pittsburgh Steelers',
         'sfo':'San Francisco 49ers','sea':'Seattle Seahawks','tam':'Tampa Bay Buccaneers','oti':'Tennessee Titans','was':'Washington Commanders'}

timeOut = 2
#year to start grabbing data from
year = 2012
while(year < 2023):
    for team in teams:
        url = f'https://www.pro-football-reference.com/teams/{team}/{year}_lines.htm'
        r = requests.get(url)
        while(1):
            if (r.ok):
                df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
                print(url)
                df = df_list[0]
                with open('NFL_Game_Lines_By_Year.csv', 'a') as file: file.write(f"{teams[team]},{year}\n")
                df.to_csv('NFL_Game_Lines_By_Year.csv', mode='a')
                with open('NFL_Game_Lines_By_Year.csv', 'a') as file: file.write("\n\n")
                
                time.sleep(12)
                break
            else:
                timeOut = timeOut*2
                print(f"Code: {r.status_code}, Sleeping...{timeOut}\n")
                time.sleep(timeOut)
                r = requests.get(url)       
    year+=1