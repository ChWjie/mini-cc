"""A simple greeting module."""


def greet(name: str) -> str:
    """Return a greeting string for the given name.

    Args:
        name: The name of the person to greet.

    Returns:
        A personalized greeting string.
    """
    return f"Hello, {name}!"


def main() -> None:
    """Print a greeting to the console."""
    message: str = greet("World")
    print(message)


if __name__ == "__main__":
    main()
