class Move:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    # Verifica se o valor está entre 1 e 9
    def is_valid(self):
        return 1 <= self._value <= 9

    # Função para obter a linha
    def get_row(self):
        if self._value in (1, 2, 3):  # Tupla
            return 0  # Primeira linha
        elif self._value in (4, 5, 6):
            return 1  # Segunda linha
        elif self._value in (7, 8, 9):
            return 2  # Terceira linha
        else:
            print('numero inválido\n\n')

    # Função para obter coluna
    def get_column(self):
        if self._value in (1, 4, 7):
            return 0  # Primeira coluna
        elif self._value in (2, 5, 8):
            return 1  # Segunda coluna
        else:
            return 2  # Terceira coluna


#         col0 col1 col2
# linha 0: | 1 | 2 | 3 |
# linha 1: | 4 | 5 | 6 |
# linha 2: | 7 | 8 | 9 |
