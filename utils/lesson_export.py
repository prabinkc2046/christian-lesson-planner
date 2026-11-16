from io import BytesIO
import subprocess


def export_complete_lesson(lesson_text, suggestions_html):
    html = f"""
    <h1>Original Lesson Plan</h1>
    <pre>{lesson_text}</pre>

    <h1>Christian Worldview Integration Suggestions</h1>
    {suggestions_html}
    """

    result = subprocess.run(
        ["pandoc", "-f", "html", "-t", "docx", "-o", "-"],
        input=html.encode("utf-8"),
        capture_output=True,
        check=True,
    )

    return BytesIO(result.stdout)
