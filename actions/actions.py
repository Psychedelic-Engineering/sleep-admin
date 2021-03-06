import time, logging
from audio.playlist import PlaylistSoundCloud


def doAlarm(sleepApp):
	import random
	for i in range(1):
		start = time.time()

		warm = 0.0
		cold = 0.0

		while warm <= 0.4:
			sleepApp.led.setLum(warm, cold)
			time.sleep(0.3)
			warm += 0.0005

		while cold <= 0.2:
			sleepApp.led.setLum(warm, cold)
			time.sleep(0.3)
			cold += 0.0005
		cnt = 0.01
		len = 0.01

		while time.time() < start + 400:
			if random.random() < cnt:
				sleepApp.led.setLum(1, 1)
				time.sleep(len)
				if len <= 0.1:
					len += 0.0005
				sleepApp.led.setLum(warm, cold)
			time.sleep(0.1)
			if cnt <= 0.15:
				cnt += 0.0002

		t = 20
		while t >= 0:
			sleepApp.led.setLum(1, 1)
			time.sleep(20-t)
			sleepApp.led.setLum(0, 0)
			time.sleep(t)
			t -= 1

	sleepApp.led.setLum(0, 0)


def fallasleep(sleepApp):
	soundTrack = PlaylistSoundCloud()
	#soundTrack.loadPlaylistByTags(("morning",))
	soundTrack.loadPlaylistByName("Own")
	soundTrack.printPlaylist()

	soundTrack.setVolume(0)

	soundTrack.play()

	while soundTrack.playing:
		time.sleep(10)



	soundTrack.stop()