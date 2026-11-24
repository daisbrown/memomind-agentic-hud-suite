"""Explicitly interactive tmux macro runner."""
import argparse
from pane_watcher import list_panes
from gesture_macro_router import dispatch, MACROS

def main():
    p=argparse.ArgumentParser(); p.add_argument('--pane'); p.add_argument('--macro', choices=MACROS)
    args=p.parse_args()
    if not args.pane and not args.macro:
        for pane in list_panes(): print(pane)
        return
    if not args.pane or not args.macro: p.error('both --pane and --macro required')
    print('WARNING: sends input and Enter to the selected pane, including any existing input.')
    try: answer=input(f'Type YES to send {MACROS[args.macro]!r} to {args.pane}: ')
    except (EOFError, KeyboardInterrupt): return
    if answer == 'YES': dispatch(args.pane,args.macro,confirmed=True)

if __name__ == '__main__': main()
