import pygame
import os

pygame.init()

screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Music Player")

music_folder = "music"
music_files = [os.path.join(music_folder, filename) for filename in os.listdir(music_folder) if filename.endswith(".mp3")]

current_track_index = 0
is_playing = False

def play_music(index):
    pygame.mixer.music.load(music_files[index])
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pause_music()
                    is_playing = False
                else:
                    unpause_music()
                    is_playing = True
            elif event.key == pygame.K_n:
                current_track_index = (current_track_index + 1) % len(music_files)
                stop_music()
                play_music(current_track_index)
                is_playing = True
            elif event.key == pygame.K_p:
                current_track_index = (current_track_index - 1) % len(music_files)
                stop_music()
                play_music(current_track_index)
                is_playing = True

    screen.fill((255, 255, 255))

    font = pygame.font.SysFont(None, 30)
    text = font.render(os.path.basename(music_files[current_track_index]), True, (0, 0, 0))
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, 50))

    instructions = font.render("Press SPACE to play/pause, N to play next track, P to play previous track", True, (0, 0, 0))
    screen.blit(instructions, (screen_width // 2 - instructions.get_width() // 2, 100))

    pygame.display.flip()

pygame.quit()
