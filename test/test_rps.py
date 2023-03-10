class Player:
    def choose(self):
        raise NotImplementedError('subclass must implement this method')

class Game():
    def __init__(self, player1: Player, player2: Player):
        self._player1 = player1
        player2.choose()
        

    def start(self):
        self._player1.choose()

########

class MockPlayer(Player):
    def __init__(self):
        self._choose_was_called = False

    def choose(self):
        self._choose_was_called = True

    def methodChooseWasCalled(self) -> bool:
        return self._choose_was_called


def when_game_is_created(player1=None, player2=None) -> Game:
    player1 = player1 or MockPlayer()
    player2 = player2 or MockPlayer()
    return Game(player1, player2)

def test_does_not_ask_player_to_choose_until_game_starts():
    my_player = MockPlayer()

    game = when_game_is_created(player1=my_player)

    assert not my_player.methodChooseWasCalled()


def test_asks_p1_to_choose_an_option():
    # given
    # precodiciones  ..
    my_player = MockPlayer()

    # when
    game = when_game_is_created(player1=my_player)
    game.start()

    # then
    assert my_player.methodChooseWasCalled()


def test_asks_p2_to_choose_an_option():
    # given
    # precodiciones  ..
    my_player = MockPlayer()
    
    # when
    game = when_game_is_created(player2=my_player)
    game.start()

    # then
    assert my_player.methodChooseWasCalled()