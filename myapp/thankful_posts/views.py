from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import ThankfulPost
from myapp.thankful_posts.forms import ThankfulPostForm

thankful_posts = Blueprint('thankful_posts', __name__)

@thankful_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = ThankfulPostForm()
    if form.validate_on_submit():
        thankful_post = ThankfulPost(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(thankful_post)
        db.session.commit()
        flash('Thankful Post Created')
        print('Thankful post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)


@thankful_posts.route('/<int:thankful_post_id>')
def thankful_post(thankful_post_id):
    thankful_post = ThankfulPost.query.get_or_404(thankful_post_id) 
    return render_template('thankful_post.html', title=thankful_post.title, date=thankful_post.date, post=thankful_post)

@thankful_posts.route('/<int:thankful_post_id>/update',methods=['GET','POST'])
@login_required
def update(thankful_post_id):
    thankful_post = ThankfulPost.query.get_or_404(thankful_post_id)

    if thankful_post.author != current_user:
        abort(403)

    form = ThankfulPostForm()

    if form.validate_on_submit():
        thankful_post.title = form.title.data
        thankful_post.text = form.text.data
        db.session.commit()
        flash('Thankful Post Updated')
        return redirect(url_for('thankful_posts.thankful_post',thankful_post_id=thankful_post.id))

    elif request.method == 'GET':
        form.title.data = thankful_post.title
        form.text.data = thankful_post.text

    return render_template('create_post.html',title='Updating',form=form)

@thankful_posts.route('/<int:thankful_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(thankful_post_id):

    thankful_post = ThankfulPost.query.get_or_404(thankful_post_id)
    if thankful_post.author != current_user:
        abort(403)

    db.session.delete(thankful_post)
    db.session.commit()
    flash('Thankful Post Deleted')
    return redirect(url_for('core.index'))