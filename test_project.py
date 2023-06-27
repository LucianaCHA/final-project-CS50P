import project
from constants import GAME_TRIES

def test_fetch_a_word():
    '''
    test for fetch a word function
    shoul return a string of five or more characters
    '''
    assert isinstance(project.fetch_a_word()) == str
    assert len(project.fetch_a_word()) >= 5
    assert len(project.fetch_a_word()) <= 10

def test_play():
    '''
    should return a dict 
    '''
    result = project.play()

    assert isinstance(result, dict)
    assert 'word' in result
    assert 'tries' in result
    assert 'to_guess' in result
    assert 'masked' in result

    assert isinstance(result['word'], str)
    assert isinstance(result['tries'], int)
    assert isinstance(result['to_guess'], str)
    assert isinstance(result['masked'], list)
    assert len(result['to_guess'])//2 == len(result['word'])
    assert result['tries'] == GAME_TRIES

    assert set(result['to_guess']) == set('_ ')

    assert result['word'] != ''

def test_game_guessing():
    '''
    should check  if a char is in the guuess to word, if it does should add it'''
    assert project.game('lemon', 3, ['_','_','_','_','_'],'l' ) == 'l____'
    assert project.game('other', 3, ['_','_','_','_','_'],'h' ) == '__h__'
    assert project.game('animal', 3, ['_','_','_','_','_','_'],'a' ) == 'a___a_'
    assert project.game('animal', 3, ['a','_','_','_','a','_'],'i' ) == 'a_i_a_'

def test_game_no_guessing():
    '''if character does not match, wont add it '''
    assert project.game('lemon', 3, ['_','_','_','_','_'],'x' ) == '_____'
    assert project.game('other', 3, ['_','_','h','_','_'],'z' ) == '__h__'
    assert project.game('animal', 3, ['a','_','_','_','a','_'],'c' ) == 'a___a_'
