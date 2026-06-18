import streamlit as st
import json
from datetime import datetime
from pathlib import Path


DATA_FILE = Path("reflections.json")


def load_reflections():
    """
    Load previous reflections from the JSON file.
    If the file does not exist or is empty, return an empty list.
    """
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_reflection(reflection):
    """
    Save a new reflection into the JSON file.
    """
    reflections = load_reflections()
    reflections.append(reflection)

    with open(DATA_FILE, "w") as file:
        json.dump(reflections, file, indent=4)


def main():
    st.set_page_config(
        page_title="Rest & Reflect",
        page_icon="🌙",
        layout="centered"
    )

    st.title("Rest & Reflect")
    st.write("A nightly gratitude check-in before sleep.")

    st.divider()

    st.subheader("Tonight's Check-In")

    blessing = st.text_input(
        "One blessing from today:",
        placeholder="Example: I had food, safety, or a moment of peace"
    )

    person = st.text_input(
        "One person I appreciate:",
        placeholder="Example: my mother, friend, teacher, coworker"
    )

    improvement = st.text_area(
        "One thing I want to improve tomorrow:",
        placeholder="Example: be more patient, lower my voice, focus better"
    )

    mood = st.slider(
        "How was your emotional state today?",
        min_value=1,
        max_value=10,
        value=5
    )

    if st.button("Save Reflection"):
        if not blessing or not person or not improvement:
            st.warning("Please complete all fields before saving.")
        else:
            reflection = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "blessing": blessing,
                "person_appreciated": person,
                "tomorrow_improvement": improvement,
                "mood": mood
            }

            save_reflection(reflection)

            st.success("Reflection saved.")

            st.subheader("Tonight's Reflection")
            st.write(f"**Blessing:** {blessing}")
            st.write(f"**Person Appreciated:** {person}")
            st.write(f"**Tomorrow's Improvement:** {improvement}")
            st.write(f"**Mood Score:** {mood}/10")

    st.divider()

    st.subheader("Reflection History")

    reflections = load_reflections()

    if not reflections:
        st.info("No reflections saved yet.")
    else:
        for reflection in reversed(reflections):
            with st.expander(f"Reflection from {reflection['date']}"):
                st.write(f"**Blessing:** {reflection['blessing']}")
                st.write(f"**Person Appreciated:** {reflection['person_appreciated']}")
                st.write(f"**Tomorrow's Improvement:** {reflection['tomorrow_improvement']}")
                st.write(f"**Mood Score:** {reflection['mood']}/10")


if __name__ == "__main__":
    main()
