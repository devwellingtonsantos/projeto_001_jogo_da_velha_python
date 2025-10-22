import random

from move import Move


class Player:

    PLAYER_MARKER = 'X'
    COMPUTER_MARKER = 'O'

    # Verifica se o jogador é humano ou computador
    def __init__(self, is_human=True):
        self._is_human = is_human

        # Se for humano ele sera o 'X' se for computador 'O'
        if is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    def get_mover(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_human_move()

    def get_human_move(self):
        while True:
            user_input = int(input('Digite o seu movimento (1-9): '))
            move = Move(user_input)  # Classe do modulo move
            if move.is_valid():
                break
            else:
                print('Print digite um numero de 1 a 9')

        return move

    def get_computer_move(self):
        random_choice = random.choice(list(range(1, 10)))
        move = Move(random_choice)
        print(f'Movimento do computador (1-9): {move.value}')
        return move
