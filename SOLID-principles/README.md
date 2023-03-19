## Design patterns and SOLID principle

- `SOLID` is a set of principles for writing maintainable and scalable code. Here is a brief explanation of each principle along with an example in Python:

## **Single Responsibility Principle (SRP)**

- A class should only have one reason to change. For example, a class that handles database connections should not also be responsible for rendering HTML.

```python
# Bad example
class DatabaseConnection:
    def connect(self):
        # code to connect to the database

    def render_html(self, data):
        # code to generate HTML

# Good example
class DatabaseConnection:
    def connect(self):
        # code to connect to the database

class HTMLRenderer:
    def render(self, data):
        # code to generate HTML

```

## **Open/Closed Principle (OCP)**

- A class should be open for extension but closed for modification. This means that you should be able to add new functionality to a class without modifying its existing code.

```python
# Bad example
class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def draw(self):
        if self.shape_type == 'circle':
            # code to draw a circle
        elif self.shape_type == 'square':
            # code to draw a square

# Good example
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        # code to draw a circle

class Square(Shape):
    def draw(self):
        # code to draw a square

```

## **Liskov Substitution Principle (LSP)**

- Subclasses should be able to replace their parent class without affecting the correctness of the program.

```python
# Bad example
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

# Good example
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

```

## **Interface Segregation Principle (ISP)**

- A client should not be forced to implement interfaces they do not use.

```python
# Bad example
class Printer:
    def print(self, document):
        pass

class Scanner:
    def scan(self):
        pass

class MultifunctionDevice(Printer, Scanner):
    def print(self, document):
        # code to print a document

    def scan(self):
        # code to scan a document

# Good example
class Printer:
    def print(self, document):
        pass

class Scanner:
    def scan(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print(self, document):
        # code to print a document

    def scan(self):
        # code to scan a document

class LegacyPrinter(Printer):
    def print(self, document):
        # code to print a document

class Photocopier(Printer, Scanner):
    def print(self, document):
        # code to print a document

    def scan(self):
        # code to scan a document

```

## **Dependency Inversion Principle (DIP)**

- High-level modules should not depend on low-level modules. Both should depend on abstractions.

```python
# Bad example
class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        # code to connect to the database
        self.connection = ...

    def disconnect(self):
        # code to disconnect from the database
        self.connection = None

class User:
    def __init__(self):
        self.database = Database()

    def save(self):
        self.database.connect()
        # code to save the user data
        self.database.disconnect()

# Good example
class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        # code to connect to the database
        self.connection = ...

    def disconnect(self):
        # code to disconnect from the database
        self.connection = None

class User:
    def __init__(self, database):
        self.database = database

    def save(self):
        self.database.connect()
        # code to save the user data
        self.database.disconnect()

database = Database()
user = User(database)
```
