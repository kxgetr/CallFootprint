import argparse
import json
import sys
from pathlib import Path

def analyze(data):
    import ast
    out = {}
    for n in ast.walk(ast.parse(data)):
        if isinstance(n, ast.Call):
            out.setdefault(ast.unparse(n.func), []).append(n.lineno)
    return {k: sorted(v) for k, v in out.items()}

def main():
    parser = argparse.ArgumentParser(description='Bir modüldeki çağrı ifadelerini kullanıldıkları satırlarla eşler.')
    parser.add_argument('file', nargs='?', help='UTF-8 JSON input file (default: stdin)')
    parser.add_argument('--source', action='store_true', help='read raw Python source instead of JSON')
    args = parser.parse_args()
    try:
        raw = Path(args.file).read_text(encoding='utf-8-sig') if args.file else sys.stdin.read()
        result = analyze(raw if args.source else json.loads(raw))
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (SyntaxError, ValueError, KeyError, TypeError, OSError, IndexError, ArithmeticError) as error:
        parser.exit(2, f'Invalid input: {error}\n')
if __name__ == '__main__':
    main()
