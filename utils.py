import json

def get_posts_all(path):
	with open(path, 'r', encoding="UTF-8") as file:
		posts = json.load(file)
		return posts

def get_post_by_pk(posts,pk):
	"""возвращает один пост по его идентификатору"""
	for post in posts:
		if post["pk"] == pk:
			return post


def get_posts_by_user(posts, user_name):
	"""возвращает посты определенного пользователя"""
	posts_founded = []
	for post in posts:
		if user_name.lower() in post["poster_name"].lower():
			posts_founded.append(post)
	return posts_founded



def get_comments_by_post_id(comments, post_id):
	"""возвращает комментарии определенного поста"""
	comment_by_posts = []
	for comment in comments:
		if post_id == comment["post_id"]:
			comment_by_posts.append(comment)
	return comment_by_posts



def search_for_posts(posts,query):
	"""возвращает список постов по ключевому слову"""
	posts_founded = []
	for post in posts:
		if query.lower() in post["content"].lower():
			posts_founded.append(post)
	return posts_founded





