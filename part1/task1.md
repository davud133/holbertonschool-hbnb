# HBnB High-Level Package Diagram

## High-Level Architecture Overview

```mermaid
flowchart TB

    subgraph Presentation_Layer["Presentation Layer"]
        API["API / Endpoints"]
        Services["Services"]
    end

    Facade["HBnBFacade\n(Facade Pattern)"]

    subgraph Business_Logic_Layer["Business Logic Layer"]
        User["User"]
        Place["Place"]
        Review["Review"]
        Amenity["Amenity"]
    end

    subgraph Persistence_Layer["Persistence Layer"]
        UserRepo["UserRepository"]
        PlaceRepo["PlaceRepository"]
        ReviewRepo["ReviewRepository"]
        AmenityRepo["AmenityRepository"]
        DB["Database"]
    end

    API --> Facade
    Services --> Facade

    Facade --> User
    Facade --> Place
    Facade --> Review
    Facade --> Amenity

    User --> UserRepo
    Place --> PlaceRepo
    Review --> ReviewRepo
    Amenity --> AmenityRepo

    UserRepo --> DB
    PlaceRepo --> DB
    ReviewRepo --> DB
    AmenityRepo --> DB
