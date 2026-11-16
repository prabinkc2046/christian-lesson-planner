from io import BytesIO
import subprocess


def export_suggestions_to_word(suggestions):
    result = subprocess.run(
        ["pandoc", "-f", "html", "-t", "docx", "-o", "-"],
        input=suggestions.encode("utf-8"),
        capture_output=True,
        check=True,
    )

    return BytesIO(result.stdout)
