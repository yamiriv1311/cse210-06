import pyray

class VideoServices:
    """ This is in charge of the displaying of the game """

    def __init__(self,width,height,gameName,frameNumber,cellsize,debug=False):
        self._width = width
        self._height = height
        self._game_name = gameName
        self._frame_nummber = frameNumber
        self._cell_size = cellsize
        self._debug = debug

    def open_window(self):
        """ Opens a window """
        pyray.init_window(self._width, self._height, self._game_name)
        pyray.set_target_fps(self._frame_nummber)

    def close_window(self):
        """ closes the window """
        pyray.close_window()

    def is_playing(self):
        """ 
            checks if the windows has not been closed
            return:bool
        """
        return not pyray.window_should_close()
        
    def start_drawing(self):
        """ This ist the open section to start drawing """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        
        if self._debug == True:
            self._draw_grid()
        
    def stop_drawing(self):
        """ This is the end of the drawing section"""
        pyray.end_drawing()

    def draw_character(self,item):
        """ This draws a character """
        for i in item.get_appearance():
            pyray.draw_text(i,item.get_x_position(),item.get_y_position(), item.get_font_size(),item.get_color())

    def draw_all_characters(self,characters):
        """ This draws many characters """
        for character in characters:
            self.draw_character(character)
    
    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)

        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)
    
    def draw_banner(self,banner):
        pyray.draw_text(banner.get_message(),banner.get_x_position(),banner.get_y_position(),banner.get_font_size(),banner.get_color())

    def draw_all_banners(self,characters):
        for banner in characters:
            self.draw_banner(banner)
        