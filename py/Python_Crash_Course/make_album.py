def make_album(singer,album,song = ''):
    if song:
        mk = {'singer_name':singer,'album_name':album,'song_number':song}
    else:
        mk = {'singer_name':singer,'album_name':album}
    return print(mk)

make_album('cyx','wdg')
make_album('zjl','nzhm',10)
print('\n')
print('\n')

##This code is for exercise 8-8
active = True
while active:
    singer = input("Please enter a singer's name(enter 'q' to quit): ")
    if singer != 'q':
        album = input("Please enter one this singer's album(enter 'q' to quit): ")
    else:
        break

    if singer == 'q' or album == 'q':
        active = False
    else:
        make_album(singer,album)
        print('\n')
                   

