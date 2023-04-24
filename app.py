#(Download from youtube)#
def ytdl():
    try:
        import os
        from pytube import YouTube
        from pytube.request import URLError
        from pytube.exceptions import RegexMatchError
        from colorama import Fore
        import glob
    except ImportError as e:
        print('')
        print(" SEEMS LIKE SOME PACKAGES ARE MISSING..USE THE FOLLOWING COMMAND:")
        print('')
        print('=> pip install -r requirements.txt')
        quit()
    def progress(streams, chunk: bytes, bytes_remaining: int):
        contentsize = stream.filesize
        size = contentsize - bytes_remaining
        print( Fore.GREEN + '\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='') 

    while True:
        try:
            os.system('clear')
            print()
            print(Fore.WHITE + '     |ytdl.nin|•|INeT-NiNjA|')
            print()
            link = input(Fore.CYAN + " [ENTER THE LINK OF THE YOUTUBE VIDEO] \n => ")
            yt = YouTube(link,on_progress_callback=progress)
            print()
            print(Fore.YELLOW + ' ' + yt.title)
            break
        except URLError:
            print(Fore.RED + ' ** You are not connected to the internet!! **')
            quit()
        except RegexMatchError:
            print(Fore.RED + ' ** The link is not valid **')
        except KeyboardInterrupt:
            print(Fore.RED + ' ** Quitting the program **')
            quit()
        except:
            print(Fore.RED + ' ** Error..Please try again!! **')

    while True:
        print('')
        print(Fore.CYAN + ' [1] DOWNLOAD VIDEO')
        print(Fore.CYAN + ' [2] DOWNLOAD AS AUDIO')
        print(Fore.CYAN + ' [3] DOWNLOAD/VIEW THUMBNAIL')
        print(Fore.CYAN + ' [4] RETURN TO MAIN MENU')
        print('')
        try:
            choice = int(input(Fore.CYAN + ' [WHAT DO YOU WANT TO DO?]\n => '))
        except ValueError:
            choice = 5

        if choice < 1 or choice > 4:
            print(Fore.RED + " ** Please select a valid option!! **")
            continue
        if choice == 1:
            try:
                os.makedirs('downloaded/videos',exist_ok=True)
                print('')
                stream = yt.streams.get_by_itag(22)
                stream.download('downloaded/videos')
                break
            except:
                print(Fore.RED + " ** An error occured!! **")
            
        if choice == 2:
            try:
                os.makedirs('downloaded/music',exist_ok=True)
                print('')
                stream = yt.streams.get_by_itag(140)
                stream.download('downloaded/music')
                for filename in glob.iglob(os.path.join('downloaded/music', '*.mp4')):
                    os.rename(filename, filename[:-4] + '.mp3')
                break
            except:
                print(Fore.RED + " ** An error occured!! **")
        if choice == 3:
            try:
                print('')
                print(Fore.CYAN + ' [OPEN THIS LINK IN BROWSER TO ACCESS THUMBNAIL]')
                print('')
                print(Fore.YELLOW + yt.thumbnail_url)
                break
            except:
                print( Fore.RED + ' ** An error occured!! **')
        if choice ==4:
            youtubedl()
        if KeyboardInterrupt:
            print(Fore.RED + ' ** Quitting the program **')
            break

















#(Main program)#
ytdl()
