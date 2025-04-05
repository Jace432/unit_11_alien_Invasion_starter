"""
Provides the Settings Class for the Alien Invasion Game.

Settings Class stores the games parameters for the screen size, FPS, file paths
for assests, ship settings, bullet settings. 
"""

from pathlib import Path
class Settings:
    """Class for the settings of the Alien Invasion Game"""
    
    def __init__(self):
        """Controls the settings of the game assets; size, sound, images, etc"""
        self.name: str = "Alien Invasion"
        self.screen_w  = 1200
        self.screen_h  = 800
        self.FPS       = 60
        self.bg_file   = Path.cwd() / "Assets" / "images"  / "Starbasesnow.png"
        
        self.ship_file  = Path.cwd() / "Assets" / "images" / "DurrrSpaceShip.png"
        self.ship_w     = 65
        self.ship_h     = 85
        self.ship_speed = 5

        self.bullet_file   = Path.cwd() / "Assets" / "images" / "laserBlast.png"
        self.laser_sound   = Path.cwd() / "Assets" / "sound" / "laser.mp3"
        self.bullet_speed  = 7 
        self.bullet_w      = 25
        self.bullet_h      = 80
        self.bullet_amount = 5
        



