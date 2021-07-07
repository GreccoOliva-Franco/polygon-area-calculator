class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def set_width(self, width):
		self.width = width
	
	def set_height(self, height):
		self.height = height

	def get_area(self):
		return self.width * self.height

	def get_perimeter(self):
		return 2 * self.width + 2 * self.height

	def get_diagonal(self):
		return (self.width ** 2 + self.height ** 2) ** .5

	def get_picture(self):
		if self.height > 50 or self.width > 50:
			return "Too big for picture."

		stringList = []

		for line in range(self.height):
			stringList.append("*" * self.width)

		return "\n".join(stringList) + "\n"


	def get_amount_inside(self, shape):
		horizontals = self.width // shape.width
		verticals = self.height // shape.height

		return horizontals * verticals

	def __str__(self):
		return f"Rectangle(width={self.width}, height={self.height})"


class Square (Rectangle):
	def __init__(self, side):
		self.side = side
		super().__init__(side, side)

	def set_side(self, side):
		self.side = side
		self.width = side
		self.height = side

	def set_width(self, width):
		self.side = width
		self.width = width
		self.height = width

	def set_height(self, height):
		self.side = height
		self.width = height
		self.height = height
		
	def __str__(self):
		return f"Square(side={self.side})"