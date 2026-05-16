import streamlit as st
import altair as alt
import pandas as pd

st.set_page_config(page_title="Workplace Systems Analysis", layout="wide")

# -------------------------
# SIDEBAR NAVIGATION
# -------------------------
page = st.sidebar.radio(
    "Navigate Sections",
    [
        "Home",
        "Data Integrity Issues",
        "Communication Double Standard",
        "Time Off Task Conflict",
        "Management vs Associate Behavior",
        "Operational Feedback Discouraged"
    ]
)

# -------------------------
# HOME PAGE
# -------------------------
if page == "Home":
    st.title("Workplace Systems & Reporting Analysis Dashboard")

    st.write("""
This application organizes observed workplace system behaviors into structured conceptual sections.

Each section represents a different aspect of operational reporting, communication behavior, and feedback handling.
    """)

    st.info("Use the sidebar to navigate between sections.")

# -------------------------
# DATA INTEGRITY ISSUES
# -------------------------
elif page == "Data Integrity Issues":
    st.title("Data Integrity Issues")

    st.write("""
This section describes concerns regarding streaming task data producing inaccurate or false-positive reporting outcomes.
    """)

    data = pd.DataFrame({
        "Issue": ["False Positives", "Incorrect Streaming", "Known Reporting Bugs"],
        "Frequency": [8, 6, 7]
    })

    chart = alt.Chart(data).mark_bar().encode(
        x="Issue",
        y="Frequency"
    )

    st.altair_chart(chart, use_container_width=True)

    st.markdown("""
**Summary:**
- Reporting systems may generate unreliable task signals
- Operational performance can be impacted by inaccurate data streams
    """)

# -------------------------
# COMMUNICATION DOUBLE STANDARD
# -------------------------
elif page == "Communication Double Standard":
    st.title("Communication Double Standard")

    st.write("""
Associates may be flagged for discussing operational issues as 'time off task',
while similar discussions at management level are not consistently treated the same way.
    """)

    st.markdown("""
**Key Pattern:**
- Associate discussion → flagged
- Management discussion → not consistently flagged
    """)

# -------------------------
# TIME OFF TASK CONFLICT
# -------------------------
elif page == "Time Off Task Conflict":
    st.title("Time Off Task Definition Conflict")

    st.write("""
A conflict exists between:
- discussing broken reporting systems (operational necessity)
- classification of that discussion as non-productive time
    """)

    df = pd.DataFrame({
        "Category": ["Operational Necessity", "Policy Classification"],
        "Impact": [7, 7]
    })

    chart = alt.Chart(df).mark_line(point=True).encode(
        x="Category",
        y="Impact"
    )

    st.altair_chart(chart, use_container_width=True)

# -------------------------
# MANAGEMENT VS ASSOCIATE BEHAVIOR
# -------------------------
elif page == "Management vs Associate Behavior":
    st.title("Management vs Associate Behavior Consistency")

    st.write("""
Observed differences in how time and communication are treated across roles.
    """)

    st.markdown("""
**Observed Categories:**
- Operational execution
- Strategy discussion
- Informal conversation during shift
    """)

    df = pd.DataFrame({
        "Group": ["Associates", "Management"],
        "Non-Task Discussion Time": [2, 8]
    })

    chart = alt.Chart(df).mark_bar().encode(
        x="Group",
        y="Non-Task Discussion Time"
    )

    st.altair_chart(chart, use_container_width=True)

# -------------------------
# OPERATIONAL FEEDBACK DISCOURAGED
# -------------------------
elif page == "Operational Feedback Discouraged":
    st.title("Operational Feedback Discouraged")

    st.write("""
Associates may experience discouragement when raising concerns about system accuracy or workflow inefficiencies.
    """)

    st.markdown("""
**Feedback Topics Often Affected:**
- Data inaccuracies
- False positives
- Workflow inefficiencies
- Reporting system issues
    """)

    df = pd.DataFrame({
        "Feedback Type": ["Bug Reports", "Process Issues", "Metric Concerns"],
        "Acceptance Level": [3, 4, 2]
    })

    chart = alt.Chart(df).mark_bar().encode(
        x="Feedback Type",
        y="Acceptance Level"
    )

    st.altair_chart(chart, use_container_width=True)
