# Sound.py

from pygame import *
mixer.init()

class Sound:
	def __init__(self, sound_track):
		self.track_name = sound_track

	def execute(self, repeat = -1, start = 0.0):
		"play music"
		mixer.music.load(self.track_name)
		mixer.music.play(repeat, start)

	def halt(self):
		"stop music"
		mixer.music.fadeout(300)