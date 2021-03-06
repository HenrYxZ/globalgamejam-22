from constants import GLOBAL_VOLUME


def play(sound, volume=GLOBAL_VOLUME):
    player = sound.play()
    player.volume = volume
    return player

def humanize_time(secs):
    """
    Extracted from http://testingreflections.com/node/6534
    """
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)