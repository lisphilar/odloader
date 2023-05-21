from __future__ import annotations
from pathlib import Path
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib
import tomli_w
from odloader.exceptions import ParseError


class _TOMLParser:
    """Class for parsing TOML files.

    Args:
        dictionary: Python dictionary to save or None (empty dictionary) 
    """

    def __init__(self, dictionary: dict[str, dict[str, str | int]]) -> None:
        self._dict = dictionary or None

    def read_toml(self, filename: str or Path) -> None:
        """Read a TOML file as a dictionary (overwrite).

        Args:
            filename: TOML filename
        """
        with Path(filename).open("rb") as fh:
            try:
                self._dict = tomllib.load(fh)
            except tomllib.TOMLDecodeError:
                raise ParseError(filename=filename, ext="toml")

    def to_toml(self, filename: str or Path) -> None:
        """Write the saved dictionary as a TOML file (overwrite).

        Args:
            filename: TOML filename
        """
        with Path(filename).open("wb") as fh:
            tomli_w.dump(self._dict, fh)
