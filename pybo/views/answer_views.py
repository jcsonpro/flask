from datetime import datetime

from flask import Blueprint, request, url_for
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/question')


@bp.route('/create/<int:question_id>', methods=('POST', ))
def create(question_id):
    question = Question.query.get(question_id)
    content = request.form['content']
    answer = Answer(content=content, create_date=datetime.now())
    question.answer_set.append(answer)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))