class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    def get_perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            picture = str()
            for linhas in range(self.height):
                picture += f"{'*'*self.width}\n"
        else:
            picture = "Too big for picture."
        return picture

    def get_amount_inside(self, forma):
        return int(self.get_area() / forma.get_area())

class Square(Rectangle):

    def __init__(self, width):
        self.width = self.height = width

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, sides):
        self.width = self.height = sides


if __name__ == '__main__':
    rect = Rectangle(5, 10)
    cubo = Rectangle(2, 3)
    print(cubo.get_amount_inside(rect))