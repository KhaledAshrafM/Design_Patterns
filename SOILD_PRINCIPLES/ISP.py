# Interface Segregation Principle (ISP):
# Clients should not be forced to depend on interfaces they do not use. 
# It's better to have many client-specific interfaces than to have one general-purpose interface.

from abc import ABC, abstractmethod

class Machine(ABC):
    """An interface that defines a general-purpose machine with print, fax, and scan capabilities.
    This interface violates the Interface Segregation Principle by forcing clients to implement methods they may not need.
    """
    
    @abstractmethod
    def print(self, doc):
        """Prints a document.
        
        Args:
            doc (str): The document to print.
        """
        raise NotImplementedError
    
    @abstractmethod
    def fax(self, doc):
        """Faxes a document.
        
        Args:
            doc (str): The document to fax.
        """
        raise NotImplementedError
    
    @abstractmethod
    def scan(self, doc):
        """Scans a document.
        
        Args:
            doc (str): The document to scan.
        """
        raise NotImplementedError
  
class MultiFunctionPrinter(Machine):
    """A concrete implementation of a modern printer that can print, fax, and scan documents.
    This class implements all methods of the Machine interface.
    """

    def print(self, doc):
        """Prints a document."""
        pass 
    
    def fax(self, doc):
        """Faxes a document."""
        pass 
    
    def scan(self, doc):
        """Scans a document."""
        pass 

class OldFashionPrinter(Machine):
    """An old-fashioned printer that can only print documents.
    This class violates the Interface Segregation Principle by having to implement fax and scan methods that it doesn't use.
    """

    def print(self, doc):
        """Prints a document."""
        pass 
    
    def fax(self, doc):
        """This printer cannot fax, so this method does nothing."""
        pass 
    
    def scan(self, doc):
        """This printer cannot scan, so this method does nothing."""
        pass 

# Applying the Interface Segregation Principle:

class Printer(ABC):
    """A specific interface for printers."""

    @abstractmethod
    def print(self, doc):
        """Prints a document."""
        pass 

class Scanner(ABC):
    """A specific interface for scanners."""

    @abstractmethod
    def scan(self, doc):
        """Scans a document."""
        pass 

class MultiFunctionDevice(Printer, Scanner):
    """An interface for a device that can both print and scan."""

    @abstractmethod
    def print(self, doc):
        """Prints a document."""
        pass 
    
    @abstractmethod
    def scan(self, doc):
        """Scans a document."""
        pass

# Concrete implementations:

class MyPrinter(Printer):
    """A concrete implementation of a printer that only prints documents."""

    def print(self, doc):
        """Prints a document."""
        print(doc)

class Photocopier(Printer, Scanner):
    """A concrete implementation of a photocopier that can both print and scan documents."""

    def print(self, doc):
        """Prints a document."""
        pass
    
    def scan(self, doc):
        """Scans a document."""
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    """A concrete implementation of a multifunction machine that can delegate print and scan tasks to separate devices."""

    def __init__(self, printer: Printer, scanner: Scanner):
        """Initializes the MultiFunctionMachine with a specific printer and scanner.
        
        Args:
            printer (Printer): The printer to be used by the machine.
            scanner (Scanner): The scanner to be used by the machine.
        """
        self.printer = printer
        self.scanner = scanner 

    def print(self, doc):
        """Delegates the print task to the provided printer."""
        self.printer.print(doc)
    
    def scan(self, doc):
        """Delegates the scan task to the provided scanner."""
        self.scanner.scan(doc)
