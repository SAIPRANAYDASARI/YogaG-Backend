# Branch Strategy

A simple and scalable branching model is recommended for this project.

## Recommended Branches

- main: production-ready code
- develop: integration branch for ongoing development
- feature/*: new features or enhancements
- bugfix/*: fixes for existing defects
- hotfix/*: urgent production fixes

## Workflow

1. Create a feature branch from develop.
2. Work on the change in isolation.
3. Merge back into develop through a pull request.
4. Promote tested changes from develop to main.

## Branch Naming Conventions

- `feature/video-api`
- `feature/session-progress`
- `bugfix/profile-validation`
- `hotfix/auth-token-issue`

## Pull Request Guidelines

Each pull request should include:

- A concise title
- A summary of the change
- Testing steps or validation notes
- Screenshots when UI is involved

## Merge Policy

- No direct pushes to main.
- Require review before merging.
- Keep branches short-lived and focused.
