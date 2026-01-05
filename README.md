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
Enter a query: How many goals has Messi scored each season ?
Lionel Messi has scored the following number of goals each season:
- 2014-2015: 13 goals
- 2015-2016: 3 goals
- 2016-2017: 31 goals
````

## Evaluation

````angular2html
=== Averages ===
ContextualRelevancy:  0.263 (relevancy between retrieved sql templates and agent sql)
SQLIntentCorrectness: 0.897 (intent correctness of agent sql based on question, extracted information and retrieved sql templates)
ArgumentCorrectness:  1.000 (correctness of tool-call args from input context)

=== Per record ===
[1] Is Manchester United in the database?
  ContextualRelevancy:  0.000
    Reason: The score is 0.00 because none of the statements in the retrieval context address whether Manchester United is in the database, as noted in the irrelevancy reasons and the absence of any relevant statements.
  SQLIntentCorrectness: 0.773
    Reason: The SQL statement is syntactically correct and answers the question by checking if 'Manchester United' exists in the teams table. However, it does not use the provided information that 'Manchester United' has a primary key of 7, which could have been used for a more precise query (e.g., WHERE id = 7). There are no hallucinated filters or joins, and the output is limited to 5 rows, which is mildly extraneous but not a major issue. The main shortcoming is not leveraging the provided primary key.
  ArgumentCorrectness:  1.000
    Reason: Great job! The score is 1.00 because there were no incorrect tool calls and the input was handled perfectly.

[2] Give me the total home goals for Bayern M in the 2014-15 season.
  ContextualRelevancy:  0.000
    Reason: The score is 0.00 because the retrieval context discusses a different season and does not address total home goals for Bayern M in 2014-15, nor does it mention home games or the team as required by the input.
  SQLIntentCorrectness: 0.999
    Reason: The SQL query correctly sums the home goals for Bayern Munich (using the provided primary key 28) in the 2014-2015 season (using the mapped season string). The query is syntactically correct, uses the correct entity and filters, and does not include unnecessary columns or hallucinated conditions. All provided information is used appropriately, fully aligning with the evaluation steps.
  ArgumentCorrectness:  1.000
    Reason: Great job! The score is 1.00 because there are no incorrect tool calls and the input is handled correctly.

[3] Calculate home advantage for Real Madrid in the 2015-16 season
  ContextualRelevancy:  0.750
    Reason: The score is 0.75 because, while the context provides SQL queries that can be used to calculate home advantage for any team and season ('The context provides SQL queries...for a given team and season'), the specific data referenced is for the 2016-2017 season, not the requested 2015-16 season.
  SQLIntentCorrectness: 0.973
    Reason: The SQL output correctly uses the provided information: Real Madrid's primary key (38) and the season ('2015-2016'). It constructs CTEs to separately aggregate home and away results for Real Madrid in the specified season, aligning with the intent to calculate home advantage. The query is syntactically plausible, uses the correct entity and season, and does not introduce hallucinated filters or joins. The output columns provide all necessary stats to assess home advantage, matching the question's requirements and the evaluation steps.
  ArgumentCorrectness:  1.000
    Reason: Great job! The score is 1.00 because there are no incorrect tool calls and all the input information is handled correctly.

[4] How many goals did Messi score in the 15-16 season?
  ContextualRelevancy:  1.000
    Reason: The score is 1.00 because the retrieval context provides SQL queries that directly answer how many goals Messi scored in the 15-16 season. Great job!
  SQLIntentCorrectness: 1.000
    Reason: The SQL query correctly counts the number of goals scored by Messi in the 2015-2016 season, using the provided primary key for Messi ('vgOOdZbd'), the correct season string ('2015-2016'), and the correct event label ('Goal'). The query structure matches the intent of the question, uses the provided information accurately, and does not introduce any unnecessary filters or columns. The output is syntactically plausible and directly answers the user question.
  ArgumentCorrectness:  1.000
    Reason: Great job! The score is 1.00 because all tool calls were correct and there were no issues with the input or reasoning.
...
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
