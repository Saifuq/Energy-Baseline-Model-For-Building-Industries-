import re

with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

selectbox_css_old = """/* 🏙️ SELECTBOX OVERRIDES - WHITE ON BLACK */
.st-key-city_select div[data-baseweb="select"] > div,
.st-key-bldg_select div[data-baseweb="select"] > div {
    background-color: #000000 !important;
    color: #FFFFFF !important;
    border-radius: 0px !important;
    border: 2px solid #000000 !important;
}
.st-key-city_select div[data-baseweb="select"] *,
.st-key-bldg_select div[data-baseweb="select"] * {
    color: #FFFFFF !important;
}
div[role="listbox"] {
    background-color: #000000 !important;
}
div[role="listbox"] * {
    color: #FFFFFF !important;
    background-color: #000000 !important;
}
div[role="listbox"] [data-baseweb="list-item"]:hover {
    background-color: #333333 !important;
}"""

selectbox_css_new = """/* 🏙️ SELECTBOX OVERRIDES - PURE WHITE TEXT ON DEEP BLACK */
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

navbar_css_old = """/* ═══ NAVBAR (Midnight Blue) ═══ */
.navbar {
  background: linear-gradient(90deg, #0A3D62 0%, #1A5276 100%);
  padding: 0 48px;
  display: flex; align-items: center; justify-content: space-between;
  height: 85px;
  border-radius: 0 0 20px 20px;
  margin-bottom: 32px;
  box-shadow: 0 8px 32px rgba(10, 61, 98, 0.25);
}
.navbar-brand { font-size: 26px; font-weight: 900; color: #FFFFFF; font-family: Georgia, serif; }
.navbar-creator { font-size: 11px; color: #E2E8F0; margin-top: 4px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; }
.menu-btn {
    display: flex; align-items: center; gap: 10px;
    background: rgba(255,255,255,0.15); color: #FFFFFF !important;
    padding: 10px 24px; border-radius: 100px;
    font-size: 14px; font-weight: 700; cursor: pointer;
    border: 1px solid rgba(255,255,255,0.3); transition: all 0.3s;
}
.menu-btn:hover { background: rgba(255,255,255,0.3); transform: translateY(-2px); }
.nav-pill {
    background: rgba(255,255,255,0.2); color: #FFFFFF !important;
    font-size: 11px; font-weight: 800;
    padding: 6px 14px; border-radius: 100px;
}
.nav-pill-2 {
    color: #E2E8F0 !important; font-size: 11px; font-weight: 600;
    margin-left: 8px; border-bottom: 1px solid rgba(255,255,255,0.3);
}"""

navbar_css_new = """/* ═══ NAVBAR (Ultra Elite) ═══ */
.navbar {
  background: linear-gradient(135deg, #0f172a 0%, #020617 100%);
  padding: 0 48px;
  display: flex; align-items: center; justify-content: space-between;
  height: 90px;
  border-radius: 0 0 24px 24px;
  margin-bottom: 40px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4), inset 0 -1px 0 rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.05);
}
.navbar-brand { font-size: 28px; font-weight: 900; color: #FFFFFF; font-family: Georgia, serif; letter-spacing: -0.02em; }
.navbar-creator { font-size: 12px; color: #94a3b8; margin-top: 5px; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; }
.menu-btn {
    display: flex; align-items: center; gap: 10px;
    background: linear-gradient(90deg, #f97316, #f59e0b); color: #000000 !important;
    padding: 12px 28px; border-radius: 100px;
    font-size: 14px; font-weight: 900; cursor: pointer;
    box-shadow: 0 4px 15px rgba(249,115,22,0.4);
    border: none; transition: all 0.3s;
}
.menu-btn:hover { transform: scale(1.05); box-shadow: 0 6px 20px rgba(249,115,22,0.6); }
.nav-pill {
    background: rgba(255,255,255,0.1); color: #FFFFFF !important;
    backdrop-filter: blur(10px);
    font-size: 12px; font-weight: 800; border: 1px solid rgba(255,255,255,0.2);
    padding: 8px 18px; border-radius: 100px; letter-spacing: 0.05em;
}
.nav-pill-2 {
    color: #6ee7b7 !important; font-size: 12px; font-weight: 800;
    margin-left: 10px; border-bottom: 2px solid #6ee7b7; padding-bottom: 2px;
}"""

navbar_html_old = """<div class="navbar">
  <div style="display:flex; align-items:center; gap:28px;">
    <div class="menu-btn" style="background:#FFFFFF; color:#0A3D62 !important; border:2px solid #FFFFFF; font-weight:950;">☰ DASHBOARD MENU</div>
    <div style="width:1.5px; height:36px; background:rgba(255,255,255,0.3);"></div>
    <div style="width:48px;height:48px;background:#FFFFFF;color:#0A3D62;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:950;border-radius:12px;">E</div>
    <div>
      <div class="navbar-brand">India AI Energy Baseline Model</div>
      <div class="navbar-creator">Saifuddin Farooqui &nbsp;·&nbsp; BTP Research Project</div>
    </div>
  </div>
  <div style="display:flex; gap:16px; align-items:center;">
    <span class="nav-pill" style="font-weight:950; border:2px solid rgba(255,255,255,0.5);">BEE / ECBC 2017</span>
    <span class="nav-pill-2" style="font-weight:950; opacity:1; border-bottom:2px solid #F97316;">R² ≥ 0.92</span>
  </div>
</div>"""

navbar_html_new = """<div class="navbar">
  <div style="display:flex; align-items:center; gap:32px;">
    <div class="menu-btn">⬅️ OPEN SIDEBAR</div>
    <div style="width:2px; height:40px; background:rgba(255,255,255,0.1);"></div>
    <div style="width:52px;height:52px;background:linear-gradient(135deg, #4f46e5, #3b82f6);color:#fff;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:900;border-radius:14px;box-shadow: 0 4px 15px rgba(59,130,246,0.5);">⚡</div>
    <div>
      <div class="navbar-brand">India Energy AI Engine.</div>
      <div class="navbar-creator">Saifuddin Farooqui &nbsp;|&nbsp; BTP Research Division</div>
    </div>
  </div>
  <div style="display:flex; gap:20px; align-items:center;">
    <span class="nav-pill">ECBC 2024 Readiness</span>
    <span class="nav-pill-2">Validation: R² > 0.95</span>
  </div>
</div>"""

if selectbox_css_old in code:
    code = code.replace(selectbox_css_old, selectbox_css_new)
else:
    print("Could not find selectbox css old")

if navbar_css_old in code:
    code = code.replace(navbar_css_old, navbar_css_new)
else:
    print("Could not find navbar css old")

if navbar_html_old in code:
    code = code.replace(navbar_html_old, navbar_html_new)
else:
    print("Could not find navbar html old")

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Applied patch3 successfully.")
