from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    pattern = ""
    pattern_option = ""
    highlighted_text = ""
    error_message = None
    
    default_text = """Here are some sample texts that match the pattern options: 
example@unair.ac.id, user@example.com, john.doe@example.org, arkan.syafiq.attaqy-2022@ftmm.unair.ac.id, 6400000910990001, user_name, Python3_9, Password@2021, Secr3t!Key, document.pdf, file.txt, photo.jpg, report.docx, thesis.doc, 164221062, 165309876, 162123456, 166456789, Jakarta, Surabaya, Bandung, jakarta, surabaya, bandung, +6281234567890, +447911123456, 0212345678, https://example.com, 12345-6789, 4111111111111111, 2023-09-07, 192.168.0.1, 14:30, 12345678901


You can create your own sentences to test the patterns as well!"""
    
    text = default_text
    
    if request.method == "POST":
        pattern_option = request.form.get("pattern_option", "")
        pattern = request.form.get("pattern", "")
        text = request.form.get("text", default_text)

        if pattern_option:
            pattern = pattern_option

        if pattern and text:
            try:
                # Mark matches before replacing them
                matches = re.finditer(pattern, text)
                highlighted_text = text

                for match in matches:
                    highlighted_text = highlighted_text.replace(match.group(0), f'[[[{match.group(0)}]]]')

                # Now, replace the marked matches with actual highlighted text
                highlighted_text = highlighted_text.replace('[[[', '<span class="highlight">').replace(']]]', '</span>')

            except re.error as e:
                error_message = f"Oops... Sorry, Incorrect input"

    return render_template('index.html', pattern=pattern, text=text, highlighted_text=highlighted_text, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
