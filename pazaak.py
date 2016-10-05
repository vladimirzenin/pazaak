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

    cancel_round = False
    while not cancel_round:
        step(board_player1, cards, handles_player1, score_b_pl1)
        step(board_player2, cards, handles_player2, score_b_pl2)
        cancel_round = True

def init_cards(cards, handles_player1, handles_player2):
    print('Select cards...')

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

def step(board, cards, handles_card, score):
    
    ind = 0
    ind_board = -1
    while ind <= 8:
        if board[ind] == 0:
            ind_board = ind
            break
        ind = ind + 1 

    ind_selected_card_general = random.randint(0, len(cards) )
    selected_card_general = cards[ind_selected_card_general]
    cards.pop(ind_selected_card_general)

    score = score + selected_card_general

    hand_gamer = ''
    for i in handles_card:
        hand_gamer = hand_gamer + ', ' + str(i)

    str_ = 'Your score: ' + str(score) + '. Доступна рука игрока: ' + hand_gamer
    print(str_)
    select_done = False
    while not select_done:

        user_input = input()
        print('======================')
        print(user_input)
        select_card = int(user_input)
        ind = handles_card.index(select_card)
        if ind > 0:
            handles_card.pop(ind)
            select_done = True

    
            



if __name__ == "__main__":
    main()
else:
    print('Is console')