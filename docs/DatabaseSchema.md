# Database Schema

This document summarizes the current database design used by the YogiG Django backend.

## Overview

The project uses SQLite for local development and Django's built-in authentication system. The schema is organized around a content domain of categories, videos, user profiles, favorites, and guided sessions.

## Core Tables

| Table | Purpose | Key Notes |
| --- | --- | --- |
| auth_user | Built-in Django user account table | Used for authentication and ownership |
| categories_category | Defines workout or wellness categories | Each category has a unique name |
| profiles_profile | Stores extended user profile information | Links one-to-one with a user |
| videos_video | Represents an individual yoga or fitness video | Belongs to one category |
| videos_videobenefit | Stores benefits for a video | Related to one video |
| videos_videostep | Stores instructional steps for a video | Related to one video |
| favorites_favorite | Tracks a user's favorite videos | Unique per user-video pair |
| sessions_session | Represents a workout session for a user | Belongs to one category and one user |
| sessions_sessionvideo | Tracks video progress inside a session | Unique per session-video pair |

## Model Relationships

### 1. User and Profile

- Each Django user can have exactly one profile.
- The relationship is implemented using a one-to-one field.
- Profile data includes age, gender, height, weight, and fitness level.

### 2. Category and Video

- Each category can contain many videos.
- Each video belongs to exactly one category.
- This supports content organization by focus area or workout type.

### 3. Video Details

- Each video can have many benefits and many steps.
- These are modeled as child tables to keep the main video model focused on core metadata.

### 4. Favorites

- Users can mark videos as favorites.
- A favorite is a many-to-many style relationship expressed through an explicit join model.
- The composite uniqueness constraint prevents duplicate favorites.

### 5. Sessions and Progress Tracking

- A session belongs to a user and a category.
- A session may contain many videos through the session-video join model.
- Each session video tracks completion state, watched duration, and completion timestamp.

## Important Constraints

- Category names are unique.
- A user cannot favorite the same video twice.
- A session cannot include the same video twice.
- Session status is restricted to In Progress, Completed, or Cancelled.

## Notes

The accounts app currently does not define a custom user model. The backend relies on Django's default user model for authentication and ownership.
