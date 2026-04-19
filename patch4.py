import re

with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

selectbox_css_old = """/* 🏙️ SELECTBOX OVERRIDES - PURE WHITE TEXT ON DEEP BLACK */
div[data-baseweb="select"] > div, div[data-baseweb="select"] > div * {
    background-color: #000000 !important;
    color: #FFFFFF !important;
    border-color: #444444 !important;
}
div[data-baseweb="select"] span {
    color: #FFFFFF !important;
}
ul[role="listbox"], div[role="listbox"] {
    background-color: #000000 !important;
}
ul[role="listbox"] li, div[role="listbox"] li {
    background-color: #000000 !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
}
ul[role="listbox"] li *, div[role="listbox"] li * {
    color: #FFFFFF !important;
}
ul[role="listbox"] li:hover, div[role="listbox"] li:hover, ul[role="listbox"] li:hover * {
    background-color: #2D3748 !important;
    color: #FFFFFF !important;
}"""

selectbox_css_new = """/* 🏙️ SELECTBOX OVERRIDES - PURE WHITE TEXT ON DEEP BLACK */
div[data-baseweb="select"] > div, div[data-baseweb="select"] > div * {
    background-color: #000000 !important;
    color: #FFFFFF !important;
    border-color: #444444 !important;
    font-family: Georgia, serif !important;
}
div[data-baseweb="select"] span {
    color: #FFFFFF !important;
}

/* THE POP-UP SCROLLER ITSELF (ABSOLUTE OVERRIDE) */
div[data-baseweb="popover"] {
    background-color: #000000 !important;
}
div[data-baseweb="popover"] div, div[data-baseweb="popover"] ul, div[data-baseweb="popover"] li {
    background-color: #000000 !important;
}
div[data-baseweb="popover"] span, div[data-baseweb="popover"] p, div[data-baseweb="popover"] li * {
    color: #FFFFFF !important;
    font-family: Georgia, serif !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}
div[data-baseweb="popover"] li:hover, div[data-baseweb="popover"] li:hover * {
    background-color: #1A5276 !important;
    color: #FFFFFF !important;
}

ul[role="listbox"], div[role="listbox"], [data-testid="stVirtualDropdown"] {
    background-color: #000000 !important;
}
ul[role="listbox"] li, div[role="listbox"] li, [data-testid="stVirtualDropdown"] li {
    background-color: #000000 !important;
}
ul[role="listbox"] li *, div[role="listbox"] li *, [data-testid="stVirtualDropdown"] li * {
    color: #FFFFFF !important;
    font-family: Georgia, serif !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}
ul[role="listbox"] li:hover, div[role="listbox"] li:hover, ul[role="listbox"] li:hover *, [data-testid="stVirtualDropdown"] li:hover * {
    background-color: #1A5276 !important;
    color: #FFFFFF !important;
}"""

if selectbox_css_old in code:
    code = code.replace(selectbox_css_old, selectbox_css_new)
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Applied patch4 successfully.")
else:
    print("WARNING: Could not find old css inside app.py!")
