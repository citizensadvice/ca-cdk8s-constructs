# Show the list of available commands
@help:
    just --list

# Run typechecking
[group("code quality")]
typecheck:
    uv run ty check .

# Run pytest tests
[group("code quality")]
pytest:
    uv run pytest tests

# Run ruff linter
[group("code quality")]
lint:
    uv run ruff check .
    uv run ruff format --check .

# Run all tests: typechecking, pytest, and linting
[group("code quality")]
all-tests: typecheck pytest lint

# Autoformat code with ruff
[group("code quality")]
format:
    uv run ruff format .
    uv run ruff check --fix .
    just --fmt --unstable

# Bump version, push and create draft release
[confirm("Are you sure you want to draft a release? [y/N]")]
[group("release")]
draft-release bump='patch': (_bump_version bump) _push_version _create_draft_release

_bump_version bump:
    git checkout main
    git pull origin main
    git reset
    uv version --bump {{ bump }}
    git add pyproject.toml uv.lock

[confirm("Are you sure you want to push the version change? [y/N]")]
_push_version:
    git commit -m "Bumped version to $(uv version --short)"
    git push origin main

_create_draft_release:
    gh release create $(uv version --short) --draft --generate-notes
    echo "> Follow the link to review and publish the release"
