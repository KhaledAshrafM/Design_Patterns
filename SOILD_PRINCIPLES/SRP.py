# Single Responsibility Principle (SRP): 
# A class should have only one reason to change, meaning that a class should have only one job or responsibility.

# Example:
class Journal:
    """Represents a personal journal where you can add and remove entries."""

    def __init__(self):
        """Initializes a new journal with an empty list of entries and a counter."""
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        """Adds a new entry to the journal.
        
        Args:
            text (str): The text of the entry to be added.
        """
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        """Removes an entry from the journal.
        
        Args:
            pos (int): The position of the entry to be removed.
        """
        del self.entries[pos]
        self.count -= 1

    def __str__(self):
        """Returns the string representation of the journal."""
        return "\n".join(self.entries)
    
    # Methods related to persistence (saving/loading) have been commented out 
    # because they violate the Single Responsibility Principle. They should be 
    # handled by a separate class.

    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:
    """Handles the saving and loading of journal entries to and from a file."""

    @staticmethod
    def save_to_file(journal, filename):
        """Saves the journal entries to a file.
        
        Args:
            journal (Journal): The journal object to be saved.
            filename (str): The name of the file where the journal will be saved.
        """
        with open(filename, "w") as file:
            file.write(str(journal))

# Usage Example:
j = Journal()
j.add_entry("I coded one program")
j.add_entry("I ate ice cream")
print(f"Journal entries:\n{j}")

file = "journal.txt"
PersistenceManager.save_to_file(j, file)
with open(file) as f:
    print(f.read())
