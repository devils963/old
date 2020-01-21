import datetime


class View_Service():
    def show_game_information(self, game_information_list):
        filtered_games = self.filter_on_date(game_information_list)
        self.print_game_information(filtered_games)

    def filter_on_date(self, game_information_list):
        for passnum in range(len(game_information_list)-1, 0, -1):
            for i in range(passnum):
                date1 = datetime.datetime.strptime(
                    game_information_list[i]['date'], '%Y-%m-%d')
                date2 = datetime.datetime.strptime(
                    game_information_list[i+1]['date'], '%Y-%m-%d')
                if date1 > date2:
                    temp = game_information_list[i]
                    game_information_list[i] = game_information_list[i+1]
                    game_information_list[i+1] = temp
        return game_information_list

    def print_game_information(self, filtered_games):
        for filtered_game in filtered_games:
            print()
            print('date:', filtered_game['date'])
            print('game:', filtered_game['home'], filtered_game['away'], '|compare|',
                filtered_game['compared_home'], filtered_game['compared_away'])
            print('minimal betting odd:', filtered_game['minimal_betting_odd'])
            print('probability to win this game:',
                filtered_game['winning_side_probability'], 'on', filtered_game['winning_side'])

            if filtered_game['best_bookmaker'] != '':
                print('best one is ' + filtered_game +
                    ' with quote ' + str(filtered_game))
            else:
                print('dont work for this game')
            print()

    def print_progress_bar(self, iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
        percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
        if iteration == total:
            print()
    