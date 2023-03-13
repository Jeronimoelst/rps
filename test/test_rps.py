class Player:
    def choose(self):
        raise NotImplementedError('subclass must implement this method')
    
    def winner(self):
        raise NotImplementedError('subclass must implement this method')


class Game():
    def __init__(self, player1: Player, player2: Player):
        self._player1 = player1
        self._player2 = player2
        

    def start(self):
        player1_choice = self._player1.choose()
        if player1_choice == 'rock':
            self._player1.winner()
        else:
            self._player2.winner()

        

########

class MockPlayer(Player):
    def __init__(self):
        self._choose_was_called = False
        self._winner_was_called = False

        self._next_choice = ''

    def choose(self):
        self._choose_was_called = True
        return self._next_choice
    
    def winner(self):
        self._winner_was_called = True


    def method_choose_was_called(self) -> bool:
        return self._choose_was_called
    
    def method_winner_was_called(self) -> bool:
        return self._winner_was_called
    
    def choose_rock(self):
        self._next_choice = 'rock'
    def choose_scissors(self):
        self._next_choice = 'scissors'


def when_game_is_created(player1=None, player2=None) -> Game:
    player1 = player1 or MockPlayer()
    player2 = player2 or MockPlayer()
    return Game(player1, player2)

def test_does_not_ask_player_to_choose_until_game_starts():
    my_player = MockPlayer()

    game = when_game_is_created(player1=my_player, player2=my_player)

    assert not my_player.method_choose_was_called()


def test_asks_p1_to_choose_an_option():
    # given
    # precodiciones  ..
    my_player = MockPlayer()

    # when
    game = when_game_is_created(player1=my_player)
    game.start()

    # then
    assert my_player.method_choose_was_called()


def test_asks_p2_to_choose_an_option():
    # given
    # precodiciones  ..
    my_player = MockPlayer()
    
    # when
    game = when_game_is_created(player2=my_player)
    game.start()

    # then
    assert my_player.method_choose_was_called()

def test_player1_wins():
    my_player1 = MockPlayer()
    my_player2 = MockPlayer()
    my_player1.choose_rock()
    my_player2.choose_scissors()

    game = when_game_is_created(player1=my_player1, player2=my_player2)
    game.start()
    
    assert my_player1.method_winner_was_called()
    assert not my_player2.method_winner_was_called()


def test_player2_wins():
    my_player1 = MockPlayer()
    my_player2 = MockPlayer()
    my_player1.choose_scissors()
    my_player2.choose_rock()

    game = when_game_is_created(player1=my_player1, player2=my_player2)
    game.start()
    
    assert not my_player1.method_winner_was_called()
    assert my_player2.method_winner_was_called()

    


