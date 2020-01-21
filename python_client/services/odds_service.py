import requests
import json
from fuzzywuzzy import fuzz
import datetime
from pathlib import Path

class Odds_Service:

    def get_all_fixtures_of_date(self, fixture_date):
        limit = self.read_request_limit()
        if int(limit) <= 1:
            print('request limit reached')
            return ''
        else:
            date = datetime.datetime.strptime(fixture_date, '%Y-%m-%d')
            url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/date/" + \
                str(date.date())
            headers = self.get_header_information()
            response = requests.request("GET", url, headers=headers)
            self.write_request_limit(
                response.headers['X-RateLimit-requests-Remaining'])
            fixture_list = json.loads(response.text)['api']['fixtures']
            return fixture_list

    def filter_on_not_finished(self, fixtures):
        filtered_fixtures = []
        for fixture in fixtures:
            if fixture['status'] != "Match Finished":
                filtered_fixtures.append(fixture)
        return filtered_fixtures

    def get_fixture_from_team_names(self, fixtures, home_team, away_team):
        highest_score = 0
        selected_fixture = None
        for fixture in fixtures:
            fixture_home_team = fixture['homeTeam']['team_name']
            fixture_away_team = fixture['awayTeam']['team_name']
            similarity_score_home_team = fuzz.token_sort_ratio(
                fixture_home_team, home_team)
            similarity_score_away_team = fuzz.token_sort_ratio(
                fixture_away_team, away_team)
            higher_score = similarity_score_home_team if similarity_score_home_team > similarity_score_away_team else similarity_score_away_team
            if higher_score > highest_score:
                highest_score = higher_score
                selected_fixture = fixture
        return selected_fixture

    def get_odds_list_of_fixture(self, fixture_id):
        limit = self.read_request_limit()
        if int(limit) <= 1:
            print('request limit reached')
            return ''
        else:
            url = "https://api-football-v1.p.rapidapi.com/v2/odds/fixture/" + str(fixture_id)
            headers = self.get_header_information()
            response = requests.request("GET", url, headers=headers)
            odds_list = json.loads(response.text)['api']['odds']
            return odds_list
    
    def get_best_bookmaker(self, minimal_ratio, predicted_winning_side, games_odds_list):
        best_bookmaker = {}
        best_bookmaker['bookmaker_name'] = ''
        best_bookmaker['odd'] = 0
        for odds in games_odds_list:
            bookmakers = odds['bookmakers']
            for bookmaker in bookmakers:
                bets = bookmaker['bets']
                for bet in bets:
                    if bet['label_name'] == "Match Winner":
                        values = bet['values']
                        if predicted_winning_side == 'home':
                            for bet_quotes in values:
                                if bet_quotes['value'] == "Home" and float(bet_quotes["odd"]) > minimal_ratio:
                                    if float(best_bookmaker["odd"]) < float(bet_quotes["odd"]) :
                                        best_bookmaker["bookmaker_name"] = bookmaker["bookmaker_name"]
                                        best_bookmaker["odd"] =  bet_quotes["odd"]
                        if predicted_winning_side == 'away':
                             for bet_quotes in values:
                                if bet_quotes['value'] == "Away" and float(bet_quotes["odd"]) > minimal_ratio:
                                    if float(best_bookmaker["odd"]) < float(bet_quotes["odd"]) :
                                        best_bookmaker["bookmaker_name"] = bookmaker["bookmaker_name"]
                                        best_bookmaker["odd"] =  bet_quotes["odd"]
        return best_bookmaker

    def write_request_limit(self, limit):
        path = Path(__file__).parent / "./request_limit.txt"
        text_file = open(path, "w")
        text_file.write(str(limit))
        text_file.close()

    def read_request_limit(self):
        path = Path(__file__).parent / "./request_limit.txt"
        text_file = open(path, "r")
        content = text_file.read()
        text_file.close()
        return content

    def get_header_information(self):
        path = Path(__file__).parent / "../api-credentials.txt"
        text_file = open(path, "r")
        content = text_file.read()
        headers = {
                'x-rapidapi-host': 'api-football-v1.p.rapidapi.com',
                'x-rapidapi-key': content
        }
        return headers