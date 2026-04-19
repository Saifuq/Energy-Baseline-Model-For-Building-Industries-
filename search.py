import sys
lines = open('app.py', encoding='utf-8').readlines()
with open('search.txt', 'w', encoding='utf-8') as f:
    for i, ln in enumerate(lines):
        ln_lower = ln.lower()
        if 'research' in ln_lower or 'ashrae' in ln_lower:
            f.write(f'{i+1}: {ln}')
