from Spell import Spell


class FlameBurst(Spell):
    def __init__(self):
        super().__init__(self, "fire", 8, 2, "Flame Burst")


class SunBolt(Spell):
    def __init__(self):
        super().__init__(self, "fire", 16, 6, "Sun Bolt")


class InfernoWave(Spell):
    def __init__(self):
        super().__init__(self, "fire",34, 18, "Inferno Wave")
