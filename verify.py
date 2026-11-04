import json
import subprocess
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
cmd = [sys.executable, str(here / 'callfootprint.py')]
example = here / "input.json"
expected = {'send': [1, 2]}
for args, stdin in [([str(example)], None), ([], example.read_text(encoding="utf-8"))]:
    process = subprocess.run(cmd + args, input=stdin, text=True, capture_output=True)
    assert process.returncode == 0, process.stderr
    assert json.loads(process.stdout) == expected, process.stdout
bad = subprocess.run(cmd, input="{", text=True, capture_output=True)
assert bad.returncode == 2
