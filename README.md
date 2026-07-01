# YogiG Backend

YogiG is a Django-based backend service for managing yoga and fitness video content, personalized workout sessions, user profiles, and favorites. The project is designed to support a modern wellness application with structured video recommendations and session tracking.

## Overview

This repository contains the backend foundation for:

- User authentication and profile management
- Category-based video organization
- Personalized fitness sessions
- Favorites and progress tracking
- Admin-friendly content management

## Technology Stack

- Python 3.x
- Django 6.0
- Django REST Framework
- SQLite for local development
- Pillow for image handling
- Django CORS Headers

## Project Structure

- accounts: authentication-related application scaffolding
- profiles: user profile and fitness metadata
- categories: workout categories and taxonomy
- videos: yoga/fitness video content and related benefits/steps
- favorites: user-video bookmark relationships
- sessions: structured workout sessions and per-video progress
- config: Django project settings and URL routing

## Quick Start

1. Navigate to the project directory:
   ```bash
   cd yogig_backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Documentation

The documentation set for this project is available in the docs folder:

- [docs/DatabaseSchema.md](docs/DatabaseSchema.md)
- [docs/ERDiagram.md](docs/ERDiagram.md)
- [docs/API_Documentation.md](docs/API_Documentation.md)
- [docs/ProjectWorkflow.md](docs/ProjectWorkflow.md)
- [docs/BranchStrategy.md](docs/BranchStrategy.md)
- [docs/DevelopmentRoadmap.md](docs/DevelopmentRoadmap.md)

## Current Status

The project currently includes:

- Django app structure for core business domains
- Database models for categories, videos, profiles, favorites, and sessions
- SQLite-backed local development configuration
- Django admin integration

Future work will focus on exposing the data through REST APIs, adding authentication flows, and connecting the backend to frontend clients.
