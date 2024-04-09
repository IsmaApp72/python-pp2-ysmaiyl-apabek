import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame Music Player")
playlist = ['track1.mp3', 'track2.mp3', 'track3.mp3']  
current_track = 0
pygame.mixer.init()
pygame.mixer.music.load(playlist[current_track])
pygame.mixer.music.play(-1)  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: 
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n: 
                current_track = (current_track + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play(-1)
            elif event.key == pygame.K_b: 
                current_track = (current_track - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play(-1)
    screen.fill((30, 30, 30))
    pygame.display.flip()
pygame.quit()

