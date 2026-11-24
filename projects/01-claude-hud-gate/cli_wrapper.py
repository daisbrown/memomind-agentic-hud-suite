"""Explicit, local terminal approval wrapper; not a shell prompt interceptor."""
import argparse
import subprocess
import sys
from risk_analyzer import classify
from memomind_core import HUDFormatter
from memomind_core.simulator import render


def main(argv=None, input_fn=input, runner=subprocess.run):
    parser = argparse.ArgumentParser(description="Review and run one command (no shell).")
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    command = args.command
    if command and command[0] == '--': command = command[1:]
    if not command: parser.error('provide a command after --')
    risk = classify(' '.join(command))
    print(render(HUDFormatter().format([f'[GATE: {risk}]', ' '.join(command), 'Type YES to run'])))
    try: answer = input_fn('Approve this command? Type YES: ')
    except (EOFError, KeyboardInterrupt): return 1
    if answer != 'YES': return 1
    try: return runner(command, check=False).returncode
    except OSError as exc:
        print(f'Could not start command: {exc}', file=sys.stderr)
        return 127

if __name__ == '__main__': sys.exit(main())
