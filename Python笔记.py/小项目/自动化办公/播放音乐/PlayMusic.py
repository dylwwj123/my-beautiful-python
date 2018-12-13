#超简单播放
import time
import pygame

path1 = r"/Users/wangwenshuai/my-beautiful-python/Python笔记.py/小项目/自动化办公/播放音乐/影子传说.Mp3"

pygame.mixer.init()

track = pygame.mixer.music.load(path1)

pygame.mixer.music.play()

time.sleep(10)

# pygame.mixer.music.pause()

pygame.mixer.music.stop()

#demo