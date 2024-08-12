import pygame
import PIL
import cv2
import moviepy
import pydub
import tkinter as tk
from importlib.metadata import version

def check_installation():
    print("✅ Pygame version:", pygame.__version__)  # Perbaiki typo di sini
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    print("✅ MoviePy version:", version("moviepy"))
    print("✅ Pydub version:", version("pydub"))
    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()
