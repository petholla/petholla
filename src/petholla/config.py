import tomllib
import pathlib

def get_config(application: str) -> dict | None:
    """Read config for application."""
    home = pathlib.Path.home()
    filename = f"{home}/.petholla_config.toml"
    with open(filename, "rb") as file:
        data = tomllib.load(file)
        return data.get(application)
