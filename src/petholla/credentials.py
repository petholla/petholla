import tomllib
import pathlib

def load_credentials(application: str) -> dict | None:
    """Read credentials."""
    home = pathlib.Path.home()
    filename = f"{home}/.credentials.toml"
    with open(filename, "rb") as file:
        data = tomllib.load(file)
        return data.get(application)
