from pygame import *
mixer.init()

class soundTracks:
	def __init__(self, sound_track):
		self.track_name = sound_track
	def execute(self, repeat):
		mixer.music.load(self.track_name)
		mixer.music.play(repeat, 0.0)