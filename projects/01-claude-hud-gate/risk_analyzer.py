"""Heuristics for a simulator, not a security boundary."""
import re

def classify(command, files=()):
    text = " ".join([command, *files]).lower()
    if re.search(r"\b(drop|truncate)\b|\brm\s+-(?:[a-z]*r[a-z]*f|[a-z]*f[a-z]*r)|--force(?:\b|=)|(?:^|[ /])\.env\b|\bdeploy\b.*\bprod", text):
        return "HIGH"
    if re.search(r"\b(?:install|update|upgrade|migrate)\b", text):
        return "MED"
    return "LOW"
