class Action:
    """A thing that is done.
    
    The responsibility of action is to do somthing that is integral or important in the game. Thus,
    it has one method, execute(), which should be overridden by derived classes.
    """

    def execute(self):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.
        """
        pass