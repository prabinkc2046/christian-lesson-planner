import streamlit as st
from utils.document_reader import extract_text
from utils.ai_analysis import generate_worldview_suggestions
from utils.document_export import export_suggestions_to_word
from utils.html_cleaner import clean_html
from utils.lesson_export import export_complete_lesson
from streamlit_quill import st_quill
import hashlib

st.set_page_config(
    page_title="Integrate Biblical Truth in Your Lesson Plan",
    page_icon="📖",
    layout="wide",
)

st.title("Integrate Biblical Truth in Your Lesson Plan", anchor=False)
st.caption(
    "Upload your lesson plan and receive practical suggestions to help you "
    "integrate a Christian worldview naturally and meaningfully."
)

uploaded_file = st.file_uploader(
    "Upload Lesson Plan",
    type=["pdf", "docx", "txt"],
    help="Upload an existing lesson plan in PDF, Word, or text format.",
)

if uploaded_file is not None:
    file_id = hashlib.sha256(uploaded_file.getvalue()).hexdigest()

    if st.session_state.get("current_file_id") != file_id:
        st.session_state["current_file_id"] = file_id
        st.session_state.pop("suggestions", None)

    st.success(f"Lesson plan uploaded: {uploaded_file.name}", icon="✅")

    lesson_text = extract_text(uploaded_file)

    st.subheader("Lesson Plan Preview", anchor=False)
    st.caption(
        "Review the lesson content before generating Christian worldview suggestions."
    )

    st.text_area(
        "Lesson Content",
        value=lesson_text,
        height=400,
    )

    if st.button(
        "Generate Christian Worldview Suggestions",
        type="primary",
        icon=":material/auto_awesome:",
    ):
        with st.spinner("Preparing Christian worldview suggestions..."):
            suggestions = generate_worldview_suggestions(lesson_text)
            st.session_state["suggestions"] = suggestions

if "suggestions" in st.session_state:
    st.subheader("Christian Worldview Suggestions", anchor=False)
    st.caption(
        "Review and refine these suggestions so they best suit your lesson, "
        "students, and teaching context."
    )

    left, right = st.columns(2, gap="medium")

    with left:
        with st.container(border=True, height=600):
            st.subheader("Edit Suggestions", anchor=False)
            st.caption(
                "Adjust the suggestions to align with your teaching style and lesson goals."
            )

            edited = st_quill(
                value=clean_html(st.session_state["suggestions"]),
                html=True,
                key="suggestions_editor",
            )

            if edited is not None:
                st.session_state["suggestions"] = edited

    with right:
        with st.container(border=True, height=600):
            st.subheader("Preview", anchor=False)
            st.caption("View how the reviewed suggestions will appear.")

            if edited is not None:
                st.html(edited)

if "suggestions" in st.session_state:
    word_file = export_suggestions_to_word(st.session_state["suggestions"])

    st.download_button(
        label="Download Suggestions as Word Document",
        data=word_file,
        file_name="christian_worldview_suggestions.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        icon=":material/download:",
        type="primary",
    )
