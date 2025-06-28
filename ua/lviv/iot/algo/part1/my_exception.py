class ZeroItemsError(Exception):
    message = "Nothing to subtract in "

    def __init__(self, class_name=""):
        self.class_name = class_name

    def __str__(self):
        return f"ZeroItemsError({self.message} {self.class_name})"
