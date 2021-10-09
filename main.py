
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
  'outtmpl':'Music.',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        
    }],
}

strong = input('Enter yt link here : ')
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([strong])

from pygame import mixer
  
# Starting the mixer
mixer.init()
  
# Loading the song
mixer.music.load("Music.wav")
  
# Setting the volume
mixer.music.set_volume(0.7)
  
# Start playing the song
mixer.music.play()