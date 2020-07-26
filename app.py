from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from CodingTA.CodingTA import CodingTA
app = Flask(__name__)
coding_assistant = CodingTA()
description = """
Task: Sorting Tuples \n
Can we sort items other than integers?  \n
For this question, you will be sorting tuples! We represent a person using a tuple (gender, age). \n
Given a list of people, write a function sort_age that sorts the people and return a list in an order such that the older people are at the front of the list. An example of the list of people is [("M", 23), ("F", 19), ("M", 30)]. The sorted list would look like [("M", 30), ("M", 23), ("F", 19)]. You may assume that no two members in the list of people are of the same age.
"""

@app.route('/hello')
def hello():
    return "Hello World!"

def debug(buggy_code):
    return coding_assistant.repairCode(buggy_code)

def check_correctness(code):
    tr_dict = coding_assistant.tester.tv_code(code)
    return all(tr_dict.values())

@app.route('/tmp_func', methods=('GET', 'POST'), endpoint="tmp_func")
def tmp_func():
    return redirect(url_for('question_page'))

@app.route('/', methods=('GET', 'POST'), endpoint="question_page")
@app.route('/question_page', methods=('GET', 'POST'), endpoint="question_page")
def question_page():
    if request.method == 'POST':
        code = request.form['code']
        # print(code)
        if check_correctness(code):
            message = "Accepted"
            perf_map = {}
            perf_map["rep_code"] = "You Answer is correct"
            perf_map["ori_bug_code"] = code
        else:
            message = "Wrong Answer"
            perf_map = debug(code)
            print("#############################")
            print(perf_map)
        return render_template('new_page.html',
                               ori_bug_code=code.replace("\n", "<br/>").replace(" ", "&nbsp;"),
                               rep_code=perf_map["rep_code"].replace("\n", "<br/>").replace(" ", "&nbsp;"))

    return render_template('raw_page.html', description=description.replace("\n", "<br/>"))

if __name__ == '__main__':
    app.run(debug=True)




