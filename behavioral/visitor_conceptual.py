from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import logging

logging.basicConfig(level="INFO")


class Component(ABC):
    """
    The Component interface declares an `accept` method that should take the
    base visitor interface as an argument.
    """

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class ConcreteComponentA(Component):
    """
    Each Concrete Component must implement the `accept` method in such a way
    that it calls the visitor's method corresponding to the component's class.
    """

    def accept(self, visitor: Visitor) -> None:
        """
        Note that we're calling `visitConcreteComponentA`, which matches the
        current class name. This way we let the visitor know the class of the
        component it works with.
        """

        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self) -> str:
        """
        Concrete Components may have special methods that don't exist in their
        base class or interface. The Visitor is still able to use these methods
        since it's aware of the component's concrete class.
        """

        return "A"


class ConcreteComponentB(Component):
    """
    Same here: visitConcreteComponentB => ConcreteComponentB
    """

    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self) -> str:
        return "B"


class Visitor(ABC):
    """
    The Visitor Interface declares a set of visiting methods that correspond to
    component classes. The signature of a visiting method allows the visitor to
    identify the exact class of the component that it's dealing with.
    """

    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass


"""
Concrete Visitors implement several versions of the same algorithm, which can
work with all concrete component classes.

You can experience the biggest benefit of the Visitor pattern when using it with
a complex object structure, such as a Composite tree. In this case, it might be
helpful to store some intermediate state of the algorithm while executing
visitor's methods over various objects of the structure.
"""


class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        logging.info(
            "%s + ConcreteVisitor1", element.exclusive_method_of_concrete_component_a()
        )

    def visit_concrete_component_b(self, element) -> None:
        logging.info(
            "%s + ConcreteVisitor1", element.special_method_of_concrete_component_b()
        )


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        logging.info(
            "%s + ConcreteVisitor2", element.exclusive_method_of_concrete_component_a()
        )

    def visit_concrete_component_b(self, element) -> None:
        logging.info(
            "%s + ConcreteVisitor2", element.special_method_of_concrete_component_b()
        )


def client_code(components: List[Component], visitor: Visitor) -> None:
    """
    The client code can run visitor operations over any set of elements without
    figuring out their concrete classes. The accept operation directs a call to
    the appropriate operation in the visitor object.
    """

    # ...
    for component in components:
        component.accept(visitor)
    # ...


if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    logging.info(
        "The client code works with all visitors via the base Visitor interface:"
    )
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    logging.info(
        "It allows the same client code to work with different types of visitors:"
    )
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)
