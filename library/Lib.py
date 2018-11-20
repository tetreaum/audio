import os
import sys

class Lib:
    """This class creates a library to store media"""
	
    def __init__(self):
        """Initializes the library"""

    def listMedia(self):
        """Prints the name of each media file"""
        files = os.listdir("/home/tetreaum/cis343/cli-audio/audio/media")
        # for name in files:
          #  print(name)
        return files
    def chooseSong(self):
        """Chooses a song from the directory"""
        #return media/songname.wav
