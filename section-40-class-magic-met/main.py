class Image():
    def __init__(self, resolution, title, extension) -> None:
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_size):
        self.resolution = new_size

    def __str__(self) -> str:
        return f"{self.title} {self.resolution} {self.extension}"

    def __add__(self, other):
        return f"{self.title} {other.title}"

    def __eq__(self, other):
        return self.title == other.title


cat_img = Image("800x600", "kitty", "jpg")
dog_img = Image("800x600", "dogy", "jpg")

cat_img.resize("1027x768")

print(cat_img)
print(dog_img)
print(cat_img + dog_img)
print(cat_img == dog_img)
