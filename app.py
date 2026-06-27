import streamlit as st
from agents.search_agent import SearchAgent

st.set_page_config(
    page_title="Market Intelligence",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ──────────────────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');  # noqa: E501
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&display=swap');  # noqa: E501

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background: #080D1A;
    color: #C8D6F0;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Hero banner ── */
.hero {
    background: linear-gradient(135deg, #0A1628 0%, #0D1F3C 60%, #091525 100%);
    border-bottom: 1px solid #1A2E50;
    padding: 56px 64px 48px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -120px; right: -120px;
    width: 420px; height: 420px;
    background: radial-gradient(
        circle, rgba(37,99,235,0.18) 0%, transparent 70%
    );
    pointer-events: none;
}
.hero-eyebrow {
    font-family: 'Inter', monospace;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #2563EB;
    margin-bottom: 14px;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(32px, 4vw, 52px);
    font-weight: 700;
    color: #EEF4FF;
    line-height: 1.1;
    margin-bottom: 12px;
    letter-spacing: -0.02em;
}
.hero-title span { color: #3B82F6; }
.hero-sub {
    font-size: 15px;
    color: #6B84A8;
    max-width: 520px;
    line-height: 1.6;
}

/* ── Search bar section ── */
.search-section {
    padding: 40px 64px 32px;
    background: #080D1A;
    border-bottom: 1px solid #111C30;
}
.search-label {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #4A6080;
    margin-bottom: 10px;
}

/* ── Override Streamlit input ── */
.stTextInput > div > div > input {
    background: #0D1829 !important;
    border: 1.5px solid #1D2F4A !important;
    border-radius: 10px !important;
    color: #E8F0FF !important;
    font-size: 16px !important;
    font-family: 'Inter', sans-serif !important;
    padding: 14px 18px !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stTextInput > div > div > input:focus {
    border-color: #2563EB !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.15) !important;
}
.stTextInput > div > div > input::placeholder {
    color: #2E4060 !important;
}
.stTextInput label { display: none !important; }

/* ── Button ── */
.stButton > button {
    background: linear-gradient(135deg, #1D4ED8, #2563EB) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    padding: 14px 32px !important;
    letter-spacing: 0.03em !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
    width: 100% !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #1E40AF, #1D4ED8) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(37,99,235,0.35) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Spinner ── */
.stSpinner > div { color: #3B82F6 !important; }

/* ── Success banner ── */
.stAlert {
    background: #0C1F12 !important;
    border: 1px solid #166534 !important;
    border-radius: 10px !important;
    color: #4ADE80 !important;
}

/* ── Results area ── */
.results-section {
    padding: 40px 64px;
}
.results-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 32px;
}
.results-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #EEF4FF;
}
.results-count {
    background: #1A2D50;
    color: #3B82F6;
    font-size: 12px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 20px;
    letter-spacing: 0.05em;
}

/* ── Result card ── */
.result-card {
    background: #0D1829;
    border: 1px solid #162038;
    border-radius: 14px;
    padding: 28px 30px;
    margin-bottom: 18px;
    transition: all 0.25s ease;
    position: relative;
    overflow: hidden;
}
.result-card::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: linear-gradient(180deg, #2563EB, #06B6D4);
    border-radius: 3px 0 0 3px;
}
.result-card:hover {
    border-color: #1E3A6E;
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.4);
}
.card-index {
    font-family: 'Inter', monospace;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.14em;
    color: #2563EB;
    text-transform: uppercase;
    margin-bottom: 10px;
}
.card-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 18px;
    font-weight: 600;
    color: #D6E4FF;
    margin-bottom: 12px;
    line-height: 1.35;
}
.card-content {
    font-size: 14px;
    color: #7A92B4;
    line-height: 1.75;
    margin-bottom: 18px;
}
.card-url {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: #0A1525;
    border: 1px solid #1A2D4A;
    border-radius: 6px;
    padding: 6px 12px;
    font-size: 12px;
    font-family: 'Inter', monospace;
    color: #4A7CBF;
    text-decoration: none;
    word-break: break-all;
    transition: all 0.15s;
}
.card-url:hover {
    background: #0F1E38;
    color: #6BA3E8;
    border-color: #2563EB;
}

/* ── Empty state ── */
.empty-state {
    text-align: center;
    padding: 80px 40px;
    color: #2E4060;
}
.empty-icon { font-size: 48px; margin-bottom: 16px; }
.empty-text {
    font-size: 15px;
    color: #3A5070;
    line-height: 1.6;
}

/* ── Divider override ── */
hr { border-color: #111C30 !important; margin: 0 !important; }

/* ── Responsive ── */
@media (max-width: 768px) {
    .hero, .search-section, .results-section {
        padding-left: 24px;
        padding-right: 24px;
    }
    .hero-title { font-size: 28px; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ── Hero ────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="hero">
    <div class="hero-eyebrow">
        📡 &nbsp; AI-Powered Intelligence Platform
    </div>
    <div class="hero-title">Market Research,<br><span>Automated.</span></div>
    <div class="hero-sub">
        Enter any company name to get deep competitive insights, news signals,
        and market context — powered by AI search agents.
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ── Search ──────────────────────────────────────────────────────────────
st.markdown(
    '<div class="search-section"><div class="search-label">Company</div>',
    unsafe_allow_html=True,
)

col1, col2 = st.columns([5, 1])
with col1:
    company = st.text_input(
        "company_input",
        placeholder="e.g. OpenAI, Tesla, Stripe…",
        label_visibility="collapsed",
    )
with col2:
    search_clicked = st.button("🔍  Analyze", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── Results ─────────────────────────────────────────────────────────────
if search_clicked:
    if not company.strip():
        st.warning("Please enter a company name to begin your research.")
    else:
        search_agent = SearchAgent()

        msg = f"Scanning intelligence sources for **{company}**…"
        with st.spinner(msg):
            result = search_agent.search_company(company)

        items = result.get("results", [])

        st.markdown(
            f"""
        <div class="results-section">
            <div class="results-header">
                <div class="results-title">Research Results</div>
                <div class="results-count">{len(items)} sources</div>
            </div>
        """,
            unsafe_allow_html=True,
        )

        if items:
            for i, item in enumerate(items, 1):
                title = item.get("title", "Untitled")
                content = item.get("content", "No content available.")
                url = item.get("url", "")

                url_html = (
                    f'<a class="card-url" href="{url}"'
                    f' target="_blank">🔗 &nbsp;{url}</a>'
                    if url
                    else ""
                )

                st.markdown(
                    f"""
                <div class="result-card">
                    <div class="card-index">Source {i:02d}</div>
                    <div class="card-title">{title}</div>
                    <div class="card-content">{content}</div>
                    {url_html}
                </div>
                """,
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                """
            <div class="empty-state">
                <div class="empty-icon">🔎</div>
                <div class="empty-text">
                    No results found for this company.<br>
                    Try a different name or check your spelling.
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)

else:
    # idle state
    st.markdown(
        """
    <div class="results-section">
        <div class="empty-state">
            <div class="empty-icon">📊</div>
            <div class="empty-text">
                Enter a company name above and click
                <strong style="color:#3B82F6">Analyze</strong>
                to generate your market intelligence report.
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )
