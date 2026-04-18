# Sequence Diagrams for API Calls

This document contains four sequence diagrams for the main API calls in the HBnB application. Each diagram shows how the Presentation Layer, Business Logic Layer, and Persistence Layer interact to process a request.

---

## 1. User Registration

### Description
This sequence diagram shows how a new user account is created. The API receives the registration request, sends it to the facade, the business logic validates and creates the user, and the persistence layer stores it in the database.

```mermaid
sequenceDiagram
    actor Client
    participant API as Presentation Layer / API
    participant Facade as HBnBFacade
    participant UserModel as Business Logic / User
    participant UserRepo as Persistence / UserRepository
    participant DB as Database

    Client->>API: POST /users (user data)
    API->>Facade: register_user(user data)
    Facade->>UserModel: create_user(user data)
    UserModel->>UserModel: validate fields
    UserModel->>UserModel: hash password
    UserModel-->>Facade: new User object
    Facade->>UserRepo: save(user)
    UserRepo->>DB: INSERT user
    DB-->>UserRepo: user saved
    UserRepo-->>Facade: saved user
    Facade-->>API: success response
    API-->>Client: 201 Created
