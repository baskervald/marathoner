from crunchyroll.apis.meta import MetaApi
from subprocess import Popen
from livestreamer import streams
import os

crunchyroll = MetaApi()
episodes = crunchyroll.list_media(crunchyroll.search_anime_series(raw_input('Anime name: '))[0])
length = len(episodes)

def prompt (episodeNumber):
  print 'Play episode ' + str(episodeNumber + 1) +' (y/n/r/s)?',
  response = raw_input()
  if response == 'y':
    print 'Playing episode ' + str(episodeNumber)
    playEpisode(episodeNumber + 1)
  elif response == 'r':
    print 'Repeating episode ' + str(episodeNumber)
    playEpisode(episodeNumber)
  elif response == 's':
    print 'Skipped.'
    prompt(episodeNumber + 1)
  else:
    print 'Thanks for watching'

def playEpisode(episodeNumber):
  episode = episodes[length-episodeNumber]
  streamlist = streams(episode.url)
  qualities = []
  for quality in streamlist:
    qualities.append(quality)
  print 'Choose quality (' + ' '.join(qualities) + '):',
  response = raw_input()
  with open(os.devnull, 'w') as f:
    proc = Popen(['mpv', '--fullscreen', '--cache=4096', streamlist[response].url], stdout=f)
    proc.wait()
    prompt(episodeNumber)
    
playEpisode(int(raw_input('Episode number: ')))