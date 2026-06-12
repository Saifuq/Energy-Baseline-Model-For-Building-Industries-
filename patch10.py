with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

old_sidebar = """with st.sidebar:
    st.markdown("### ⚙️ Configuration Matrix")
    st.markdown("---")
    avail_cities = sorted(weather_df["city"].unique().tolist())
    city  = st.selectbox("🏙️ Indian City", avail_cities,
                         index=avail_cities.index("Mumbai") if "Mumbai" in avail_cities else 0,
                         key="city_select")
    bldg  = st.selectbox("🏢 Building Type", list(BLDG_MAP.keys()), key="bldg_select")
    sqft  = st.slider("📐 Built-up Area (sq.ft)", 5000, 500000, 50000, 5000, help="Total conditioned floor space in square feet. Correlates directly with baseline energy volume.")
    age   = st.slider("🏗️ Building Age (yrs)", 1, 50, 12, help="Age of the facility. AI determines potential efficiency degradation and insulation decay over time.")
    tariff= st.slider("💡 Electricity Tariff (₹/kWh)", 4.0, 16.0, 8.0, 0.5, help="Local commercial grid electricity price per unit. Modifies financial ROI projections.")
    st.markdown("---")
    st.markdown("<b>🛡️ Advanced Simulation Params</b>", unsafe_allow_html=True)
    target_sav = st.slider("🎯 AI Optimization Target (%)", 5, 50, 15, 1, help="Simulate a percentage load reduction driven by AI recommendations to view hypothetical savings.")
    grid_std   = st.radio("🔋 Grid Emission Standard", ["CEA 2023 (India)", "Global Baseline (IEA)"])
    st.markdown("---")
    st.markdown("<b>Model Specification</b>", unsafe_allow_html=True)
    st.caption("Algorithm: XGBoost (hist)  \\nFeatures: 31  \\nTraining: ASHRAE Kaggle 2.5M rows  \\nValidation: NASA POWER + IMD Synthetic")
    st.markdown("---")
    st.markdown(\"\"\"
    <div style='font-size:12px;line-height:1.8;color:#000; font-weight:600;'>
    <b>Researcher & Creator</b><br>
    Saifuddin Farooqui<br>
    <span style='font-size:11px;color:#4B5563; font-weight:400;'>
    BTP Final Year Project<br>
    Energy Baseline Model for<br>
    Buildings & Industries — India
    </span>
    </div>
    \"\"\", unsafe_allow_html=True)"""

new_sidebar = """with st.sidebar:

    # ── SIDEBAR HEADER ──
    st.markdown(\"\"\"
    <div style='background:linear-gradient(135deg,#0f172a,#1e3a5f);
                border-radius:14px; padding:20px 16px; margin-bottom:18px;
                text-align:center; border:1px solid rgba(255,255,255,0.1);'>
      <div style='font-size:26px; margin-bottom:6px;'>⚡</div>
      <div style='font-size:15px; font-weight:900; color:#FFFFFF;
                  font-family:Georgia,serif; letter-spacing:0.03em;'>
        AI Energy Engine
      </div>
      <div style='font-size:10.5px; color:#94a3b8; margin-top:4px;
                  font-weight:700; letter-spacing:0.12em; text-transform:uppercase;'>
        BTP · Saifuddin Farooqui
      </div>
    </div>
    \"\"\", unsafe_allow_html=True)

    # ── CITY QUICK-SELECT CARDS ──
    st.markdown(\"\"\"
    <div style='font-size:11px; font-weight:900; color:#0A3D62;
                letter-spacing:0.18em; text-transform:uppercase;
                border-left:3px solid #f97316; padding-left:10px; margin-bottom:12px;'>
      🏙️ Select Indian City
    </div>
    \"\"\", unsafe_allow_html=True)

    # City metadata: name → (emoji, climate zone, typical ECI reference)
    CITY_SIDEBAR = {
        "Ahmedabad":  ("🌵", "Hot & Dry",      "High EPI"),
        "Bengaluru":  ("🌸", "Composite",       "Moderate EPI"),
        "Chennai":    ("🌊", "Warm & Humid",    "High EPI"),
        "Delhi":      ("🏛️", "Composite",       "High EPI"),
        "Hyderabad":  ("🔷", "Composite",       "Moderate EPI"),
        "Jaipur":     ("🏰", "Hot & Dry",       "High EPI"),
        "Kanpur":     ("🏭", "Composite",       "Moderate EPI"),
        "Kolkata":    ("🌿", "Warm & Humid",    "High EPI"),
        "Lucknow":    ("🌙", "Composite",       "Moderate EPI"),
        "Mumbai":     ("🌴", "Warm & Humid",    "High EPI"),
        "Nagpur":     ("🌞", "Hot & Dry",       "High EPI"),
        "Pune":       ("🏔️", "Composite",       "Low EPI"),
        "Surat":      ("⚓", "Warm & Humid",    "Moderate EPI"),
        "Vadodara":   ("🎭", "Hot & Dry",       "High EPI"),
        "Visakhapatnam": ("🐚", "Warm & Humid", "High EPI"),
        "Bhopal":     ("🌲", "Composite",       "Moderate EPI"),
    }

    avail_cities = sorted(weather_df["city"].unique().tolist())

    # City pills display
    city_cols = st.columns(2)
    city_pill_style_active   = "background:#0A3D62;color:#fff;border:2px solid #0A3D62;"
    city_pill_style_inactive = "background:#fff;color:#0A3D62;border:2px solid #CBD5E1;"

    # Use session state to track clicked city
    if "selected_city" not in st.session_state:
        st.session_state.selected_city = "Mumbai" if "Mumbai" in avail_cities else avail_cities[0]

    city_grid_html = "<div style='display:grid; grid-template-columns:1fr 1fr; gap:6px; margin-bottom:14px;'>"
    for c in avail_cities:
        meta   = CITY_SIDEBAR.get(c, ("🏙️", "Composite", "Moderate EPI"))
        is_sel = (c == st.session_state.selected_city)
        bg     = "#0f172a"  if is_sel else "#f8fafc"
        col    = "#FFFFFF"  if is_sel else "#0f172a"
        border = "#f97316"  if is_sel else "#e2e8f0"
        city_grid_html += f\"\"\"
          <div style='background:{bg}; color:{col}; border:2px solid {border};
                      border-radius:10px; padding:7px 8px; text-align:center;
                      font-family:Georgia,serif; cursor:pointer; transition:all 0.2s;
                      font-size:12px; font-weight:{"900" if is_sel else "700"};'>
            {meta[0]} {c}
          </div>\"\"\"
    city_grid_html += "</div>"
    st.markdown(city_grid_html, unsafe_allow_html=True)

    city = st.selectbox("🏙️ Indian City", avail_cities,
                        index=avail_cities.index(st.session_state.selected_city)
                              if st.session_state.selected_city in avail_cities else 0,
                        key="city_select",
                        help="Select the Indian city for energy simulation. Each city has its own NASA POWER calibrated weather profile.")
    st.session_state.selected_city = city

    # Show selected city info card
    city_meta = CITY_SIDEBAR.get(city, ("🏙️", "Composite", "Moderate EPI"))
    ZONE_COLORS = {"Hot & Dry": "#f97316", "Warm & Humid": "#3b82f6", "Composite": "#10B981"}
    zc = ZONE_COLORS.get(city_meta[1], "#6366f1")
    st.markdown(f\"\"\"
    <div style='background:#f8fafc; border-radius:12px; padding:14px 16px;
                border-left:4px solid {zc}; margin-bottom:16px;'>
      <div style='font-size:22px; margin-bottom:4px;'>{city_meta[0]} <b style="font-size:15px;color:#0f172a;">{city}</b></div>
      <div style='display:flex; gap:8px; flex-wrap:wrap; margin-top:6px;'>
        <span style='background:{zc}22; color:{zc}; border:1px solid {zc}55;
                     border-radius:20px; padding:3px 10px; font-size:11px; font-weight:800;'>
          🌡️ {city_meta[1]}
        </span>
        <span style='background:#f0fdf4; color:#16a34a; border:1px solid #bbf7d0;
                     border-radius:20px; padding:3px 10px; font-size:11px; font-weight:800;'>
          📊 {city_meta[2]}
        </span>
      </div>
    </div>
    \"\"\", unsafe_allow_html=True)

    st.markdown("<hr style='border:0;border-top:1.5px dashed #e2e8f0;margin:8px 0 16px;'>", unsafe_allow_html=True)

    # ── BUILDING TYPE ──
    st.markdown(\"\"\"
    <div style='font-size:11px; font-weight:900; color:#0A3D62;
                letter-spacing:0.18em; text-transform:uppercase;
                border-left:3px solid #f97316; padding-left:10px; margin-bottom:10px;'>
      🏢 Building Type
    </div>
    \"\"\", unsafe_allow_html=True)

    BLDG_ICONS = {
        "Education":                  "🎓",
        "Lodging/residential":        "🏠",
        "Office":                     "💼",
        "Entertainment/public assembly": "🎭",
        "Retail":                     "🛍️",
        "Parking":                    "🅿️",
        "Public services":            "🏛️",
        "Warehouse/storage":          "📦",
        "Food sales and service":     "🍽️",
    }

    bldg_labels = list(BLDG_MAP.keys())
    bldg_display = [f"{BLDG_ICONS.get(b,'🏢')} {b}" for b in bldg_labels]
    bldg_sel = st.selectbox("🏢 Building Type", bldg_display, key="bldg_select",
                            help="Commercial building category. Each type has different occupancy profiles and ECBC EPI benchmarks.")
    bldg = bldg_labels[bldg_display.index(bldg_sel)]

    st.markdown("<hr style='border:0;border-top:1.5px dashed #e2e8f0;margin:12px 0;'>", unsafe_allow_html=True)

    # ── PARAMETERS ──
    st.markdown(\"\"\"
    <div style='font-size:11px; font-weight:900; color:#0A3D62;
                letter-spacing:0.18em; text-transform:uppercase;
                border-left:3px solid #10B981; padding-left:10px; margin-bottom:10px;'>
      ⚙️ Building Parameters
    </div>
    \"\"\", unsafe_allow_html=True)

    sqft  = st.slider("📐 Built-up Area (sq.ft)", 5000, 500000, 50000, 5000,
                      help="Total conditioned floor space. Directly scales baseline energy volume.")
    age   = st.slider("🏗️ Building Age (yrs)", 1, 50, 12,
                      help="Older buildings have higher EPI due to insulation degradation and legacy HVAC systems.")
    tariff= st.slider("💡 Tariff (₹/kWh)", 4.0, 16.0, 8.0, 0.5,
                      help="Commercial electricity tariff. Converts predicted kWh to financial cost (₹ Lakhs).")

    st.markdown("<hr style='border:0;border-top:1.5px dashed #e2e8f0;margin:12px 0;'>", unsafe_allow_html=True)

    # ── ADVANCED ──
    st.markdown(\"\"\"
    <div style='font-size:11px; font-weight:900; color:#0A3D62;
                letter-spacing:0.18em; text-transform:uppercase;
                border-left:3px solid #8B5CF6; padding-left:10px; margin-bottom:10px;'>
      🛡️ Advanced Simulation
    </div>
    \"\"\", unsafe_allow_html=True)

    target_sav = st.slider("🎯 AI Optimization Target (%)", 5, 50, 15, 1,
                           help="Hypothetical reduction via AI recommendations. Models best-case retrofit outcomes.")
    grid_std   = st.radio("🔋 Grid Standard",
                          ["CEA 2023 (India)", "Global Baseline (IEA)"],
                          help="Emission factor standard used for CO₂ footprint calculation.")

    st.markdown("<hr style='border:0;border-top:1.5px dashed #e2e8f0;margin:12px 0;'>", unsafe_allow_html=True)

    # ── MODEL INFO ──
    st.markdown(\"\"\"
    <div style='background:#f8fafc; border-radius:12px; padding:14px 16px;
                border:1px solid #e2e8f0; margin-bottom:12px; font-size:12px;
                font-family:Georgia,serif; line-height:1.8; color:#334155;'>
      <b style='color:#0f172a; font-size:13px;'>🧠 Model Specification</b><br>
      <span style='color:#6366f1; font-weight:800;'>Algorithm:</span> XGBoost (hist)<br>
      <span style='color:#6366f1; font-weight:800;'>Features:</span> 31 Variables<br>
      <span style='color:#6366f1; font-weight:800;'>Training:</span> ASHRAE 2.5M rows<br>
      <span style='color:#6366f1; font-weight:800;'>Validation:</span> NASA POWER + IMD
    </div>
    \"\"\", unsafe_allow_html=True)

    # ── CREATOR CARD ──
    st.markdown(\"\"\"
    <div style='background:linear-gradient(135deg,#0f172a,#1e3a5f);
                border-radius:12px; padding:16px; text-align:center;
                border:1px solid rgba(255,255,255,0.1);'>
      <div style='font-size:11px; color:#94a3b8; font-weight:700;
                  letter-spacing:0.15em; text-transform:uppercase; margin-bottom:6px;'>
        Researcher & Creator
      </div>
      <div style='font-size:15px; font-weight:900; color:#FFFFFF;
                  font-family:Georgia,serif;'>
        Saifuddin Farooqui
      </div>
      <div style='font-size:10.5px; color:#6ee7b7; margin-top:4px; font-weight:700;'>
        BTP Final Year Project<br>Energy Baseline Model
      </div>
      <div style='font-size:10px; color:#94a3b8; margin-top:6px;'>
        Supervisor: Dr. Sivasankari Sundaram
      </div>
    </div>
    \"\"\", unsafe_allow_html=True)"""

if old_sidebar in code:
    code = code.replace(old_sidebar, new_sidebar)
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Patch 10 — Enhanced Sidebar — Applied Successfully!")
else:
    print("WARNING: Could not find old sidebar block!")
