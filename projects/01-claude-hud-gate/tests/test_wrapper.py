from types import SimpleNamespace
from cli_wrapper import main

def test_reject_and_approve_without_shell():
    calls = []
    def run(cmd, check):
        calls.append((cmd, check)); return SimpleNamespace(returncode=7)
    assert main(['--', 'echo', 'hello'], lambda _: 'no', run) == 1
    assert calls == []
    assert main(['--', 'echo', 'hello'], lambda _: 'YES', run) == 7
    assert calls == [(['echo', 'hello'], False)]

def test_eof_fails_closed():
    def eof(_): raise EOFError()
    assert main(['echo'], eof) == 1
