from django.test import TestCase, RequestFactory
from .models import Todo
from datetime import datetime
from .views import mark_as_completed, index
from django.contrib.auth.models import User


class TodoTestCase(TestCase):
    def setUp(self):
        self.todo_a = Todo.objects.create(task='First Todo', date=datetime.today())
        self.user = User.objects.create(username='johndoe', email='john@example.com', password='secret')
        self.factory = RequestFactory()

    def test_authenticated_user_can_mark_todo_as_complete(self):
        todo_id = self.todo_a.id
        self.assertIsNone(self.todo_a.completed_at)

        request = self.factory.get('/mark-completed/' + str(todo_id))
        response = mark_as_completed(request, todo_id)
        self.assertEqual(response.status_code, 302)

        updated_todo = Todo.objects.get(id=todo_id)
        self.assertIsNotNone(updated_todo.completed_at)

    def test_authorised_users_add_a_todo(self):
        post_date = {
            'task': 'Some task name',
            'date': '2019-06-13',
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }

        self.assertEqual(1, Todo.objects.count())

        request = self.factory.post('todos', post_date)
        response = index(request)

        self.assertEqual(2, Todo.objects.count())
