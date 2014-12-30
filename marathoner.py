from crunchyroll.apis.meta import MetaApi
from subprocess import Popen
from livestreamer import streams
import os

crunchyroll = MetaApi()
episodes = crunchyroll.list_media(crunchyroll.search_anime_series(raw_input('Anime name: '))[0])
length = len(episodes)

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
    print 'Play episode ' + str(episodeNumber + 1) +' (y/n/r)?',
    response = raw_input()
    if response == 'y':
      playEpisode(episodeNumber + 1)
    elif response == 'r':
      playEpisode(episodeNumber)
    else:
      print 'Thanks for watching'
    
playEpisode(int(raw_input('Episode number: ')))