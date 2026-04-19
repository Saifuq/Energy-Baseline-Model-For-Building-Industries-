import sys

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    'sqft  = st.slider("📐 Built-up Area (sq.ft)", 5000, 500000, 50000, 5000)',
    'sqft  = st.slider("📐 Built-up Area (sq.ft)", 5000, 500000, 50000, 5000, help="Total conditioned floor space in square feet. Correlates directly with baseline energy volume.")'
)

text = text.replace(
    'age   = st.slider("🏗️ Building Age (yrs)", 1, 50, 12)',
    'age   = st.slider("🏗️ Building Age (yrs)", 1, 50, 12, help="Age of the facility. AI determines potential efficiency degradation and insulation decay over time.")'
)

text = text.replace(
    'tariff= st.slider("💡 Electricity Tariff (₹/kWh)", 4.0, 16.0, 8.0, 0.5)',
    'tariff= st.slider("💡 Electricity Tariff (₹/kWh)", 4.0, 16.0, 8.0, 0.5, help="Local commercial grid electricity price per unit. Modifies financial ROI projections.")'
)

text = text.replace(
    'target_sav = st.slider("🎯 AI Optimization Target (%)", 5, 50, 15, 1)',
    'target_sav = st.slider("🎯 AI Optimization Target (%)", 5, 50, 15, 1, help="Simulate a percentage load reduction driven by AI recommendations to view hypothetical savings.")'
)

text = text.replace(
    'new_cop  = st.slider("Improve HVAC COP", 3.0, 6.0, float(pr[\'COP\']), 0.1)',
    'new_cop  = st.slider("Improve HVAC COP", 3.0, 6.0, float(pr[\'COP\']), 0.1, help="Coefficient of Performance measures cooling efficiency. Upgrading to a 5.0+ COP chiller slashes energy waste dramatically.")'
)

text = text.replace(
    'new_shgc = st.slider("Lower Glass SHGC", 0.15, 0.60, float(pr[\'SHGC\']), 0.05)',
    'new_shgc = st.slider("Lower Glass SHGC", 0.15, 0.60, float(pr[\'SHGC\']), 0.05, help="Solar Heat Gain Coefficient. Lower value prevents external sun-heat from entering, vastly decreasing AC thermal load.")'
)

text = text.replace(
    'new_ach  = st.slider("Tighten Air ACH", 0.5, 15.0, float(pr[\'ACH\']), 0.5)',
    'new_ach  = st.slider("Tighten Air ACH", 0.5, 15.0, float(pr[\'ACH\']), 0.5, help="Air Changes per Hour. Tighter building sealing lowers ACH, heavily avoiding cold air leakage.")'
)

df_old = '''    audit_df = pd.DataFrame(audit_rows)
    st.dataframe(audit_df, use_container_width=True, hide_index=True)'''

df_new = '''    audit_df = pd.DataFrame(audit_rows)
    st.dataframe(audit_df, use_container_width=True, hide_index=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    csv_data = audit_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Export Financial & Carbon Audit (CSV)",
        data=csv_data,
        file_name=f"{city.replace(' ', '_')}_{bldg.replace('/', '_')}_AI_Audit.csv",
        mime='text/csv',
        type="primary"
    )'''

if df_old in text:
    text = text.replace(df_old, df_new)
else:
    print("WARNING: Could not find df_old block")

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Patch 7 Applied")
