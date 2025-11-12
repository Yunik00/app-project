### Android operating system architecture
The operating system is made up of four fundamental layers:
1. Linux Kernel
   Relies on the Linux kernel for underlying functionalities such as threading and low-level memory management
2. Android Runtime
   Includes the virtual machine and the fundamental libraries to run the applications
3. Application Framework
   These APIs form the building blocks you need to create Android apps
4. Applications
   The system apps function both as apps for users and to provide key capabilities that developers can access from their own app

![[android-stack_2x.png]]

### Android Architecture Patterns
##### What are Architecture Patterns?
It is a general and reusable solution to a common problem.
Decouples the different layers and helps to do isolated testing of each component.
##### Most common in Android
- MVP (Model - View - Presenter)
  It organizes the structure of an application into three distinct layers: model, view, and presenter. This pattern is particularly appreciated for its benefits in the separation of responsibilities
  - **View**: The view layer is exclusively responsible for rendering objects. It is important that the view does not perform any other function beyond showing, rendering and hiding elements
  - **Presenter**: The presenter acts as an intermediary between the view and the model. Its main function is to manage how data is presented in view
  - **Model**: The model, also called an interactor, is responsible for all communication with the database and HTTP connections 
  ![[MVP-diagram.png]]

- MVVM (Model - View - ViewModel)
  MVVM is composed of three main layers:
  * **View**: In charge of the visual representation, that is, what the user sees and interacts with.
  * **ViewModel**: This layer acts as an intermediary between the view and the model; manages presentation logic and manages data flow.
  * **Model**: Contains the data and business logic of the application.
  ![[MVVM - diagram.png]]

##### How is MVVM different from MVP?
The main difference lies in the communication between the View and the knowledge of the presentation logic:
- MVP (Model-View-Presenter): Use contracts for communication, making the View and Presenter more coupled.
- MVVM (Model-View-ViewModel): Communication is done through observers and subscriptions. The View automatically updates when there are changes to the ViewModel, eliminating the need for contracts and reducing the number of mediator classes.
### Design Pattern
##### Creational patterns
Delegates the responsibility of creating and instancing the clases we'll need. It's main purpose is encapsulate the classes' knowledge and hide how they are created.
- [[Singleton]]
- [[Builder]]
- [[Factory]]
##### Estructural Patterns
Focuses on how classes and objects are composed to form larger structures.
- Adapter
- Proxy
- Facade
##### Behavior patterns
It tells us what the communication between objects is like and how we can decouple and delegate responsibilities.
- Observer
- Command



