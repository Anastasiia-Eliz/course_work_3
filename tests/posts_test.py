import pytest
from utils import get_posts_all, get_post_by_pk, get_posts_by_user, search_for_posts, get_comments_by_post_id


@pytest.fixture
def all_posts():
	return get_posts_all("data/posts.json")


@pytest.fixture
def all_posts_by_comments():
	return get_posts_all("data/comments.json")


@pytest.fixture
def keys_expected():
	return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


@pytest.fixture
def keys_expected_by_comments():
	return {"post_id", "commenter_name", "comment", "pk"}


# Получение всех постов
def test_posts(all_posts):
	posts = all_posts
	assert type(posts) == list, "Список постов должен быть списком"
	assert type(posts[0]) == dict, "Каждый пост должен быть словарем"


def test_all_posts_has_keys(all_posts, keys_expected):
	posts = all_posts
	first_post = posts[0]
	first_post_keys = set(first_post.keys())
	assert first_post_keys == keys_expected, "Ключи неверны"


def test_get_post_by_pk(all_posts):
	posts = all_posts
	post = get_post_by_pk(posts, 1)
	assert type(post) == dict, "Должен быть словарем"


# Получение одного поста
def test_one_post_has_keys(all_posts, keys_expected):
	posts = all_posts
	post = get_post_by_pk(posts, 1)
	post_keys = set(post.keys())
	assert post_keys == keys_expected, "Ключи неверны"


parameters_by_pk = [1, 2, 3, 4, 5, 6, 7, 8, ]


@pytest.mark.parametrize("post_pk", parameters_by_pk)
def test_one_post_correct_keys(all_posts, post_pk):
	posts = all_posts
	post = get_post_by_pk(posts, post_pk)
	assert post["pk"] == post_pk, "Номер полученного поста не соответствует запрошенному "


# Получение поста по имени пользователя

parameters_by_user = [("leo", [1, 5]), ("larry", [4, 8]), ("hank", [3, 7])]


@pytest.mark.parametrize("poster_name, pk_correct", parameters_by_user)
def test_one_post_by_name(all_posts, poster_name, pk_correct):
	posts = all_posts
	post_users = get_posts_by_user(posts, poster_name)
	post_pk = []
	for post in post_users:
		post_pk.append(post["pk"])

	assert post_pk == pk_correct, "Полученный пост по пользователю не соответствует запрошенному "


# Поиск постов по слову

parameters_by_search = [("тарелка", [1]), ("елки", [3]), ("проснулся", [4])]


@pytest.mark.parametrize("query, pk_correct", parameters_by_search)
def test_one_post_by_search(all_posts, query, pk_correct):
	posts = all_posts
	post_users = search_for_posts(posts, query)
	post_pk = []
	for post in post_users:
		post_pk.append(post["pk"])

	assert post_pk == pk_correct, "Полученный пост  не соответствует запрошенному "


# Поиск по комментариям

def test_posts_comments(all_posts_by_comments):
	posts = all_posts_by_comments
	assert type(posts) == list, "Список постов должен быть списком"
	assert type(posts[0]) == dict, "Каждый пост должен быть словарем"


def test_all_posts_has_keys(all_posts_by_comments, keys_expected_by_comments):
	posts = all_posts_by_comments
	first_post = posts[0]
	first_post_keys = set(first_post.keys())
	assert first_post_keys == keys_expected_by_comments, "Ключи неверны"


parameters_by_comment = [
	(1, {1, 2, 3, 4}),
	(2, {5, 6, 7, 8}),
	(3, {9, 10, 11, 12}),
	(4, {13, 14, 15, 16}),
	(5, {17, 18}),
	(6, {19}),
	(7, {20})

]

@pytest.mark.parametrize("post_id, correct_comments", parameters_by_comment)
def test_one_post_correct_comments(all_posts_by_comments, post_id, correct_comments):
	all_comments = all_posts_by_comments
	comments = get_comments_by_post_id(all_comments, post_id)
	comment_pk = set([comment["pk"] for comment in comments])
	assert comment_pk == correct_comments, "Полученные комментарии определенного поста не соответствуют запрошенным "
