"""Simple inspectable lexical document index; no vector or latency claims."""
from pathlib import Path
import re
from collections import Counter

def tokens(text): return re.findall(r'[a-z0-9]+', text.lower())

class LocalIndex:
    def __init__(self, docs): self.docs = [(str(path), Path(path).read_text(encoding='utf-8')) for path in docs]
    def search(self, query, limit=3):
        terms = set(tokens(query))
        if not terms or limit <= 0: return []
        scored = []
        for path, body in self.docs:
            counts = Counter(tokens(body))
            score = sum(counts[t] for t in terms)
            if score: scored.append((score, path, body))
        return sorted(scored, key=lambda x: (-x[0], x[1]))[:limit]
