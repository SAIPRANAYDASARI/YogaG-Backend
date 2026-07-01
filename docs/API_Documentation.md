# API Documentation

The YogiG backend is built with Django and Django REST Framework. At the moment, the project exposes the Django admin interface and is in the early stages of API development.

## Current API Status

### Implemented Routes

- Admin interface: `/admin/`

### Configuration Notes

- Django REST Framework is installed and enabled.
- JWT authentication is configured via `rest_framework_simplejwt`.
- CORS headers are enabled for development-friendly cross-origin access.

## Recommended API Surface

The backend is structured to support the following API modules:

| Module | Purpose | Suggested Endpoint Group |
| --- | --- | --- |
| Authentication | Register, login, refresh tokens | `/api/auth/` |
| Profiles | Manage user profile data | `/api/profiles/` |
| Categories | Retrieve and manage categories | `/api/categories/` |
| Videos | List, detail, and filter videos | `/api/videos/` |
| Favorites | Save and remove favorite videos | `/api/favorites/` |
| Sessions | Create and update workout sessions | `/api/sessions/` |

## Authentication

The project is configured to use JWT-based authentication in the future. Recommended endpoints include:

- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `POST /api/auth/token/refresh/`

## Response Conventions

A consistent API contract should follow these conventions:

- Use JSON for all responses.
- Return meaningful HTTP status codes.
- Use resource-specific success and error payloads.
- Include pagination for list endpoints where appropriate.

## Future Enhancements

Planned API improvements include:

- Full CRUD endpoints for categories and videos
- Session-based progress tracking APIs
- Search and filtering for videos by difficulty or focus area
- User-specific favorite and session operations
