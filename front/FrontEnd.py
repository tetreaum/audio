import curses
import curses.textpad
import sys
from exception import exception as e

class FrontEnd:

    """Initializes the front end of the audio player"""
    def __init__(self, player, lib):
        self.player = player
        self.lib = lib
        self.player.play(sys.argv[1])
        curses.wrapper(self.menu)
    
    """Creates the menu for the audio player"""
    def menu(self, args):
        self.stdscr = curses.initscr()
        self.stdscr.border()
        # Checking the size of the screen
        size = self.stdscr.getmaxyx()
        height = size[0]
        width = size[1]
        if (width < 5) or (height < 5):
            raise e.CLI_Audio_Screen_Size_Exception("Screen is too small")
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - Library")
        self.stdscr.addstr(9,10, "ESC - Quit")
        self.updateSong()
        self.stdscr.refresh()
        while True:
            c = self.stdscr.getch()
            if c == 27:
                self.quit()
            elif c == ord('p'):
                self.player.pause()
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('l'):
                files = self.lib.listMedia()
                x = 16
                for f in files:
                    self.stdscr.addstr(x, 10, f)
                    x+=1
    
    """Updates the screen, shows the song currently playing"""
    def updateSong(self):
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(15,10, "Now playing: " + self.player.getCurrentSong())
        # self.stdscr.addstr(16,0, "                                        ")

    """Changes the song"""
    def changeSong(self):
        changeWindow = curses.newwin(5, 40, 5, 50)
        changeWindow.border()
        changeWindow.addstr(0,0, "What is the file path?", curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(1,1, 30)
        curses.noecho()
        del changeWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.player.stop()
        self.player.play(path.decode(encoding="utf-8"))
        
    """Exits the audio player"""
    def quit(self):
        self.player.stop()
        exit()
