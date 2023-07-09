class ExtendedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")


custom_lst = ExtendedList([1, 2, 3, 4])
print(isinstance(custom_lst, ExtendedList))  # True
print(isinstance(custom_lst, list))  # True
print(isinstance(custom_lst, object))  # True
print(list.__subclasses__())  # [<class '__main__.ExtendedList'>]
print(object.__subclasses__())  # [<class '__main__.ExtendedList'>]
custom_lst.print_list_info()
