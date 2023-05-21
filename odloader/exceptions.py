from __future__ import annotations
from pathlib import Path


class _BaseException(Exception):
    """Basic class of exception.

    Args:
        message: main message of error, should be set in child classes
        details: details of error
    """

    def __init__(self, message: str, details: str | None = None) -> None:
        self._message = message
        self._details = "" if details is None else f" {details}."

    def __str__(self):
        return f"{self._message}. {self._details}"


class ParseError(_BaseException):
    """Error when parsing files.

    Args:
        filename: file which we tried to parse
        ext: expected extention of the file
        details: details of error
    """

    def __init__(self, filename: str | Path, ext: str, details: str | None = None) -> None:
        message = f"We tried to parse {filename} as a {ext.upper()} file, but failed"
        super().__init__(message=message, details=details)
