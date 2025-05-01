"""
Main module for the application.

This module contains the main functionality of the application.
"""

class ExampleClass:
    """A class that serves as an example.
    
    This class demonstrates how to write proper docstrings
    that Sphinx can parse into documentation.
    
    Attributes:
        name (str): The name of the example.
        value (int): The value of the example.
    """
    
    def __init__(self, name, value=0):
        """Initialize the ExampleClass.
        
        Args:
            name (str): The name of the example.
            value (int, optional): The value of the example. Defaults to 0.
        """
        self.name = name
        self.value = value
    
    def add_value(self, amount):
        """Add to the current value.
        
        Args:
            amount (int): The amount to add.
            
        Returns:
            int: The new value.
            
        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.value += amount
        return self.value


def example_function(param1, param2=None):
    """Example function with types documented in the docstring.
    
    Args:
        param1 (int): The first parameter.
        param2 (str, optional): The second parameter. Defaults to None.
        
    Returns:
        bool: The return value. True for success, False otherwise.
        
    Examples:
        >>> example_function(1, "test")
        True
    """
    return True