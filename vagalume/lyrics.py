# pip install vagalume
from vagalume import lyrics
result = lyrics.find('Legiao Urbana', 'Faroeste Caboclo')
print(result.song.lyric)