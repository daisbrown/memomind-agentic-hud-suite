"""Read local Docker container state; no Docker commands modify state."""
import json
import subprocess


def list_containers(runner=subprocess.run):
    result = runner(['docker', 'ps', '--format', '{{json .}}'], capture_output=True, text=True, check=True, timeout=5)
    return [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
