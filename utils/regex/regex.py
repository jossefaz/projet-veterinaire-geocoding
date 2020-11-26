import re

REGEX_REGISTRY = {
    "Tel": "^T.l.:",
    "Fax": "^Fax.:",
    "Ordinal": "^N..ordinal"
}


def reg_true(exp: str, string_to_test: str) -> bool:
    return len(re.findall(exp, string_to_test)) == 1


def is_tel(string_to_test: str) -> bool:
    return reg_true(REGEX_REGISTRY["Tel"], string_to_test)


def is_fax(string_to_test: str) -> bool:
    return reg_true(REGEX_REGISTRY["Fax"], string_to_test)


def is_ordinal(string_to_test: str) -> bool:
    return reg_true(REGEX_REGISTRY["Ordinal"], string_to_test)


def remove_non_digit(target_string: str) -> str:
    return re.sub(r"\D", "", target_string)
