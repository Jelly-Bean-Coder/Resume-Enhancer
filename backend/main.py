from flask import Flask
import views
from flask_cors import CORS
import markdown

app = Flask(__name__, template_folder="../frontend/templates")
app.config["SECRET_KEY"] = "nv589pbhiobgp785bui57bvu2b3viubuyviB67fwyV7GD79FB4VYVBIYOBVYB9G78bv4u8bBHJ^H657"
CORS(app)

app.register_blueprint(views.views_bp)

@app.template_filter('markdown')
def markdown_filter(text):
    extensions = [
        'fenced_code', 
        'tables', 
        'extra',           # Adds footnotes and abbr
        'toc',             # Generates [TOC]
    ]
    return markdown.markdown(text, extensions=extensions)

if __name__ == "__main__":
    app.run(debug=True)