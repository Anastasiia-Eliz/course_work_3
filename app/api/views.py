from flask import Blueprint, jsonify
from utils import get_posts_all, get_post_by_pk
import logging
from config import PATH
api_blueprint = Blueprint("api_blueprint", __name__)

logger = logging.getLogger("basic")

@api_blueprint.route("/api/posts/")
def all_posts():
	logger.debug("Запрошены все посты через API")
	posts = get_posts_all(PATH)
	return jsonify(posts)


@api_blueprint.route("/api/posts/<int:post_pk>/")
def posts_by_id(post_pk):
	logger.debug(f"Запрошен пост с pk {post_pk} через API")
	posts = get_posts_all(PATH)
	post = get_post_by_pk(posts, post_pk)
	return jsonify(post)
