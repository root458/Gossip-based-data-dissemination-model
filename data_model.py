
class Data:

    def __init__(self):
        self.__items = [0, 0, 0, 0, 0]
        self.__version = 0

    def update_data(self, new_items):
        self.__items = new_items
        self.__version += 1

    def get_data(self):
        return self.__items

    def get_version(self):
        return self.__version
