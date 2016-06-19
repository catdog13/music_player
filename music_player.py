import subprocess
import random
import os
song_list = []


def make_list(list_path):
    for root, subdir, files in os.walk(list_path):
        for songs in files:
            if songs.endswith('.flac'):
                full_path = os.path.join(root, songs)
                song_list.append(full_path)


def player(song_path):
    mplayer = r'C:\Users\Tom\Documents\Python_Projects\music_player\MPlayer\mplayer.exe'
    process = '{} "{}"'.format(mplayer, song_path)
    subprocess.Popen(process, stdout=subprocess.PIPE).stdout.read()


if __name__ == '__main__':
    make_list('D:\\Music\\foobar2000\\')
    print('Press Enter to skip current song and Space bar to pause')
    while True:
        random.shuffle(song_list)
        for path in song_list:
            path_parts = path.split(os.sep)
            artist = path_parts[3]
            album = path_parts[4]
            song_name = os.path.splitext(path_parts[5])[0]
            print('Artist: {} - Album: {} - Song: {}'.format(artist, album, song_name))
            player(path)
