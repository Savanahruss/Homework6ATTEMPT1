import Homework5P1P2 as Cls
import scr.FigureSupport as FigSupport

#myGame=Cls.Game(id=1,prob_head=0.5)
mySetGame=Cls.SetOfGames(prob_head=0.5,n_games=1000)

FigSupport.graph_histogram(mySetGame.get_game_rewards(),
                           x_range=(-300,300),title='Histogram of Rewards',
                           x_label='Number of Games',
                           y_label='Reward')
