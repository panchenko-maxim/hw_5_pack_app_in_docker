from app.services import get_name_address


def app() -> None:
    name, address = get_name_address()
    print(f"Hello, {name}!\nThis is your address:\n{'-' * 10}\n{address}")  # noqa: T201
