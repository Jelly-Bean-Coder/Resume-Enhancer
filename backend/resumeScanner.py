from magika import Magika
import PyPDF2, docx
from io import BytesIO
import ollama

def extractText(byte):
    detector = Magika()
    detection_result = detector.identify_bytes(byte)
    extension = detection_result.output.label
    text = ""

    new_file = BytesIO(byte)

    if extension == "pdf":
        rdr = PyPDF2.PdfReader(new_file) 

        text = ""
        for page in rdr.pages:
            text = text + str(page.extract_text()) or ""
    elif extension == "docx":
        rdr = docx.Document(new_file)

        text = ""
        for i in rdr.paragraphs:
            text += i.text + "\n\n"

    elif extension == "txt":
        text = bytes.decode("utf-8", errors="replace")


    return text
    



def prompt(file, jobDesc):
    resume_extracted: str = extractText(byte=file)

    ai_instructions = f"""
    You are an expert resume reviewer.
    Analyze the resume against the job description. Answer politley and tell the user how to improve it.
    Provide:
    - ATS score (0–100)
    - Missing keywords
    - Strengths
    - Weaknesses
    - Bullet point improvements
    Resume:
    {resume_extracted}

    Job Description:
    {jobDesc}



        Please format your entire response in clean, readable Markdown using the following style:

    # Title (H1)

    ## Section Header (H2)

    - Bullet points
    - With spacing
    - And clarity

    ### Subsection (H3)

    1. Numbered steps
    2. With explanations

    **Bold text** for emphasis  
    *Italic text* when needed  

    Use code blocks like this:

    ```python
    print("example")
    ```

    Use horizontal rules:

    ---

    Use tables:

    | Column | Value |
    |--------|--------|
    | A      | B      |

    Return ONLY the formatted Markdown, nothing else.
    """

    response = ollama.generate(
        model="llama3.2",
        prompt=ai_instructions
    )

    return response["response"]
