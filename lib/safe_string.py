"""
Lib - Safe String
"""
import re

from unidecode import unidecode

RFC_REGEXP = r"^[A-ZÑ&]{3,4}\d{6}(?:[A-Z\d]{3})?$"


def safe_rfc(input_str: str) -> str:
    """Safe RFC"""
    removed_spaces = re.sub(r"\s", "", input_str)
    removed_simbols = re.sub(r"[^a-zA-Z0-9]+", "", removed_spaces)
    final = unidecode(removed_simbols.upper())
    if re.fullmatch(RFC_REGEXP, final) is None:
        raise ValueError("RFC es incorrecto")
    return final
