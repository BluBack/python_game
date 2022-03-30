class GameStats():
    """game stats"""
    def __init__(self, game_settings):
        """Initialize statistics"""
        self.game_settings = game_settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """initialize statistics, during the game"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0