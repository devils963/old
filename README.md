# SPI-Soccer-Prediction

This program helps to find favorable betting odds on evaluating public SPI-Ratings.
It is based on FiveThirtyEight's SPI-Ratings  (`https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv`).
To make clear this algorithm has no guarantee to succeed but it can provide helpful advise on deciding which bet you should choose.

# How to Setup

## Prerequesites
* Python 3.8
* Rapid-API account (instructions on this later)

## Steps to Setup
1. Clone this repository to your destination of choice (example-destination : C:\Users\Public\Documents)
2. Navigate to <example-destination>\spi-soccer-prediction\python_client
3. Create a file called `api-credentials.txt` (important: name it exactly this)
4. put your Rapid-Api-Key in this document.
    1. If you dont have one go to `https://rapidapi.com/api-sports/api/api-football/pricing`
    2. Select the free plan
    3. Sign In or create a new account
    4. Go to `https://rapidapi.com/api-sports/api/api-football/endpoints` and look for your x-rapidapi-key (e.g. located in the displayed code snippet at the right bottom)
5. open the command line and type `cd <example-destination>\spi-soccer-prediction\python_client` (substitute <example-destination> with the location you stored the repo)
6. type `python main.py` to run the program 

# Credits 
Data powered by [API-FOOTBALL](https://www.api-football.com/)
The data provided by [FiveThirtyEight](https://fivethirtyeight.com/) is under Creative Commons Attribution 4.0 International license and is available [here](https://github.com/fivethirtyeight/data/tree/master/soccer-spi).




