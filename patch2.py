import re

with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix remaining paper_bgcolor="transparent"
code = code.replace('paper_bgcolor="transparent"', 'paper_bgcolor="rgba(0,0,0,0)"')
code = code.replace("paper_bgcolor='transparent'", 'paper_bgcolor="rgba(0,0,0,0)"')
code = code.replace('plot_bgcolor="transparent"', 'plot_bgcolor="rgba(0,0,0,0)"')
code = code.replace("plot_bgcolor='transparent'", 'plot_bgcolor="rgba(0,0,0,0)"')

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Replaced all remaining Plotly transparent backgrounds.")
