"""Search local Markdown from a terminal; no speech processing or cloud."""
import argparse
from pathlib import Path
from local_index import LocalIndex
from memomind_core import HUDFormatter
from memomind_core.simulator import render

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('directory', type=Path); parser.add_argument('query')
    args=parser.parse_args()
    matches=LocalIndex(sorted(args.directory.rglob('*.md'))).search(args.query, 1)
    if not matches: print('No matching documents'); return
    score,path,body=matches[0]
    first=next((line.strip() for line in body.splitlines() if line.strip()), '')
    print(render(HUDFormatter().format([Path(path).name, first, f'MATCH SCORE: {score}'])))

if __name__ == '__main__': main()
