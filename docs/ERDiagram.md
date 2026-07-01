# Entity Relationship Diagram

The following diagram illustrates the main entities and relationships used by the current Django schema.

```mermaid
erDiagram
    USER ||--o{ PROFILE : has
    USER ||--o{ SESSION : creates
    USER ||--o{ FAVORITE : creates

    CATEGORY ||--o{ VIDEO : contains
    CATEGORY ||--o{ SESSION : organizes

    VIDEO ||--o{ VIDEO_BENEFIT : includes
    VIDEO ||--o{ VIDEO_STEP : includes
    VIDEO ||--o{ FAVORITE : appears_in
    VIDEO ||--o{ SESSION_VIDEO : appears_in

    SESSION ||--o{ SESSION_VIDEO : contains
```

## Entity Notes

- USER refers to Django's built-in authentication user model.
- PROFILE stores additional user fitness and personal information.
- CATEGORY organizes content into reusable topic buckets.
- VIDEO is the main content entity for yoga or fitness lessons.
- FAVORITE links users to videos they have saved.
- SESSION tracks a user's workout progression across selected videos.
- SESSION_VIDEO represents progress for each video inside a session.
