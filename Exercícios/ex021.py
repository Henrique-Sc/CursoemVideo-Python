from pygame import mixer

mixer.init()

input('Pressione enter para começar a música: ')
mixer.music.load('Exercícios\ex021_music1.mp3')
mixer.music.play()

input('Pressione enter para começar a próxima música: ')
mixer.music.load('Exercícios\ex021_music2.mp3')
mixer.music.play()

input('Pressione Enter para parar a música: ')

print('--- Programa finalizado ---')
