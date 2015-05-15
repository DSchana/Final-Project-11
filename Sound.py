# Sound.py

from pygame import *
mixer.init()

class Sound:
	def __init__(self, sound_track):
		self.track_name = sound_track

	def execute(self, repeat, start = 0.0):
		mixer.music.load(self.track_name)
		mixer.music.play(repeat, start)