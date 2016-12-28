# Реализация игры Пазаак из вселенной Звездных войн
# Впервые появилась в игре Star Wars: Knight of the old Respublic 
# 
# ПРАВИЛА
# 
# Игра на 2 игрока.
# Цель - первым набрать 20 очков без перебора, или приблизится к 20. Матч длится 3 раунда.
# Так же победа присуждается автоматически при наборе 9 карт, при условии отсутствия перебора.
# 
# Игроки поочередно выбирают карту из главной колоды (случайно).
# После выбора карты из общей колоды игрок может принять решение 
# добавить карту из дополнительной колоды (т.н. рука игрока).
# В конце своего хода игрок должен выбрать - играть дальше, или пасовать.
# 
# Главная колода:
# Номиналы: 1-10. В раздаче участвует 4 набора главной колоды по 10 карт.
# Дополнительная колода:
# У каждого игрока имеется собственная дополнительная колода из 10 карт, формируемая до начала партии.
# В начале партии из этих 10 карт случайным образом отбирается 4, которые будут доступны игроку.
# Виды карт доп. колоды:
#   А. Карты номиналом 1 - 6   (положительные)
#   Б. Карты номиналом -6 - -1 (отрицательные)
#   В. Карты номиналом -6 - 6  (перевертыши)
# 

import sys
import array
import random

def main():
    
    init_math = True

    while True:

        if init_math:
            print('Starting pazaak math')

            cards           = array.array('H') # Главная колода
            handles_player1 = array.array('H') # Рука игрока 1
            handles_player2 = array.array('H') # Рука игрока 2

            board_player1   = array.array('H', [0,0,0,0,0,0,0,0,0]) # Доска игрока 1
            board_player2   = array.array('H', [0,0,0,0,0,0,0,0,0]) # Доска игрока 2

            score_b_pl1     = 0                # Счет игрока 1
            score_b_pl2     = 0                # Счет игрока 2

            full_score_pl1  = 0                # Выиграно партий игроком 1
            full_score_pl2  = 0                # Выиграно партий игроком 2

            init_cards(cards, handles_player1, handles_player2)

            init_math = False
        
        print('Turn of Player 1:')
        step(board_player1, cards, handles_player1, score_b_pl1)

        print('Turn of Player 2:')
        step(board_player2, cards, handles_player2, score_b_pl2)

        status_pl1 = checkWin(score_b_pl1)
        status_pl2 = checkWin(score_b_pl2)

        win_message = ''

        if status_pl1 == 2 and status_pl2 == 2:
            # Next turn
            win_message = ''
        elif (status_pl1 == 0 and status_pl2 == 0
            or status_pl1 == 1 and status_pl2 == 1):
            # Standoff
            win_message = 'Standoff turn!'
            init_math = True            
        elif status_pl1 == 1:
            # win player 1    
            full_score_pl1 = full_score_pl1 + 1
            win_message = 'Player 1 win turn!'
            init_math = True
        elif status_pl2 == 1:
            # win player 2
            full_score_pl2 = full_score_pl2 + 1
            win_message = 'Player 2 win turn!'
            init_math = True
        elif status_pl1 == 2:
            # player 1 - lose; win player 2
            full_score_pl2 = full_score_pl2 + 1
            win_message = 'Player 2 win turn!'
            init_math = True
        elif status_pl2 == 2:
            # player 2 - lose; win player 1
            full_score_pl1 = full_score_pl1 + 1
            win_message = 'Player 1 win turn!'
            init_math = True

        print(win_message)

        win_message = ''
        if full_score_pl1 == 3 and full_score_pl2 == 3:
            # Standoff math
            win_message = 'Standoff math!'
        elif full_score_pl1 == 3:
            # Player 1 win math
            win_message = 'Player 1 win math!'
        elif full_score_pl2 == 3:
            # Player 2 win math
            win_message = 'Player 2 win math!'
        
        if not win_message == '':
            print(win_message)
            break

# Инициализация колод
def init_cards(cards, handles_player1, handles_player2):

    i = 1
    while i <= 4:
        m = 1
        while m <= 10:
            cards.append(m)
            m = m + 1
        i = i + 1
    
    m = 1
    while m <= 4:
        x = random.randint(1,7)
        handles_player1.append(x)    
        m = m + 1
    m = 1
    while m <= 4:
        x = random.randint(1,7)
        handles_player2.append(x) 
        m = m + 1  

# Ход игрока
def step(board, cards, handles_card, score):
    
    # Вытягивание карты из главной колоды
    ind_selected_card_general = random.randint(0, len(cards) )
    selected_card_general = cards[ind_selected_card_general]
    cards.pop(ind_selected_card_general)

    score = score + selected_card_general
    
    # Даем возможность сбросить карту руки, либо завершить ход, либо пасовать
    hand_gamer = ''
    for i in handles_card:
        hand_gamer = (hand_gamer 
                    + (', ' if len(hand_gamer) > 0 else '')
                    + str(i))
    str_score = 'Your score: ' + str(score) + '. Your hand: ' + hand_gamer + '. Enter the hand card, or "Next", or "Pass"'

    while True:
        
        print(str_score)

        user_input = input()
        
        try:
            user_input = int(user_input)
        except:
            pass

        if user_input == "Next" or user_input == "next":
            print('End turn.')
            break
        elif user_input == "Pass" or user_input == "pass":
            # ДОПИСАТЬ
            break
        elif user_input in handles_card:
            select_card = int(user_input)
            score = score + select_card
            str_score = 'Your score: ' + str(score) + '. End turn.'
            print(str_score)

            ind = handles_card.index(select_card)
            handles_card.pop(ind)
            break

# Проверка статуса - поражение, победа, или в процессе игры
def checkWin(score):
    if score > 20:
        return 0 # Fail
    elif score == 20:
        return 1 # Win
    else:
        return 2 # Not win

if __name__ == "__main__":
    main()
else:
    print('Is console')