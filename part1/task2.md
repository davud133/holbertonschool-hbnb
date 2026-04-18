# Detailed Class Diagram for Business Logic Layer

## Business Logic Layer - Class Diagram

```mermaid
classDiagram

    class BaseModel {
        +UUID id
        +datetime created_at
        +datetime updated_at
        +save()
        +update()
        +delete()
    }

    class User {
        +string first_name
        +string last_name
        +string email
        +string password
        +bool is_admin
        +create_place()
        +create_review()
        +update_profile()
    }

    class Place {
        +string title
        +string description
        +float price
        +float latitude
        +float longitude
        +create()
        +update()
        +add_amenity()
        +remove_amenity()
    }

    class Review {
        +string text
        +int rating
        +create()
        +update()
        +delete()
    }

    class Amenity {
        +string name
        +create()
        +update()
        +delete()
    }

    BaseModel <|-- User
    BaseModel <|-- Place
    BaseModel <|-- Review
    BaseModel <|-- Amenity

    User "1" --> "0..*" Place : owns
    User "1" --> "0..*" Review : writes
    Place "1" --> "0..*" Review : receives
    Place "0..*" --> "0..*" Amenity : has
    Review "1" --> "1" Place : about
    Review "1" --> "1" User : written_by
