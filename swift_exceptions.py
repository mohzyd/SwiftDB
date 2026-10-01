class Invalid_Key(Exception):
    def __init__(self):
        super().__init__("Key is invalid.")

class No_Loaded_Database(Exception):
    def __init__(self):
        super().__init__("Please load a database. You can use .load() before attempting to use any command.")

class Empty_Database(Exception):
    def __init__(self):
        super().__init__("Empty database. There is nothing to delete")

class No_Database(Exception):
    def __init__(self):
        super().__init__("There is no database with such name. Please create it using the .load() command.")

class Missing_Args(Exception):
    def __init__(self):
        super().__init__("The method is missing critical arguments.")

class Missing_Database_Name(Exception):
    def __init__(self):
        super().__init__("Missing Database Name. Please specify a name.")