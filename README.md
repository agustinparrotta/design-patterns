# Design Patterns

Design Patterns is the most essential part of Software Engineering, as they provide the general repeatable solution to a commonly occurring problem in software design.

Types:

1. Creational
2. Structural
3. Behavioral

## 1. Creational

Provides essential information regarding the **Class** instantiation or the **Object** instantiation. Class Creational Pattern and the Object Creational pattern is the major categorization of the Creational Design Patterns. **Class-creation** patterns use **inheritance** effectively in the instantiation process, and **object-creation** patterns use **delegation** effectively to get the job done.

- Factory
- Abstract factory
- Builder
- Prototype
- Singleton

### 1.1. Factory

Allows an interface or a class to create an object, but lets subclasses decide which class or object to instantiate.

- Best way to create an object.
- Objects are created without exposing the logic to the client (same common interface).

Notes:

- Less complicated, more customizable through subclasses
- Uses inheritance, but does not require an init step
- Is a specialization of the Template pattern.
- 2 main entities: Creator and Product. Creator knows how to create the product and execute it. Product contains operation itself.

Importance: 5

### 1.2. Abstract factory

Allows you to produce the families of related objects without specifying their concrete classes.

- Easiest way to produce a similar type of many objects.
- It provides a way to encapsulate a group of individual factories. Basically, here we try to abstract the creation of the objects depending on the logic, business, platform choice, etc.

Notes:

- Products from a factory are compatible with each other
- 2 main entities: Creator and Product

Importance: 4

### 1.3. Builder

Aims to separate the construction of a complex object from its representation so that the same construction process can create different representations.

- Allows you to construct complex objects step by step. Using the same construction code, we can produce different types and representations of the object easily.
- Provides flexibility to the solutions to various object creation problems.

Notes:

- Use Builder only when the products are quite complex and require extensive configuration

Importance: 4

### 1.4. Prototype

Aims to reduce the number of classes used for an application. It allows you to copy existing objects independent of the concrete implementation of their classes. Generally, here the object is created by copying a prototypical instance during run-time.

- Highly recommended to use it when the object creation is an expensive task in terms of time and usage of resources and already there exists a similar object.
- Provides a way to copy the original object and then modify it according to our needs.

Notes:

- Basically is the implementation of `copy.copy` and `copy.deepcopy` for custom objects

Importance: 3

### 1.5. Singleton

It is a way to provide one and only one object of a particular type. It involves only one class to create methods and specify the objects.

- Example: Database connectivity. When each object creates a unique Database Connection to the Database, it will highly affect the cost and expenses of the project. So, it is always better to make a single connection rather than making extra irrelevant connections.

Notes:

- Potential issues related to thread safety.
- It brakes the Single Responsibility Principle.

Importance: 3

## 2. Structural

Are about organizing different classes and objects to form larger structures and provide new functionality while keeping these structures flexible and efficient. Mostly they use Inheritance to compose all the interfaces. It also identifies the relationships which led to the simplification of the structure.

- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Proxy
- FlyWeight

### 2.1. Adapter

Help us in making the incompatible objects adaptable to each other. This method provides a different interface for a class. Using this idea, we can integrate the classes that couldn’t be integrated due to interface incompatibility.

Notes:

- It’s very often used in systems based on some legacy code. In such cases, Adapters make legacy code work with modern classes.

Importance: 4

### 2.2. Bridge

Allows us to separate the Implementation Specific Abstractions and Implementation Independent Abstractions from each other and can be developed considering as the single entities. Bridge Method is always considered as one of the best methods to organize the class hierarchy.

Notes:

- Bridge can be recognized by a clear distinction between some controlling entity and several different platforms that it relies on.
- Useful for decoupling an abstraction from its implementation

Importance: 2

### 2.3. Composite

Describes a group of objects that is treated the same way as a single instance of the same type of the objects. The purpose is to compose objects into tree type structures to represent the whole-partial hierarchies.

Notes:

- Using the Composite pattern makes sense only when the core model of your app can be represented as a tree.

Importance: 3

### 2.4. Decorator

Allows you to dynamically attach new behaviors to objects without changing their implementation by placing these objects inside the wrapper objects that contains the behaviors. It is not equivalent to the Inheritance because the new feature is added only to that particular object, not to the entire subclass.

Notes:

- Without creating a new subclass, it’s possible to enhance the functionality of an object by extending its behavior.
- Use python implementation.

Importance: 3

### 2.5. Facade

Provides a simpler unified interface to a more complex system. The word Facade means the face of a building or particularly an outer lying interface of a complex system, consists of several sub-systems. It provides an easier way to access methods of the underlying systems by providing a single entry point.

Notes:

- Having a facade is handy when you need to integrate your app with a sophisticated library that has dozens of features, but you just need a tiny bit of its functionality.
- It is basically a wrapper for a subsystem.

Importance: 4

### 2.6. FlyWeight

Focus on minimizing the number of objects that are required by the program at the run-time. Basically, it creates a Flyweight object which is shared by multiple contexts. It is created in such a fashion that you can not distinguish between an object and a Flyweight Object. One important feature of flyweight objects is that they are immutable.

Notes:

- To implement the Flyweight method in Python, we use Dictionary that stores reference to the object which have already been created, every object is associated with a key.
- Prototype design pattern sounds similar, but it was about the initial creation of any objects. The purpose is different. The Flyweight pattern is used to reduce memory usage by sharing common data among similar objects, while the Prototype pattern is used to create new objects by copying existing ones.

Importance: 1

### 2.7. Proxy

Allows you to provide the replacement for an another object. Here, we use different classes to represent the functionalities of another class. The most important part is that here we create an object having original object functionality to provide to the outer world.

Proxies are also called surrogates, handles, and wrappers. They are closely related in structure, but not purpose, to Adapters, Decorators and Facade. The purpose is "Controls and manage access to the object they are protecting".

Notes:

- It controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.
- It is useful when you want to add some additional behaviors to an object of some existing class without changing the client code.

Importance: 2

## 3. Behavioral

Are about identifying the common communication patterns between objects and realize these patterns. These patterns are concerned with algorithms and the assignment of responsibilities between objects.

- Chain of responsibility
- Command
- Iterator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template
- Visitor

### 3.1. Chainf of Responsibility

Is the object-oriented version of if … elif … elif … else and make us capable to rearrange the condition-action blocks dynamically at the run-time. It allows us to pass the requests along the chain of handlers. The processing is simple, whenever any handler received the request it has two choices either to process it or pass it to the next handler in the chain.
This pattern aims to decouple the senders of a request from its receivers by allowing the request to move through chained receivers until it is handled.

Notes:

- It’s mostly relevant when your code operates with chains of objects, such as filters, event chains, etc.

Importance: 3

### 3.2. Command

Encapsulates a request as an object, thereby allowing for the parameterization of clients with different requests and the queuing or logging of requests. Parameterizing other objects with different requests in our analogy means that the button used to turn on the lights can later be used to turn on stereo or maybe open the garage door. It helps in promoting the “invocation of a method on an object” to full object status. Basically, it encapsulates all the information needed to perform an action or trigger an event.

Notes:

- This pattern is recognizable by behavioral methods in an abstract/interface type (sender) which invokes a method in an implementation of a different abstract/interface type (receiver) which has been encapsulated by the command implementation during its creation.
- It is easier to add new commands, queue or log commands for later execution, or undo/redo commands as needed.
- The strategy pattern sounds similar. However, the intent is different. The strategy pattern focuses on providing alternative algorithms or strategies for a particular task, while the command pattern focuses on encapsulating a request as an object to enable undo/redo operations or to implement logging and transactional systems.

Importance: 5

### 3.3. Iterator

Allows us to traverse the elements of the collections without taking the exposure of in-depth details of the elements. It provides a way to access the elements of complex data structure sequentially without repeating them. It is used to access the elements of an aggregate object sequentially without exposing its underlying implementation.

Notes:

- Iterator is easy to recognize by the navigation methods (such as next, previous and others).
- Applying the pattern can be an overkill if your app only works with simple collections.

Importance: 4

### 3.4. Mediator

Allows us to reduce the unordered dependencies between the objects. In a mediator environment, objects take the help of mediator objects to communicate with each other. It reduces coupling by reducing the dependencies between communicating objects. The mediator works as a router between objects and it can have it’s own logic to provide a way of communication.

Notes:

- Most popular usage is facilitating communications between GUI components of an app. The synonym of the Mediator is the Controller part of MVC pattern. Some examples: When communication is important. For example, in a distributed system, a mediator can be used to coordinate the communication between different nodes or services. Other potential use cases for the mediator pattern include chat applications, event-driven systems, and workflow management systems.

Importance: 1

### 3.5. Memento

Provides the ability to restore an object to its previous state. Without revealing the details of concrete implementations, it allows you to save and restore the previous version of the object. It tries not to disturb the encapsulation of the code and allows you to capture and externalize an object’s internal state.

Notes:

- Useful for games, database systems, transaction management.
- It could consume too much memory.

Importance: 2

### 3.6. Observer

Allows you to define or create a subscription mechanism to send the notification to the multiple objects about any new event that happens to the object that they are observing. The subject is basically observed by multiple objects. The subject needs to be monitored and whenever there is a change in the subject, the observers are being notified about the change. This pattern defines one to Many dependencies between objects so that one object changes state, all of its dependents are notified and updated automatically.

Notes:

- It provides a way to react to events happening in other objects without coupling to their classes.
- The pattern can be recognized by subscription methods, that store objects in a list and by calls to the update method issued to objects in that list.

Importance: 5

### 3.7. State

Allows an object to change its behavior when there occurs a change in its internal state. It helps in implementing the state as a derived class of the state pattern interface. If we have to change the behavior of an object based on its state, we can have a state variable in the Object and use if-else condition block to perform different actions based on the state. It may be termed as the object-oriented state machine. It implements the state transitions by invoking methods from the pattern’s superclass.

### 3.8. Strategy

Allows you to define the complete family of algorithms, encapsulates each one and putting each of them into separate classes and also allows to interchange there objects. It is implemented in Python by dynamically replacing the content of a method defined inside a class with the contents of functions defined outside of the class. It enables selecting the algorithm at run-time. This method is also called as Policy Method.

### 3.9. Template

Defines the skeleton of the operation and leaves the details to be implemented by the child class. Its subclasses can override the method implementations as per need but the invocation is to be in the same way as defined by an abstract class. Such methods are highly used in framework development as they allow us to reuse the single piece of code at different places by making certain changes. This leads to avoiding code duplication too.

### 3.10. Visitor

Allows us to separate the algorithm from an object structure on which it operates. It helps us to add new features to an existing class hierarchy dynamically without changing it. All the behavioral patterns proved as the best methods to handle the communication between the objects. Similarly, it is used when we have to perform an operation on a group of similar kinds of objects.

# References

See those posts for more information:

- [GeeksForGeeks](https://www.geeksforgeeks.org/python-design-patterns/)
- [RefactoringGuru](https://refactoring.guru/design-patterns)
- [Medium](https://medium.com/towardsdev/a-catalog-for-design-patterns-in-python-a1b69493c677)
- [Clean Code in Python, by Mariano Anaya](https://www.packtpub.com/product/clean-code-in-python-second-edition/9781800560215)
