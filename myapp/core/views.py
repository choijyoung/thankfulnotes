# core/views.py 
from flask import render_template, request, Blueprint
from myapp.models import ThankfulPost

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    thankful_posts = ThankfulPost.query.order_by(ThankfulPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', thankful_posts=thankful_posts)

@core.route('/info')
def info():
    return render_template('info.html')