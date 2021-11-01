class CustomList(list):
    def __add__(self, x: list):
        #checking if incorrect types
        if not isinstance(x, list):
            raise TypeError("can only add one list (not " + str(type(x)) + ") to another list")
        #create instance to return
        result_list = CustomList()
        result_list.extend(self)
        #extend first list if it's shorter
        dif = self.__len__() - x.__len__()
        if dif < 0:
            result_list.extend([0 for i in range(0,-dif)])
        #get sum
        for i in range(0, x.__len__()):
            result_list.__setitem__(i, result_list.__getitem__(i) + x.__getitem__(i))
        return result_list

    def __radd__(self, x: list):
        if not isinstance(x, list):
            raise TypeError("can only add one list (not " + str(type(x)) + ") to another list")
        result_list = CustomList()
        result_list.extend(self)
        dif = self.__len__() - x.__len__()
        if dif < 0:
            result_list.extend([0 for i in range(0,-dif)])
        for i in range(0, x.__len__()):
            result_list.__setitem__(i, result_list.__getitem__(i) + x.__getitem__(i))
        return result_list

    def __sub__(self, x: list):
        if not isinstance(x, list):
            raise TypeError("can only subtract one list (not " + str(type(x)) + ") from another list")
        result_list = CustomList()
        result_list.extend(self)
        dif = result_list.__len__() - x.__len__()
        if dif < 0:
            result_list.extend([0 for i in range(0,-dif)])
        for i in range(0, x.__len__()):
            result_list.__setitem__(i, result_list.__getitem__(i) - x.__getitem__(i))
        return result_list
    
    def __rsub__(self, x: list):
        if not isinstance(x, list):
            raise TypeError("can only subtract one list (not " + str(type(x)) + ") from another list")
        result_list = CustomList()
        result_list.extend(x)
        dif = result_list.__len__() - self.__len__()
        if dif < 0:
            result_list.extend([0 for i in range(0,-dif)])
        for i in range(0, self.__len__()):
            result_list.__setitem__(i, result_list.__getitem__(i) - self.__getitem__(i))
        return result_list
    
    def __ge__(self, x: list) -> bool:
        if not isinstance(x, list):
            raise TypeError("can only compare one list (not " + str(type(x)) + ") with another list")
        return sum(self) >= sum(x)

    def __le__(self, x: list) -> bool:
        if not isinstance(x, list):
            raise TypeError("can only compare one list (not " + str(type(x)) + ") with another list")
        return sum(self) <= sum(x)    

    def __lt__(self, x: list) -> bool:
        if not isinstance(x, list):
            raise TypeError("can only compare one list (not " + str(type(x)) + ") with another list")
        return sum(self) < sum(x) 

    def __gt__(self, x: list) -> bool:
        if not isinstance(x, list):
            raise TypeError("can only compare one list (not " + str(type(x)) + ") with another list")
        return sum(self) > sum(x) 