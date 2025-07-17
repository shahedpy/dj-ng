from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from backend.todo.models.models import Todo
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Create sample todos for testing'

    def handle(self, *args, **options):
        # Create a test user if it doesn't exist
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={'password': 'testpass123'}
        )
        
        if created:
            user.set_password('testpass123')
            user.save()
            self.stdout.write(self.style.SUCCESS('Created test user: testuser'))
        
        # Create sample todos
        sample_todos = [
            {
                'title': 'Complete Django Tutorial',
                'description': 'Finish the Django REST API tutorial',
                'priority': 'high',
                'due_date': datetime.now() + timedelta(days=3)
            },
            {
                'title': 'Buy groceries',
                'description': 'Milk, eggs, bread, and fruits',
                'priority': 'medium',
                'due_date': datetime.now() + timedelta(days=1)
            },
            {
                'title': 'Exercise',
                'description': 'Go for a 30-minute run',
                'priority': 'low',
                'due_date': datetime.now() + timedelta(hours=2)
            },
            {
                'title': 'Read a book',
                'description': 'Continue reading "Clean Code"',
                'priority': 'low',
                'completed': True
            },
            {
                'title': 'Team meeting',
                'description': 'Weekly standup with the development team',
                'priority': 'high',
                'due_date': datetime.now() + timedelta(days=2)
            }
        ]
        
        for todo_data in sample_todos:
            todo, created = Todo.objects.get_or_create(
                user=user,
                title=todo_data['title'],
                defaults=todo_data
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created todo: {todo.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Todo already exists: {todo.title}')
                )
        
        self.stdout.write(
            self.style.SUCCESS('Sample data creation completed!')
        )
