import re

with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

navbar_old = """/* ═══ NAVBAR (Ultra Elite) ═══ */
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
.navbar-brand { font-size: 20px; font-weight: 900; color: #FFFFFF; font-family: Georgia, serif; letter-spacing: 0.01em; }
.navbar-creator { font-size: 12px; color: #94a3b8; margin-top: 5px; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; }"""

navbar_new = """/* ═══ NAVBAR (Ultra Elite) ═══ */
.navbar {
  background: linear-gradient(135deg, #0f172a 0%, #020617 100%);
  padding: 24px 48px;
  display: flex; align-items: center; justify-content: space-between;
  min-height: 110px;
  height: auto;
  flex-wrap: wrap;
  gap: 24px;
  border-radius: 0 0 28px 28px;
  margin-bottom: 44px;
  box-shadow: 0 12px 45px rgba(0, 0, 0, 0.45), inset 0 -1px 0 rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.08);
}
.navbar-brand { font-size: clamp(20px, 2.5vw, 25px); font-weight: 900; color: #FFFFFF; font-family: Georgia, serif; letter-spacing: 0.02em; line-height: 1.25; margin-bottom: 2px; }
.navbar-creator { font-size: 13.5px; color: #94a3b8; margin-top: 6px; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; line-height: 1.5; }"""

if navbar_old in code:
    code = code.replace(navbar_old, navbar_new)
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Applied patch6 successfully.")
else:
    print("WARNING: Could not find old navbar CSS to replace!")
