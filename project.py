import sys
import pygame as pg
from wonderwords import RandomWord
import constants
from constants import GAME_TRIES,CENTER, SCREEN_WIDTH, SCREEN_HEIGHT, OK_BUTTON_COLOR, NO_BUTTON_COLOR, EXIT_BUTTON_COLOR, INFO_COLOR

TRIES = GAME_TRIES

def load_image(file) -> str:  # from aliens example
    """loads an image, prepares it for play"""
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit(f'Could not load image "{file}" {pg.get_error()}')
    return surface.convert()


def fetch_a_word() -> str:
    ''' fetchs a word from api and returns it'''
    get_random = RandomWord()
    return get_random.word(include_parts_of_speech=["nouns", "adjectives"], word_min_length=5, word_max_length=10)


def play():
    '''Returns an object to start play'''
    word = fetch_a_word()
    to_guess = ['_ '] * len(word)
    guess_it = ''.join(to_guess)
    return {
        'word': word,
        'tries': TRIES,
        'to_guess': guess_it,
        'masked': to_guess
    }


def game(word_to_guess: str, tries: int, wip: list, guess: str) -> str:
    '''Returns a string with the word to guess masked'''
    while tries > 0:
        if guess in word_to_guess:
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    wip[i] = letter
            return "".join(wip)


def main():
    '''Main function to run the game'''
    pg.init()

    screen = pg.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_rect = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    tries = GAME_TRIES

    pg.display.set_caption("Guess 'Em or Burst")
    font = pg.font.Font("freesansbold.ttf", 25)

    bg_img = load_image('images/1208.jpg')
    bg_img = pg.transform.scale(
        bg_img, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    background = pg.Surface(screen_rect.size)
    for x in range(0, screen_rect.width, bg_img.get_width()):
        background.blit(bg_img, (x, 0))
    screen.blit(background, (0, 0))

    pg.display.flip()

    baloon_image = load_image('images/balloon.gif')
    baloon_image = pg.transform.scale(baloon_image, (200, 200))

    start_screen = True
    start_button_visible = True
    exit_button_visible = False
    replay_ok = False

    confirm_exit_screen = False

    game_over_screen = False
    game_won_screen = False

    button_width, button_height = 200, 50
    start_button_position = screen.get_rect().centerx - button_width, 400
    exit_button_position = start_button_position[0] + button_width, 400

    word = ''

    def draw_button(text, pos_x, pos_y, color, width, height):
        '''draws a button with given text, color and position'''
        pg.draw.rect(screen, color, (pos_x, pos_y, width, height), 25, 100)
        text_surface = font.render(text, True, ('white'))
        text_rect = text_surface.get_rect(
            center=(pos_x + width // 2, pos_y + height // 2))
        screen.blit(text_surface, text_rect)

    def draw_text_box(text, position, color):
        '''draws a button with given text, color and position'''

        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = position
        screen.blit(text_surface, text_rect)

    def game_over(title: str, subtitle: str):
        '''Print to screen a message with the correct word'''
        screen.blit(background, (0, 0))
        draw_text_box(title, (CENTER[0] - 50,
                      CENTER[1]-200), INFO_COLOR)
        draw_text_box(f"The word was: {subtitle}", (CENTER[0]-100,
                      CENTER[1]-100), INFO_COLOR)
        draw_button(
            "Play again", start_button_position[0],
            start_button_position[1],
            OK_BUTTON_COLOR,
            button_width,
            button_height)
        draw_button("Exit", exit_button_position[0], exit_button_position[1],
                    NO_BUTTON_COLOR, button_width, button_height)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pg.mouse.get_pos()

                if start_screen:
                    if start_button_position[0] <= mouse_pos[0] \
                        <= start_button_position[0] + button_width and \
                            start_button_position[1] <= mouse_pos[1] <= \
                    start_button_position[1] + button_height:
                        exit_button_visible = True
                        start_screen = False
                        start_button_visible = False
                        if not word:
                            result = play()
                            word = result["word"]

                    elif exit_button_position[0] <= mouse_pos[0] <= \
                        exit_button_position[0] + button_width and \
                            exit_button_position[1] <= mouse_pos[1] <= \
                    exit_button_position[1] + button_height:
                        start_screen = False
                        draw_text_box("Are you sure you want to exit?",
                                      (360, 150), EXIT_BUTTON_COLOR)
                        draw_button(
                                    "Yes",
                                    start_button_position[0],
                                    start_button_position[1],
                                    OK_BUTTON_COLOR, button_width, button_height)
                        draw_button(
                            "No", exit_button_position[0],
                            exit_button_position[1], NO_BUTTON_COLOR, button_width, button_height)
                        confirm_exit_screen = True

# TODO check if this is the correct way to do it
                if exit_button_visible and 10 <= mouse_pos[0] <= 10 + button_width and \
                        10 <= mouse_pos[1] <= 10 + button_height:
                    exit_button_visible = False
                    confirm_exit_screen = True

                    if confirm_exit_screen:
                        sys.exit()

            if event.type == pg.KEYDOWN:
                key_pressed = pg.key.name(event.key)

                if key_pressed in word:
                    result["to_guess"] = game(
                        word, 3, result["masked"], key_pressed)
                    if result["to_guess"] == word:
                        game_won_screen = True

                else:
                    tries -= 1
                    if tries == 0:
                        game_over_screen = True

        pg.display.flip()

        if start_screen and start_button_visible:
            draw_button(
                "Start", 
                start_button_position[0],
                start_button_position[1],
                OK_BUTTON_COLOR, button_width, button_height)
            draw_button(
                "Exit", exit_button_position[0],
                exit_button_position[1],
                NO_BUTTON_COLOR, button_width, button_height)

        if exit_button_visible:
            screen.blit(background, (0, 0))

            draw_button("X", 10, 10, EXIT_BUTTON_COLOR, 50, 50)

            for i in range(tries):
                x_position = 50*i + 400
                y_position = 20 if i % 2 == 0 else 30
                screen.blit(baloon_image, (x_position, y_position))

        if confirm_exit_screen:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pg.mouse.get_pos()

                    if exit_button_position[0] <= mouse_pos[0] <= \
                        exit_button_position[0] + button_width and \
                            exit_button_position[1] <= mouse_pos[1] <= \
                                exit_button_position[1] + button_height:
                        confirm_exit_screen = False
                        start_screen = True

                    if start_button_position[0] <= mouse_pos[0] <= \
                        start_button_position[0] + button_width and \
                            start_button_position[1] <= mouse_pos[1] <=\
                                start_button_position[1] + button_height:
                        sys.exit()
        if word:
            draw_text_box(result["to_guess"], (CENTER[0] - 15, 400), (0, 0, 0))

        if game_over_screen:
            game_over("Game Over", word)
            if event.type == pg.QUIT:
                running = False
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pg.mouse.get_pos()

                    if exit_button_position[0] <= mouse_pos[0] <= \
                        exit_button_position[0] + button_width and \
                            exit_button_position[1] <= mouse_pos[1] <= \
                                exit_button_position[1] + button_height:
                        word = ''
                        sys.exit()

                    if start_button_position[0] <= mouse_pos[0] <= \
                        start_button_position[0] + button_width and \
                            start_button_position[1] <= mouse_pos[1] <= \
                                start_button_position[1] + button_height:

                        word = ''

                        game_over_screen = False
                        start_screen = True
                        screen.blit(background, (0, 0))
                        exit_button_visible = True
                        if not word:
                            result = play()
                            word = result["word"]
                        tries = GAME_TRIES

                        if event.type == pg.KEYDOWN:
                            key_pressed = pg.key.name(event.key)
                            if key_pressed in word:
                                result["to_guess"] = game(
                                    word, 3, result["masked"], key_pressed)
                                if result["to_guess"] == word:
                                    game_won_screen = True

                            else:
                                tries -= 1
                                if tries == 0:
                                    print("perdiste")
                                    game_over_screen = True
        if game_won_screen:
            game_over("You WIN!", word)
            if event.type == pg.QUIT:
                running = False
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pg.mouse.get_pos()

                    if exit_button_position[0] <= mouse_pos[0] <= exit_button_position[0] + button_width and \
                            exit_button_position[1] <= mouse_pos[1] <= exit_button_position[1] + button_height:
                        word = ''
                        sys.exit()

                    if start_button_position[0] <= mouse_pos[0] <= start_button_position[0] + button_width and \
                            start_button_position[1] <= mouse_pos[1] <= start_button_position[1] + button_height:

                        word = ''

                        game_won_screen = False
                        start_screen = True
                        screen.blit(background, (0, 0))
                        exit_button_visible = True
                        if not word:
                            result = play()
                            word = result["word"]
                        tries = GAME_TRIES
                        print(
                            f'WORD3: {word} start_Scrree{replay_ok} running{running}')
                        exit_button_visible = True
                        if event.type == pg.KEYDOWN:
                            key_pressed = pg.key.name(event.key)

                            if key_pressed in word:
                                result["to_guess"] = game(
                                    word, 3, result["masked"], key_pressed)
                                if result["to_guess"] == word:
                                    game_won_screen = True

                            else:
                                tries -= 1
                                if tries == 0:
                                    game_over_screen = True
    pg.quit()


if __name__ == "__main__":
    main()
    pg.quit()
