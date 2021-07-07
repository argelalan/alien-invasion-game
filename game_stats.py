class GameStats:
    """Class that manages game statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize scoreboard attributes."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Reset game statistics for new game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
