from run import app

class TestApi:

	def test_app_all_posts_status_code(self):
		"""проверка получения корректного списка"""
		response = app.test_client().get("/api/posts", follow_redirects=True)
		assert response.status_code == 200, "Статус  код запроса всех постов неверный"
		assert response.mimetype == "application/json", "Получен не json"



	def test_app_all_posts_type_count_content(self):
		"""проверка правильности полученных данных"""
		response = app.test_client().get("/api/posts", follow_redirects=True)
		assert type(response.json) == list, """получен не список"""
		assert len(response.json) == 8, """получено неверное количество постов"""



	def test_app_all_posts_type_check_keys(self):
		"""проверка полученных ключей"""

		keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

		response = app.test_client().get("/api/posts", follow_redirects=True)
		first_key = set(response.json[0].keys())
		assert keys == first_key, """полученные ключи не совпадают"""

	def test_app_one_post_type_count_content(self):
			"""проверка правильности полученных данных"""
			response = app.test_client().get("/api/posts/1", follow_redirects=True)
			assert type(response.json) == dict, """получен не словарь"""


	def test_app_one_post_type_check_keys(self):
			"""проверка полученных ключей"""

			keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

			response = app.test_client().get("/api/posts/1", follow_redirects=True)
			first_key = response.json.keys()
			assert keys == first_key, """полученные ключи не совпадают"""


