# HBnB Technical Documentation

## Introduction

This document provides a technical blueprint for the HBnB application. Its purpose is to guide the implementation of the project by describing the system architecture, the core business entities, and the interaction flow for major API calls.

The HBnB application follows a **three-layer architecture**:

- **Presentation Layer**: Handles API requests and user interaction
- **Business Logic Layer**: Contains the core models and business rules
- **Persistence Layer**: Manages data storage and retrieval

A **Facade pattern** is used to simplify communication between layers. Instead of allowing the Presentation Layer to directly interact with all business objects and repositories, a central facade coordinates operations and provides a clean interface.

This document includes:

- A high-level architecture diagram
- A detailed class diagram for the Business Logic Layer
- Sequence diagrams for key API calls
- Explanatory notes for each section

---

# 1. High-Level Architecture

## Purpose

This diagram presents the overall organization of the HBnB application. It shows the three major layers of the system and how they communicate through the facade.

## High-Level Package Diagram

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
