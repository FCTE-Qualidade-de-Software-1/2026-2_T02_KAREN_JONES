import re
import os

with open('artigo/main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Balanced environments
begins = re.findall(r'\\begin\{([^}]+)\}', text)
ends = re.findall(r'\\end\{([^}]+)\}', text)
print(f'Total \\begin: {len(begins)}, Total \\end: {len(ends)}')
stack = []
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}', text):
    kind, env = m.groups()
    if kind == 'begin':
        stack.append((env, m.start()))
    else:
        if not stack:
            print(f'ERROR: Extra \\end{{{env}}}')
        else:
            top_env, top_pos = stack.pop()
            if top_env != env:
                print(f'ERROR: Mismatched \\begin{{{top_env}}} and \\end{{{env}}}')
if stack:
    print('ERROR: Unclosed environments:', [s[0] for s in stack])
else:
    print('SUCCESS: All environments properly balanced!')

# 2. Citations
cites = set(re.findall(r'\\cite\{([^}]+)\}', text))
with open('artigo/bibliography.bib', 'r', encoding='utf-8') as f:
    bib = f.read()
bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib))
print('Citations used:', sorted(list(cites)))
print('Bib keys present:', sorted(list(bib_keys)))
missing_cites = cites - bib_keys
if missing_cites:
    print('ERROR: Missing citations in .bib:', missing_cites)
else:
    print('SUCCESS: All citations found in bib!')

# 3. References and Labels
labels = set(re.findall(r'\\label\{([^}]+)\}', text))
refs = set(re.findall(r'\\ref\{([^}]+)\}', text))
missing_refs = refs - labels
if missing_refs:
    print('ERROR: Missing labels for refs:', missing_refs)
else:
    print('SUCCESS: All refs have corresponding labels!')

# 4. Images
images = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', text)
for img in images:
    path = os.path.join('artigo', img)
    found = os.path.exists(path) or os.path.exists(path + '.png') or os.path.exists(path + '.pdf')
    if not found:
        print('ERROR: Missing image file:', path)
    else:
        print('SUCCESS: Image verified:', path)

# 5. Prohibited terms and style
if 'psm' in text.lower():
    print('WARNING: found psm in text!')
else:
    print('SUCCESS: No PSM found in main.tex!')

cid_matches = [m.group(0) for m in re.finditer(r'\bCID\b', text)]
if cid_matches:
    print('WARNING: found CID acronym in text:', cid_matches)
else:
    print('SUCCESS: No CID acronym found!')

if any(dash in text for dash in ['---', '—', '–']):
    print('WARNING: found em/en dash in text!')
else:
    print('SUCCESS: No dashes found!')

if any(lst in text for lst in ['\\begin{itemize}', '\\begin{enumerate}']):
    print('WARNING: found list in text!')
else:
    print('SUCCESS: No lists found!')
