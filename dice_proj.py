import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll


while True:
    players=input('enter number of players between(2-4) :')
    if players.isdigit():
        players=int(players)
        if players>=2 and players<=4:
            break
        else:
            print('players must be between 2-4.')
    else:
        print('please enter numbers only')


max_score=30
players_score=[0 for i in range(players)]

while max(players_score)<max_score:
    for player_indx in range(players):
        print('player number',player_indx+1,'turn has just started')
        current_score=0
        
        while True:
            should_roll=input('would you like to roll say yes or no')
            if should_roll.lower()!='yes':
                break
            
            value=roll()
            if value==1:
                print('your roll turn done')
                current_score=0
                break
            else:
                current_score+=value
                print('you rolled a value :',value)
            print('your score is :',current_score)
    
    players_score[player_indx]+=current_score
    print('your total score is :',players_score[player_indx])

maximum_score=max(players_score)
winning_indx=players_score.index(maximum_score)
print('player number',winning_indx+1, 'is the winner with a score of :',maximum_score)

    
