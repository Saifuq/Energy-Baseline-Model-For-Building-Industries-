with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix 1: Show the sidebar toggle button (stop hiding the entire header)
old_chrome = "/* ═══ STREAMLIT CHROME ═══ */\n#MainMenu, footer, header { visibility: hidden; }"

new_chrome = """/* ═══ STREAMLIT CHROME ═══ */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
/* Keep header visible so sidebar toggle arrow shows */
header { visibility: visible !important; }
header [data-testid="stToolbar"] { visibility: hidden; }

/* Style the sidebar collapse arrow button to be visible and prominent */
[data-testid="collapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    background: linear-gradient(135deg, #0f172a, #1e3a5f) !important;
    color: #FFFFFF !important;
    border-radius: 0 12px 12px 0 !important;
    border: 2px solid #f97316 !important;
    box-shadow: 4px 0 15px rgba(249,115,22,0.4) !important;
    width: 36px !important;
    height: 60px !important;
    top: 50% !important;
    cursor: pointer !important;
}
[data-testid="collapsedControl"]:hover {
    background: linear-gradient(135deg, #f97316, #f59e0b) !important;
    box-shadow: 4px 0 20px rgba(249,115,22,0.7) !important;
}
[data-testid="collapsedControl"] svg {
    color: #FFFFFF !important;
    fill: #FFFFFF !important;
}

/* Sidebar toggle button inside the sidebar (collapse button) */
button[data-testid="baseButton-header"] {
    background: rgba(249,115,22,0.15) !important;
    border-radius: 8px !important;
}"""

code = code.replace(old_chrome, new_chrome)

# Fix 2: Also update initial_sidebar_state to always be expanded
old_config = 'initial_sidebar_state="expanded",'
new_config = 'initial_sidebar_state="expanded",  # Always show sidebar'
code = code.replace(old_config, new_config)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Patch 11 - Sidebar toggle fix - Applied!")
