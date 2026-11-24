"""Allowlisted tmux actions require explicit caller confirmation."""
import re
import subprocess
MACROS = {'pytest': 'pytest -lf', 'status': 'git status'}

def dispatch(pane, macro, confirmed=False, runner=subprocess.run):
    if not confirmed: raise PermissionError('explicit confirmation required')
    if not re.fullmatch(r'%[0-9]+', pane): raise ValueError('invalid pane id')
    if macro not in MACROS: raise ValueError('unknown macro')
    runner(['tmux', 'send-keys', '-t', pane, '-l', MACROS[macro]], check=True, timeout=5)
    runner(['tmux', 'send-keys', '-t', pane, 'Enter'], check=True, timeout=5)
