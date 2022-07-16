from events import base_events, algorithm_events
from models import base_models, algorithm_models
from display import Display, GridDisplay
from game import Game


# Display and Game
display = GridDisplay(
    cell_size=20,
    rows=25,
    columns=25,
)
# display = Display()
game = Game(display)

# objects
example_model = base_models.EXAMPLE_MODEL
player = base_models.PLAYER
#game.add_object(player, example_model)
#game.add_object(base_models.FOOD)
#game.add_object(algorithm_models.self_avoiding_walker)

# events
keyboard = base_events.ARROW_KEYS
game.add_event(keyboard)
game.add_event(algorithm_events.game_of_life)

# game main loop
game.loop()
