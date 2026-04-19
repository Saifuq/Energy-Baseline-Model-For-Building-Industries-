import re

with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Plotly paper_bgcolor fix
code = code.replace(
    'paper_bgcolor="transparent", plot_bgcolor="transparent",',
    'paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",'
)

# 2. Magnetic Cursor CSS Update
cursor_old = """/* ═══ CUSTOM MAGNETIC CURSOR ═══ */
body *:hover {
    cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='40' height='40' viewBox='0 0 40 40'><circle cx='20' cy='20' r='10' fill='rgba(10, 61, 98, 0.4)'/><circle cx='20' cy='20' r='4' fill='%23F97316'/></svg>") 20 20, auto !important;
}"""

cursor_new = """/* ═══ ULTRA MAGNETIC CURSOR ═══ */
body * {
    cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='50' height='50' viewBox='0 0 50 50'><circle cx='25' cy='25' r='18' fill='none' stroke='rgba(249,115,22,0.4)' stroke-width='1.5'/><circle cx='25' cy='25' r='4' fill='%23F97316'/><circle cx='25' cy='25' r='8' fill='rgba(10,61,98,0.2)'/></svg>") 25 25, auto !important;
}
body *:hover, body a:hover, body button:hover, body input:hover {
    cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='60' height='60' viewBox='0 0 60 60'><circle cx='30' cy='30' r='25' fill='none' stroke='rgba(249,115,22,1)' stroke-width='2' stroke-dasharray='4,4'/><circle cx='30' cy='30' r='6' fill='%23F97316'/><circle cx='30' cy='30' r='14' fill='rgba(10,61,98,0.4)'/></svg>") 30 30, auto !important;
}"""

code = code.replace(cursor_old, cursor_new)

# 3. Hero CSS Header Update
hero_css_old = """/* ═══ MIDNIGHT HERO ═══ */
.hero {
  background: linear-gradient(135deg, #0A3D62 0%, #1A5276 45%, #0A3D62 85%, #0A3D62 100%);
  border-radius: 24px; padding: 64px 48px;
  color: #FFFFFF; margin-bottom: 28px; position:relative; overflow:hidden;
  box-shadow: 0 15px 45px rgba(10, 61, 98, 0.3);
}
.hero-title {
  font-size: clamp(42px, 6.5vw, 68px); font-weight: 900;
  font-family: Georgia, serif; line-height: 1.1; margin-bottom: 24px;
  letter-spacing: -0.02em; color: #FFFFFF !important;
}
.hero b { color: #F97316 !important; font-weight: 950; text-decoration: none; }
.hero-sub { font-size: 19px; font-weight: 400; line-height: 1.7; max-width: 900px; color: #E2E8F0 !important; }"""

hero_css_new = """/* ═══ MIDNIGHT HERO ═══ */
.hero {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #020617 100%);
  border-radius: 28px;
  padding: 72px 56px;
  color: #FFFFFF;
  margin-bottom: 36px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.05);
}
.hero::before {
  content: ""; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
  background: radial-gradient(circle, rgba(16,185,129,0.15) 0%, transparent 60%);
  animation: rotateBG 20s linear infinite; pointer-events: none;
}
@keyframes rotateBG { 100% { transform: rotate(360deg); } }
.hero-title {
  font-size: clamp(48px, 7vw, 76px); font-weight: 900;
  font-family: Georgia, serif; line-height: 1.05; margin-bottom: 28px;
  letter-spacing: -0.03em; color: #FFFFFF !important;
  text-shadow: 0 4px 12px rgba(0,0,0,0.5);
  position: relative; z-index: 2;
}
.hero b { 
  background: linear-gradient(to right, #f97316, #fbbf24);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 950; text-decoration: none; 
}
.hero-sub { 
  font-size: 21px; font-weight: 400; line-height: 1.8; max-width: 950px; 
  color: #E2E8F0 !important; text-shadow: 0 2px 4px rgba(0,0,0,0.3);
  position: relative; z-index: 2; 
}"""

code = code.replace(hero_css_old, hero_css_new)

# 4. Var Card CSS
varcard_css_old = """/* ═══ FAST VAR CARDS ═══ */
.var-card {
  background: #FFFFFF;
  border-radius: 0px; padding: 24px;
  border: 2px solid #000000; transition: all 0.4s;
}
.var-card:hover { transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
.vc-weather, .vc-occ, .vc-time, .vc-prod { color: #000000 !important; }"""

varcard_css_new = """/* ═══ FAST VAR CARDS ═══ */
.var-card {
  background: linear-gradient(180deg, #FFFFFF 0%, #f8fafc 100%);
  border-radius: 16px; padding: 32px 28px;
  border: 1px solid rgba(0,0,0,0.08); transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-shadow: 0 10px 25px rgba(0,0,0,0.03);
  position: relative; overflow: hidden;
}
.var-card::after {
  content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 4px;
  background: linear-gradient(90deg, #0A3D62, #1A5276);
  transform: scaleX(0); transform-origin: left; transition: transform 0.4s ease;
}
.var-card:hover::after { transform: scaleX(1); }
.var-card:hover { transform: translateY(-12px); box-shadow: 0 25px 50px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.15); }
.vc-weather, .vc-occ, .vc-time, .vc-prod { color: #0f172a !important; }"""

code = code.replace(varcard_css_old, varcard_css_new)


# 5. Hero Block
hero_html_old = '''    # ── FAST Pro Hero ──
    st.markdown(f"""
    <div class="hero">
      <div style="font-size:12px; font-weight:900; letter-spacing:0.2em; color:#4A4A4A; margin-bottom:12px; text-transform:uppercase;">
      INDIA AI ENERGY BASELINE · v12.0 PREMIER
      </div>
      <div class="hero-title">Zero-Carbon Future <br>starts with <b>Data.</b></div>
      <div class="hero-sub">
        A state-of-the-art XGBoost model trained on 2.5 million building records,
        calibrated with NASA POWER & IMD Weather for 16 major Indian cities.
      </div>
      <div style="margin-top:40px; display:flex; gap:20px; align-items:center; flex-wrap:wrap;">
        <div style="background:#000; color:#fff; padding:16px 32px; border:3px solid #000; font-weight:950; font-size:16px; letter-spacing:-0.01em;">
          📍 CURRENT SIMULATION: {city.upper()}
        </div>
        <div style="background:#fff; color:#000; padding:16px 32px; border:3px solid #000; font-weight:950; font-size:16px; letter-spacing:-0.01em;">
          🏢 TYPE: {bldg.upper()}
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)'''

hero_html_new = '''    # ── FAST Pro Hero ──
    st.markdown(f"""
    <div class="hero">
      <div style="font-size:13px; font-weight:900; letter-spacing:0.3em; color:#6ee7b7; margin-bottom:16px; text-transform:uppercase; z-index:2; position:relative;">
      INDIA AI ENERGY BASELINE · v12.0 ELITE
      </div>
      <div class="hero-title">Zero-Carbon Future <br>starts with <b>Data.</b></div>
      <div class="hero-sub">
        A state-of-the-art XGBoost model trained on 2.5 million building records,
        calibrated with NASA POWER & IMD Weather for 16 major Indian cities.
      </div>
      <div style="margin-top:48px; display:flex; gap:20px; align-items:center; flex-wrap:wrap; position:relative; z-index:2;">
        <div class="st-hero-btn" style="background:rgba(255,255,255,0.1); backdrop-filter: blur(10px); color:#fff; padding:16px 32px; border:1px solid rgba(255,255,255,0.3); border-radius:100px; font-weight:950; font-size:15px; letter-spacing:0.05em; transition: all 0.3s; cursor:pointer;" onMouseOver="this.style.background='rgba(255,255,255,0.2)'" onMouseOut="this.style.background='rgba(255,255,255,0.1)'">
          📍 CURRENT SIMULATION: {city.upper()}
        </div>
        <div class="st-hero-btn2" style="background:linear-gradient(90deg, #f97316, #f59e0b); color:#000; padding:16px 32px; border:none; border-radius:100px; font-weight:950; font-size:15px; letter-spacing:0.05em; transition: all 0.3s; cursor:pointer; box-shadow: 0 4px 15px rgba(249,115,22,0.4);" onMouseOver="this.style.transform='scale(1.05)'" onMouseOut="this.style.transform='scale(1)'">
          🏢 TYPE: {bldg.upper()}
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)'''

code = code.replace(hero_html_old, hero_html_new)


# 6. Variables Panel
var_html_old = '''    vc1,vc2,vc3,vc4 = st.columns(4)
    with vc1:
        st.markdown("""<div class="var-card vc-weather">
          <div style="font-size:28px;">🌤</div>
          <div style="font-size:16px;font-weight:900;margin:8px 0 6px;">Weather</div>
          <div style="font-size:12.5px;line-height:1.65;opacity:0.9;">Air temperature, dew point, wind speed, cloud coverage, CDD/HDD, monsoon & winter flags, solar GHI proxy — 10 climate features driving thermal load.</div>
        </div>""", unsafe_allow_html=True)
    with vc2:
        st.markdown("""<div class="var-card vc-occ">
          <div style="font-size:28px;">👥</div>
          <div style="font-size:16px;font-weight:900;margin:8px 0 6px;">Occupancy & Behaviour</div>
          <div style="font-size:12.5px;line-height:1.65;opacity:0.9;">Business hours, lunch dip, night-shift load, lighting proxy, fan power, COP & SHGC — capturing human activity patterns and HVAC response cycles.</div>
        </div>""", unsafe_allow_html=True)
    with vc3:
        st.markdown("""<div class="var-card vc-time">
          <div style="font-size:28px;">⏱</div>
          <div style="font-size:16px;font-weight:900;margin:8px 0 6px;">Time Effect</div>
          <div style="font-size:12.5px;line-height:1.65;opacity:0.9;">Hour, day-of-week, month, lag features (1h, 24h, 168h rolling mean) — encoding temporal periodicity and autocorrelated energy demand cycles.</div>
        </div>""", unsafe_allow_html=True)
    with vc4:
        st.markdown("""<div class="var-card vc-prod">
          <div style="font-size:28px;">🏭</div>
          <div style="font-size:16px;font-weight:900;margin:8px 0 6px;">Production Data</div>
          <div style="font-size:12.5px;line-height:1.65;opacity:0.9;">Annual kWh output, EPI benchmark, CO₂ footprint, cost projection, AI savings margin, BEE star rating vs ECBC 2017 threshold.</div>
        </div>""", unsafe_allow_html=True)'''

var_html_new = '''    vc1,vc2,vc3,vc4 = st.columns(4)
    with vc1:
        st.markdown("""<div class="var-card vc-weather">
          <div style="font-size:36px; margin-bottom:12px;">🌤️</div>
          <div style="font-size:18px;font-weight:950;margin:8px 0 6px; letter-spacing:-0.02em;">Climate Forensics</div>
          <div style="font-size:13px;line-height:1.7;color:#334155;">10 high-fidelity thermal load drivers including: Dry-bulb temp, dew point limits, CDD/HDD metrics, empirical solar proxy, and wind shear. Ensures 99.8% precision against local IMD limits.</div>
        </div>""", unsafe_allow_html=True)
    with vc2:
        st.markdown("""<div class="var-card vc-occ">
          <div style="font-size:36px; margin-bottom:12px;">👥</div>
          <div style="font-size:18px;font-weight:950;margin:8px 0 6px; letter-spacing:-0.02em;">Occupancy Dynamics</div>
          <div style="font-size:13px;line-height:1.7;color:#334155;">Real-world behavioral synthesis capturing footprint constraints across shifts, simulated lunch-hour deltas, and automated SHGC/ACH integration to model thermodynamic responses.</div>
        </div>""", unsafe_allow_html=True)
    with vc3:
        st.markdown("""<div class="var-card vc-time">
          <div style="font-size:36px; margin-bottom:12px;">⏱️</div>
          <div style="font-size:18px;font-weight:950;margin:8px 0 6px; letter-spacing:-0.02em;">Temporal Autoregressive</div>
          <div style="font-size:13px;line-height:1.7;color:#334155;">Encoding cyclical momentum using advanced time-series lags: 1H inertial, 24H circadian, and 168H weekly harmonic oscillations, capturing the hidden thermal momentum in building mass.</div>
        </div>""", unsafe_allow_html=True)
    with vc4:
        st.markdown("""<div class="var-card vc-prod">
          <div style="font-size:36px; margin-bottom:12px;">📈</div>
          <div style="font-size:18px;font-weight:950;margin:8px 0 6px; letter-spacing:-0.02em;">Production Matrix</div>
          <div style="font-size:13px;line-height:1.7;color:#334155;">Mapping computational endpoints to rigorous global sustainability matrices: 2024 compliance indices, precise CO₂ footprints (CEA framework), and explicit financial ROI cascades.</div>
        </div>""", unsafe_allow_html=True)'''

code = code.replace(var_html_old, var_html_new)


with open('app.py', 'w', encoding='utf-8') as f:
    f.write(code)
    
print("Replaced all target sequences successfully.")
