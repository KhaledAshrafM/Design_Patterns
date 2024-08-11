# Dependency Inversion Principle (DIP):
# High-level modules should not depend on low-level modules. Both should depend on abstractions.
# Abstractions should not depend on details. Details should depend on abstractions.

from abc import ABC, abstractmethod
from enum import Enum

class Relationship(Enum):
    """An enumeration that defines the types of relationships between people."""
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    """Represents a person with a name."""

    def __init__(self, name):
        """Initializes a new person with the specified name.
        
        Args:
            name (str): The name of the person.
        """
        self.name = name 

class RelationshipBrowser(ABC):
    """An abstract base class (interface) that defines the operations for browsing relationships."""
    
    @abstractmethod
    def find_all_children_of(self, name):
        """Finds and returns all children of a person with the given name.
        
        Args:
            name (str): The name of the person whose children are to be found.
        
        Returns:
            generator: A generator yielding the names of all children.
        """
        pass

class Relationships(RelationshipBrowser): 
    """A low-level module that stores and manages relationships between people.
    This class implements the `RelationshipBrowser` interface.
    """

    def __init__(self):
        """Initializes an empty list of relationships."""
        self.relations = []
        
    def add_parent_and_child(self, parent, child):
        """Adds a parent-child relationship to the list.
        
        Args:
            parent (Person): The parent in the relationship.
            child (Person): The child in the relationship.
        """
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))
    
    def find_all_children_of(self, name):
        """Finds and returns all children of a person with the given name.
        
        Args:
            name (str): The name of the person whose children are to be found.
        
        Returns:
            generator: A generator yielding the names of all children.
        """
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research: 
    """A high-level module that depends on the abstraction `RelationshipBrowser` 
    rather than the concrete `Relationships` class.
    """

    # Previous constructor that violates DIP:
    # def __init__(self, relationships: Relationships):
    #     """Initializes the Research object and prints the children of 'John'.
    #     This constructor is tightly coupled to the `Relationships` class, which violates the DIP.
    #     
    #     Args:
    #         relationships (Relationships): A concrete instance of the `Relationships` class.
    #     """
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')
    
    def __init__(self, browser: RelationshipBrowser, person: Person):
        """Initializes the Research object and prints the children of the given person.
        
        This constructor adheres to the Dependency Inversion Principle by depending on the `RelationshipBrowser` 
        interface rather than a concrete implementation.

        Args:
            browser (RelationshipBrowser): An object that implements the `RelationshipBrowser` interface.
            person (Person): The person whose children are to be researched.
        """
        for child in browser.find_all_children_of(person.name):
            print(f'{person.name} has a child called {child}')

# Usage Example:

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships, parent)
