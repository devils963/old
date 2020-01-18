from services.spi_data_loader_service import SPI_Data_Loader_Service
from services.spi_prediction_service import SPI_Prediction_Service
from services.odds_service  import Odds_Service
import time

spi_data_loader_service = SPI_Data_Loader_Service()
spi_data_loader_service.update_spi_file()

spi_service = SPI_Prediction_Service()
all_games_to_bet_on = spi_service.get_games_to_bet_this_week()

odds_service = Odds_Service()

for game in all_games_to_bet_on:
        fixtures_on_date = odds_service.get_all_fixtures_of_date(game['date'])
        not_finished_fixtures = odds_service.filter_on_not_finished(fixtures_on_date)
        fixture = odds_service.get_fixture_from_team_names(
            not_finished_fixtures, game['home'], game['away'])
        odds_of_game = odds_service.get_odds_list_of_fixture(fixture['fixture_id'])
        best_bookmaker = odds_service.get_best_bookmaker(
            game['min_quote'], game['winning_side'], odds_of_game)

        odds_service.show_game_information(game, fixture)
        odds_service.show_bookmaker_information(
            best_bookmaker['bookmaker_name'], best_bookmaker['odd'], game['winning_side_probability'])

        time.sleep(10)
