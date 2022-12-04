from time import sleep
from pytube import Playlist, YouTube, Channel, exceptions
from pytube.cli import on_progress
from urllib.error import HTTPError

key_api = 'AIzaSyCQFiamta-FFWg3sXeOnL4Xn9j_JwI9ZSA'

print('Program zapisuje filmy do katalogu w którym zostanie uruchomiony.')
while True:
    print('''
Co chcesz zrobić?
1 - Ściągnąć film
2 - Ściągnąć playlistę
3 - Ściągnąć cały kanał
Twój wybór to liczba:
    ''')
    choice = input()
    if choice == '1':
        link = input('Wklej link wideo do ściągnięcia:\n')
        try:
            video = YouTube(link)
        except exceptions.VideoUnavailable:
            print(f'Nie można pobrać wideo {video.title}..')
            continue
        except exceptions.RegexMatchError:
            print('Nieprawidłowy link')
            continue
        except HTTPError:
            print("HTTPError")
        else:
            print(video.title)
            video.register_on_progress_callback(on_progress)
            video.streams.get_highest_resolution().download()
            sleep(2)
            print('\nPobieranie wideo ' + video.title + ' zostało ukończone.\n')
        break
    elif choice == '2':
        link = input('Wklej link playlisty do ściągnięcia:\n')
        try:
            playlist = Playlist(link)
        except exceptions.RegexMatchError:
            print('Nieprawidłowy link')
            continue
        else:
            print('Liczba filmów w playliście: ' + str(len(playlist.video_urls)))
            print('--------------------------------------------')
            for count, video in enumerate(playlist.videos):
                try:
                    print('Ściąganie filmu ' + video.title + '...' + f'({count + 1}/{len(playlist.videos)})')
                    video.register_on_progress_callback(on_progress)
                    video.streams.get_highest_resolution().download()
                    sleep(2)
                except exceptions.VideoUnavailable:
                    print(f'Nie można pobrać wideo {video.title}. Pomijam.')
                except exceptions.RegexMatchError:
                    print('Nieprawidłowy link')
                    continue
                except exceptions.ExtractError:
                    print('ExtractError')
                except exceptions.PytubeError:
                    print('PyTube Error')
                except exceptions.AgeRestrictedError:
                    print('wiek')
                except exceptions.HTMLParseError:
                    print('HTMLParseError')
                except exceptions.VideoPrivate:
                    print('VideoPrivate')
                except HTTPError:
                    print(f"HTTPError '{video.title}'")
            print('\nPobieranie playlisty ' + playlist.title + ' zostało ukończone.\n')
            break
    elif choice == '3':
        link = input('Wklej link kanału do ściągnięcia:\n')
        try:
            channel = Channel(link)
        except exceptions.RegexMatchError:
            print('Nieprawidłowy link')
            continue
        else:
            print('Kanał: ' + channel.channel_name)
            print('Liczba filmów: ' + str(len(channel.video_urls)))
            print('--------------------------------------------')
            for count, video in enumerate(channel.videos):
                try:
                    print('Ściąganie filmu ' + video.title + '...' + f'({count + 1}/{len(channel.videos)})')
                    video.register_on_progress_callback(on_progress)
                    video.streams.get_highest_resolution().download()
                    sleep(2)
                except exceptions.VideoUnavailable:
                    print(f'Nie można pobrać wideo {video.title}. Pomijam.')
                except exceptions.RegexMatchError:
                    print('Nieprawidłowy link')
                    continue
                except exceptions.ExtractError:
                    print('ExtractError')
                except exceptions.PytubeError:
                    print('PyTube Error')
                except exceptions.AgeRestrictedError:
                    print('wiek')
                except exceptions.HTMLParseError:
                    print('HTMLParseError')
                except exceptions.VideoPrivate:
                    print('VideoPrivate')
                except HTTPError:
                    print(f"HTTPError '{video.title}'")
            print('\nPobieranie kanału ' + channel.channel_name + ' zostało ukończone.\n')
            break
    else:
        print('Wybierz 1, 2 lub 3\n')