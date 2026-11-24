"""Read pane metadata from tmux without sending keys."""
import subprocess

def list_panes(runner=subprocess.run):
    result = runner(['tmux', 'list-panes', '-a', '-F', '#{session_name}\t#{window_index}\t#{pane_id}\t#{pane_current_command}\t#{pane_dead}\t#{pane_dead_status}'], capture_output=True, text=True, check=True, timeout=5)
    panes = []
    for line in result.stdout.splitlines():
        parts = line.split('\t')
        if len(parts) != 6: raise ValueError('unexpected tmux output')
        panes.append(dict(zip(('session','window','pane','command','dead','exit_status'), parts)))
    return panes
