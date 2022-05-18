from flask import Blueprint, render_template, request, abort
from utils import get_posts_all, get_post_by_pk, get_posts_by_user, get_comments_by_post_id, search_for_posts
from config import PATH, LINK
posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")


@posts_blueprint.route("/")
def all_posts():
	try:
		posts = get_posts_all(PATH)
		return render_template("index.html", posts=posts)
	except:
		return "Что то пошло не так"


@posts_blueprint.route("/posts/<int:post_pk>/")
def posts_by_id(post_pk):
		posts = get_posts_all(PATH)
		post = get_post_by_pk(posts,post_pk)
		all_comments = get_posts_all(LINK)
		comments = get_comments_by_post_id(all_comments, post_pk)

		if post is None:
			abort(404)

		number_of_comment = len(comments)
		return render_template("post.html", post=post, comments=comments, number_of_comment=number_of_comment)

@posts_blueprint.errorhandler(404)
def post_error(e):
	return "Такой пост не найден"

@posts_blueprint.route("/users/<user_name>/")
def posts_by_name(user_name):
	try:
		all_posts = get_posts_all(PATH)
		posts = get_posts_by_user(all_posts, user_name)
		return render_template("user-feed.html", posts=posts)
	except:
		"Произошла ошибка"


@posts_blueprint.route("/search/")
def search_posts():
	s = request.args.get("s", "")
	try:
		posts = get_posts_all(PATH)
		filtered_posts = search_for_posts(posts, s)
		posts_count = len(filtered_posts)
		return render_template("search.html", s=s, posts=filtered_posts, posts_count=posts_count)
	except:
		"Что то пошло не так"




