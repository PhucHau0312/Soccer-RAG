---
sdk: docker
---
<!---WARNING!! The snippet above is required for Huggingface Space in https://huggingface.co/spaces/SimulaMet-HOST/SoccerRAG, so don't remove or move this.
You need to manually update games.db in space in ./data as space doesn't allow pushing file more than 10MB.
Sushant usually force updates that space repo with Github's version and then uploads the db file manually at https://huggingface.co/spaces/SimulaMet-HOST/SoccerRAG/tree/main/data
--->

# SoccerRAG: Multimodal Soccer Information Retrieval via Natural Queries

## Project Organization

```tree
├── data
│   ├── augmented_leagues.csv
│   ├── augmented_teams.csv
├── src
│   ├── conf
│   │   ├── schema.json
│   │   ├── sqls.json
│   ├── __init__.py
│   ├── database.py
│   ├── extractor.py
│   └── sql_chain.py
├── app.py
├── chainlit.md
├── Dockerfile
├── main_cli.py
├── main.py
├── requirements.txt
├── setup.py
```

## Enviroment setup

````bash
pip install -r requirements.txt
````

````bash
pip install soccernet
````

## Setting up the database
  
````bash
python setup.py
````

The data should be placed in the ./data/SoccerNet

For each league / season / game, there is a new folder with the name of the leauge / season (YYYY-YYYY) / game (YYYY-MM-DD - HomeTeam Score - Score AwayTeam). In each game folder, place the Labels-v2.json and Labels-captions.json files

### Setting up and populating the database

````bash
python src/database.py
````

## Running the code in command line

````bash
The code will prompt you to enter a natural language query.

python main.py
````

````bash
python main_cli.py -q "How many goals has Messi scored each season?"
````

## Running the code in ChainLit (GUI)

````bash
chainlit run app.py
````

![ChainLit](assets/chainlit.png)

### Example query

````angular2html
Enter a query: How many goals has Messi scored each season?
Lionel Messi has scored the following number of goals each season:
- 2014-2015: 13 goals
- 2015-2016: 3 goals
- 2016-2017: 31 goals
````

## Results

Sample questions (Q1-Q20) and corresponding results can be found below.

````angular2html
Question 1: Is Manchester United in the database ?
Question 2: Give me the total home goals for Bayern M in the 2014-15 season.
Question 3: Calculate home advantage for Real Madrid in the 2015-16 season.
Question 4: How many goals did Messi score in the 15-16 season ?
Question 5: How many yellow-cards did Enzo Perez get in the 15-2016 season ?
Question 6: List all teams that played a game against Napoli in 2016-17 season in seriea ? Do not limit the number of results.
Question 7: Give all the teams in the league ucl in the 2015-2016 season ?
Question 8: Give me all games in epl with yellow cards in the first half in the 2015-2016 season.
Question 9: What teams and leagues has Adnan Januzaj play in ?
Question 10: List ALL players that started a game for Las Palmas in the 2016-2017 season ? Do NOT limit the number of results.
Question 11: Did Ajax or Manchester United win the most games in the 2014-15 season ?
Question 12: How many yellow and red cards were given in the UEFA Champions League in the 2015-2016 season ?
Question 13: Are Messi and C. Ronaldo in the database ?
Question 14: How many goals did E.Hazard score in the game between Bournemouth and Chelsea in the 2015-2016 season ?
Question 15: How many yellow cards were given in the game between Bayern Munich and Shakhtar Donetsk in the 2014-15 UEFA Champions League, and did anyone receive a red card ?
Question 16: Make a list of when corners happened in the English Premier League (EPL) 2015-2016 season. Aggregate by a period of 15 minutes.
Question 17: What league is Manchester United, Arsenal, Bournemouth, Real Madrid, Chelsea, and Liverpool in ?
Question 18: How many players have "Aleksandar" as their first name in the database, and how many goals have they scored in total ?
Question 19: What did the commentary say about the game between Arsenal and Southampton in the 2016-17 season ?
Question 20: Have Mesut Ozil, Pablo Insua, or Alex Pike played for West Ham or Barcelona ?
````
  
![result-table.png](assets/result-table.png)