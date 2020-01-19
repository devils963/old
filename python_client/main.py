from services.spi_data_loader_service import SPI_Data_Loader_Service
from services.spi_prediction_service import SPI_Prediction_Service
from services.odds_service  import Odds_Service
from services.view_service import View_Service
import time

spi_data_loader_service = SPI_Data_Loader_Service()
spi_data_loader_service.update_spi_file()

spi_prediction_service = SPI_Prediction_Service()
all_games_to_bet_on = spi_prediction_service.get_games_to_bet_this_week()

odds_service = Odds_Service()
view_service = View_Service()

bettable_games_list = []

for game in all_games_to_bet_on:
        fixtures_on_date = odds_service.get_all_fixtures_of_date(game['date'])
        not_finished_fixtures = odds_service.filter_on_not_finished(fixtures_on_date)
        fixture = odds_service.get_fixture_from_team_names(
            not_finished_fixtures, game['home'], game['away'])
        odds_of_game = odds_service.get_odds_list_of_fixture(fixture['fixture_id'])
        best_bookmaker = odds_service.get_best_bookmaker(
            game['min_quote'], game['winning_side'], odds_of_game)

        game_information = spi_prediction_service.compute_game_information_dictionary(game, fixture, best_bookmaker)
        bettable_games_list.append(game_information)

        time.sleep(10)

view_service.show_game_information(bettable_games_list)





