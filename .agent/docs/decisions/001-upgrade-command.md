---
status: accepted
date: 2026-02-09
deciders: [User, AI Agent]
---

# Upgrade Command and Version Check

## Context and Problem Statement

The Ulkan CLI tool is evolving rapidly. Users need a simple way to check if they are running the latest version and update it if necessary. Without an automated way to check and update, users might be running outdated versions with bugs or missing features.

## Decision Drivers

*   **Ease of Use**: Users should not have to manually check PyPI or run complex pip commands.
*   **Awareness**: Users should be notified when a new version is available.
*   **Consistency**: The command name should align with industry standards for "moving to a newer version".
*   **Performance**: The version check should be non-blocking and fail silently if offline.

## Considered Options

*   `ulkan update` (npm style)
*   `ulkan upgrade` (pip/apt/brew style)
*   Manual `pip install --upgrade ulkan` only

## Decision Outcome

Chosen option: "**ulkan upgrade**", because it aligns better with the Python ecosystem (pip) and implies a version bump rather than just a metadata refresh.

We also implemented a non-blocking version check that:
1.  Runs on `ulkan init` (displayed in the banner).
2.  Runs on other commands (displayed in a simple header).
3.  Shows a "New release available!" notification with color coding.

### Positive Consequences

*   Users can easily keep their CLI up to date.
*   Increased adoption of new features and bug fixes.
*   Professional and polished CLI experience.

### Negative Consequences

*   Adds a dependency on `packaging` and `httpx` (though `httpx` was already there).
*   Slight overhead for the HTTP request (though we use a short timeout).

## Pros and Cons of the Options

### `ulkan update`

*   Good, because it's familiar to JS developers (npm).
*   Bad, because in package managers like `apt`, `update` only refreshes lists, it doesn't upgrade packages.

### `ulkan upgrade`

*   Good, because it's standard in `pip`, `apt`, `brew` for installing newer versions.
*   Good, because "upgrade" strongly implies "moving up" to a better version.

### Manual pip install

*   Good, because it requires zero code in Ulkan.
*   Bad, because users will forget to check for updates.
