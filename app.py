import streamlit as st

st.set_page_config(layout="wide")

st.title("Political Promise Tracker")
st.write("Track, update, and evaluate the promises made by politicians.")
government = {
    "name": "Fianna Fáil & Fine Gael Coalition",
    "leader": "Leo Varadkar (Fine Gael) & Micheál Martin (Fianna Fáil)",
    "wing": "Centre-Right",
    "wing_strength": 65,  
    "topics": ["Housing", "Healthcare", "Economy", "Climate Action"]
}

opposition = [
    {
        "name": "Sinn Féin",
        "leader": "Mary Lou McDonald",
        "wing": "Left",
        "wing_strength": 20,
        "topics": ["Housing", "Healthcare", "United Ireland"]
    },
    {
        "name": "Green Party",
        "leader": "Eamon Ryan",
        "wing": "Centre-Left",
        "wing_strength": 40,
        "topics": ["Climate Action", "Transport", "Biodiversity"]
    },
    {
        "name": "Labour Party",
        "leader": "Ivana Bacik",
        "wing": "Centre-Left",
        "wing_strength": 35,
        "topics": ["Workers' Rights", "Social Protection", "Education"]
    }
]

left_col, right_col = st.columns([2, 1])
with left_col:

    st.header("Current Government")
    st.subheader(government["name"])
    st.write(f"Leader: {government['leader']}")
    st.write(f"Ideology: {government['wing']} wing")
    st.progress(government["wing_strength"] / 100)
    st.markdown("**Policy Focus Areas:**")
    for topic in government["topics"]:
        st.write(f"- {topic}")

with right_col:
    st.header("Other Parties")
    for party in opposition:
        st.subheader(party["name"])
        st.write(f"Leader: {party['leader']}")
        st.write(f"Ideology: {party['wing']} wing")
        st.progress(party["wing_strength"] / 100)
        st.markdown("**Focus Topics:**")
        for topic in party["topics"]:
            st.write(f"- {topic}")
        st.markdown("---")
