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


def player(player_path):
    dlc_path = r'C:\Users\Tom\Documents\Python_Projects\music_player\dlcplayer\dlc.exe'
    process = dlc_path + ' -w "' + player_path + '"'
    subprocess.Popen(process, stdout=subprocess.PIPE).stdout.read()


if __name__ == '__main__':
    make_list('D:\\Music\\foobar2000')
    while True:
        random.shuffle(song_list)
        for path in song_list:
            artist = path.split('\\')[3]
            album = path.split('\\')[4]
            song_name = path.split('\\')[5]
            print('Artist: ' + artist + ' - Album: ' + album + ' - Song: ' + song_name[:-5])
            player(path)
