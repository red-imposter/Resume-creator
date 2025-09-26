from flask import Flask
from src import resume_manipulator


app = Flask(__name__,static_url_path="",static_folder="public")

@app.route("/resume/generate", methods=["POST"])
def rgenerate_resume():
    resume_manipulator.generate_resume()
    return resume_manipulator.get_resume()


@app.route("/regenerate")
def regenerate_resume():
    resume_manipulator.generate_resume()
    return resume_manipulator.get_resume()

@app.route("/")
def get_resume():
    return resume_manipulator.get_resume()

if __name__ == '__main__':
    resume_manipulator.generate_resume()
    app.run(host='localhost', port=80, debug=True)



