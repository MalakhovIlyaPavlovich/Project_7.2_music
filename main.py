'''
Done by Ilya Malakhov
Так как я не знаком с многопоточным программированием, я не реализовал остановку проигрывающегося трека.
'''


from track import Track, Album

def tracks_inp(min, max):
    tracks = input().split()
    while True:
        try:
            tracks = list(map(int, tracks))
            for x in tracks:
                if x < min or x > max:
                    break
            else:
                break
        except ValueError:
            pass
        tracks = input().split()
    return tracks

with open('tracks.txt', encoding='utf-8') as f:
    tracks = []
    for line in f:
        tracks.append(Track(*line.split(';')))
    album = Album('Тестовый альбом', '2020', *tracks)
    print(album)

    print('Какие треки вы хотите прослушать?')
    print('Введите номера треков через пробел:')
    number_of_tracks = tracks_inp(1, len(album.tracks))
    for x in number_of_tracks:
        album.tracks[x - 1].play()
