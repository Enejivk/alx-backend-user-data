#!/usr/bin/env python3
"""
Module for obfuscating log messages
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Returns the log message obfuscated
    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing the character separating fields
    Returns:
        The obfuscated log message
    """
    return re.sub(f'({"|".join(fields)})=[^{separator}]*', f'\\1={redaction}', message)