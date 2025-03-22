# CSCI3100_Software_Engineering
Assignment 2 Chan Eugene 1155193465

1.	It is better to use pure OOP. Every class is already under a hiearchy and the code can be better maintained using OOP.
2.	2 errors:
    •	Neutrophils should implement the public method is_enemy(…) as Neutrophils implements the class WhiteBloodCell
    •	There should be a weak association from B-cell to Antibody 
3.	4 Pillars:
    •	Encapsulation: Each class encapsulates its attributes and methods, such as is_enemy and kill in WhiteBloodCell
    •	Inheritance: Classes like Neutrophils and Lymphocytes inherit from WhiteBloodCell, demonstrating a hierarchical structure
    •	Polymorphism: Methods like is_enemy and kill are overridden in subclasses, allowing different behaviors based on the specific type of white blood cell
    •	Abstraction: Abstract classes like Lymphocytes define common behaviors (e.g. is_enemy) without providing implementation details
4.	Strong association:
    •	Dependency: Dependent; parts cannot exist without the whole
    •	Object Lifetime: Parent deletion destroys child objects
    Weak association:
    •	Dependency: Independent; parts can exist without the whole
    •	Object Lifetime: Parent deletion does not affect child objects
5.	Yes, Advantages:
    •	Reduces memory usage since storing a float takes much less space than storing an entire object
    •	Simplifies comparison when matching enemies based on antigen characteristics
    Disadvantages: 
    •	Loses direct access to other attributes of Enemy
    •	May introduce rounding errors
6.	Yes.
7.	Yes, HelperTCell should override the destructor if it manages resources different from those managed by TCell.
8.	white_blood_cells.py
9.	white_blood_cells_has-a.txt
 
