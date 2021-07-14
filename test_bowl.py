import pytest
from unittest import mock

import bowl


PERFECT_GAME = ['10'] * 12
PERSONAL_BEST_GAME = ["10", "8", "2", "6", "2", "9", "1", "10", "10",
                         "10", "9", "0", "7", "1", "10", "7", "3"]
CLEAN_GAME = ['10', '9', '1', '10', '8', '2', '10', '5', '5',
              '10', '7', '3', '10', '9', '1', '10']
POOR_GAME = ["6", "0", "0", "5", "0", "0", "9", "0", "8", "2", "1",
             "4", "6", "2", "0", "1", "9", "0", "4", "4"]


class TestFrames:

    @mock.patch('builtins.input', side_effect=['4', '3'])
    def test_open_frame(self, mock_input): 
            frame = bowl.Frame(1)

            pins = frame.get_roll_score()
            frame.add_roll(pins)
            pins = frame.get_roll_score()
            frame.add_roll(pins)

            assert frame.rolls == [4, 3]
            assert not frame.is_strike()
            assert not frame.is_spare()
            assert frame.score() == 7

    @mock.patch('builtins.input', side_effect=['9', '1'])
    def test_spare(self, mock_input): 
            frame = bowl.Frame(1)

            pins = frame.get_roll_score()
            frame.add_roll(pins)
            pins = frame.get_roll_score()
            frame.add_roll(pins)

            assert frame.rolls == [9, 1]
            assert not frame.is_strike()
            assert frame.is_spare()
            assert frame.score() == 10

    @mock.patch('builtins.input', side_effect=['10'])
    def test_strike(self, mock_input):    
        frame = bowl.Frame(1)

        pins = frame.get_roll_score()
        frame.add_roll(pins)

        assert frame.rolls == [10]
        assert frame.is_strike()
        assert not frame.is_spare()
        assert frame.score() == 10

    def test_frame_invalid_input(self):
        with mock.patch('builtins.print') as mock_print:
            with mock.patch('builtins.input', side_effect=['X', '10']) as mock_input:
                frame = bowl.Frame(1)
                pins = frame.get_roll_score()
                frame.add_roll(pins)
                assert frame.rolls == [10]
                assert frame.is_strike()


class TestGame:

    @mock.patch('builtins.input', side_effect=PERFECT_GAME)
    def test_perfect_game(self, mock_input):
        game = bowl.Game()
        game.start_bowling()
        assert game.current_score() == 300

    @mock.patch('builtins.input', side_effect=PERSONAL_BEST_GAME)
    def test_personal_best_game(self, mock_input):
        with mock.patch('builtins.print') as mock_print:
            game = bowl.Game()
            game.start_bowling()
            assert game.current_score() == 179

    @mock.patch('builtins.input', side_effect=CLEAN_GAME)
    def test_clean_game(self, mock_input):
        game = bowl.Game()
        game.start_bowling()
        assert game.current_score() == 200

    @mock.patch('builtins.input', side_effect=POOR_GAME)
    def test_poor_game(self, mock_input):
        game = bowl.Game()
        game.start_bowling()
        assert game.current_score() == 62

