from plates import is_valid
import pytest



def test_length():
    assert is_valid("CS") == True
    assert is_valid("CS502") == True
    assert is_valid("C") == False
    assert is_valid("OUTATIME") == False




def test_start_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C50") == False
    assert is_valid("50") == False



def test_number_rules():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False



def test_punctuation_spaces():
    assert is_valid("CS50.") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS50!") == False
