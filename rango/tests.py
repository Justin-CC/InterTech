from django.test import TestCase, Client
from rango.models import Dish, User, Comment, Receive
from decimal import Decimal
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.db.utils import DataError
from django.urls import reverse
from django.template.defaultfilters import truncatechars
from rango.views import register
# Create your tests here.


# The folloiwng code test models.

# Test Dish model.
class DishModelTest(TestCase):
    def setUp(self):
        self.dish = Dish.objects.create(
            dishname='Test Dish',
            type='Starter',
            price=Decimal('10.99'),
            description='A delicious test dish',
        )

    def test_create_dish(self):
        self.assertIsInstance(self.dish, Dish)
        self.assertEqual(self.dish.dishname, 'Test Dish')
        self.assertEqual(self.dish.type, 'Starter')
        self.assertEqual(self.dish.price, Decimal('10.99'))
        self.assertEqual(self.dish.description, 'A delicious test dish')

    def test_save_method(self): #test slug and picture
        self.assertEqual(self.dish.slug, slugify(self.dish.dishname))
        self.assertEqual(self.dish.picture, '/static/images/' + slugify(self.dish.dishname).upper() + '.jpg')

    def test_str_method(self):
        self.assertEqual(str(self.dish), self.dish.dishname)

    def test_dishname_uniqueness(self): # test uniqueness
        with self.assertRaises(ValidationError):
            Dish.objects.create(
                dishname='Test Dish', # The same dishname as in the setUp method
                type='Main Course',
                price=Decimal('15.99'),
                description='A conflicting test dish',
            )

    def test_dishname_max_length(self):
        long_name = 'A' * 51  # Exceeds the max_length of 50
        with self.assertRaises(DataError):
            Dish.objects.create(
                dishname=long_name,
                type='Starter',
                price=Decimal('10.99'),
                description='A test dish with a long name',
            )

    def test_type_max_length(self):
        long_type = 'A' * 31  # Exceeds the max_length of 30
        with self.assertRaises(DataError):
            Dish.objects.create(
                dishname='Long Type Dish',
                type=long_type,
                price=Decimal('10.99'),
                description='A test dish with a long type',
            )

    def test_description_max_length(self):
        long_description = 'A' * 501  # Exceeds the max_length of 500
        with self.assertRaises(DataError):
            Dish.objects.create(
                dishname='Long Description Dish',
                type='Starter',
                price=Decimal('10.99'),
                description=long_description,
            )

    def test_price_positive(self):
        negative_price = Decimal('-1.00')  # must be positive
        with self.assertRaises(ValidationError):
            dish = Dish(
                dishname='Negative Price Dish',
                type='Starter',
                price=negative_price,
                description='A test dish with a negative price',
            )
            dish.full_clean()

# Test User
class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            password='testpassword',
            phone=1234567890,
            email='testuser@example.com',
        )

    def test_create_user(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.password, 'testpassword')
        self.assertEqual(self.user.phone, 1234567890)
        self.assertEqual(self.user.email, 'testuser@example.com')

    def test_str_method(self):
        self.assertEqual(str(self.user), self.user.username)

    def test_username_uniqueness(self):
        with self.assertRaises(ValidationError):
            User.objects.create(
                username='testuser', # The same username as in the setUp method
                password='anotherpassword',
                phone=9876543210,
                email='anotheruser@example.com',
            )

# Test Comment
class CommentModelTest(TestCase):
    def setUp(self):
        self.dish = Dish.objects.create(
            dishname='Test Dish',
            type='Starter',
            price=10.99,
            description='A delicious test dish',
        )

        self.user = User.objects.create(
            username='testuser',
            password='testpassword',
            phone=1234567890,
            email='testuser@example.com',
        )

        self.comment = Comment.objects.create(
            dish=self.dish,
            user=self.user,
            content='A test comment for the dish',
        )

    def test_create_comment(self):
        self.assertIsInstance(self.comment, Comment)
        self.assertEqual(self.comment.dish, self.dish)
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.content, 'A test comment for the dish')

    def test_content_max_length(self):
        long_content = 'A' * 501  # Exceeds the max_length of 500
        with self.assertRaises(DataError):
            Comment.objects.create(
                dish=self.dish,
                user=self.user,
                content=long_content,
            )

# Test Receive
class ReceiveModelTest(TestCase):
    def setUp(self):
        self.receive = Receive.objects.create(
            name='John Doe',
            title='Test Title',
            content='A test content for the Receive model',
            email='johndoe@example.com',
        )

    def test_create_receive(self):
        self.assertIsInstance(self.receive, Receive)
        self.assertEqual(self.receive.name, 'John Doe')
        self.assertEqual(self.receive.title, 'Test Title')
        self.assertEqual(self.receive.content, 'A test content for the Receive model')
        self.assertEqual(self.receive.email, 'johndoe@example.com')

    def test_str_method(self):
        self.assertEqual(str(self.receive), truncatechars(self.receive.content, 30))

    def test_name_max_length(self):
        long_name = 'A' * 41  # Exceeds the max_length of 40
        with self.assertRaises(DataError):
            Receive.objects.create(
                name=long_name,
                title='Test Title',
                content='A test content',
                email='test@example.com',
            )

    def test_title_max_length(self):
        long_title = 'A' * 21  # Exceeds the max_length of 20
        with self.assertRaises(DataError):
            Receive.objects.create(
                name='Jane Doe',
                title=long_title,
                content='A test content',
                email='janedoe@example.com',
            )

    def test_content_max_length(self):
        long_content = 'A' * 501  # Exceeds the max_length of 500
        with self.assertRaises(DataError):
            Receive.objects.create(
                name='Jane Doe',
                title='Test Title',
                content=long_content,
                email='janedoe@example.com',
            )

    def test_email_validity(self):
        invalid_email = 'invalid_email'
        with self.assertRaises(ValidationError):
            receive = Receive(
                name='Invalid Email User',
                title='Test Title',
                content='A test content',
                email=invalid_email,
            )
            receive.full_clean()

#The following method test views


#Test index view
class IndexViewTest(TestCase):
    def test_view_uses_correct_template(self):  # Tests if the view returns the correct template.
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_view_no_session_data(self):  # Tests the view when there's no session data.
        response = self.client.get(reverse('index'))
        self.assertIsNone(response.context['info_dict'])

    def test_view_with_session_data(self):  # Tests the view when there's session data.
        session = self.client.session
        session['info'] = {'key': 'value'}
        session.save()

        response = self.client.get(reverse('index'))
        self.assertIsNotNone(response.context['info_dict'])
        self.assertEqual(response.context['info_dict'], {'key': 'value'})


#Test login view
class LoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            password='testpassword',
            phone=1234567890,
            email='testuser@example.com',
        )

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_valid_login_post(self):
        response = self.client.post(reverse('login'), {'user': 'testuser', 'pwd': 'testpassword'})
        self.assertRedirects(response, reverse('index'))

    def test_invalid_login_post(self):
        response = self.client.post(reverse('login'), {'user': 'testuser', 'pwd': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], 'The user name or password is incorrect')

# test logout view
class LogoutViewTest(TestCase):
    def setUp(self):  # set up a user for test
        self.user = User.objects.create(
            username='testuser',
            password='testpassword',
            phone=1234567890,
            email='testuser@example.com',
        )

    def test_logout_view(self):
        # Log in a user by setting session data
        session = self.client.session
        session['info'] = {'id': self.user.userid, 'name': self.user.username}
        session.save()

        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('index'))

        self.assertNotIn('info', self.client.session)

# test register view
class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_data = {
            'register_username': 'testuser',
            'register_phone_number': '1234567890',
            'register_email': 'test@example.com',
            'register_password': 'testpassword',
            'register_confirm_password': 'testpassword'
        }

    def test_register_get_request(self):
        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_post_request(self):
        response = self.client.post(reverse('register'), data=self.user_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertEqual(User.objects.count(), 1)

    def test_register_post_request_password_mismatch(self):
        self.user_data['register_confirm_password'] = 'wrongpassword'
        response = self.client.post(reverse('register'), data=self.user_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertIn('error', response.context)

    def test_register_post_request_existing_user(self):
        User.objects.create(username='testuser', password='testpassword', phone='1234567890', email='test@example.com')

        response = self.client.post(reverse('register'), data=self.user_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertIn('error', response.context)


# test menu view
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        # Create sample dishes
        Dish.objects.create(dishid=1, dishname='Dish 1', type='Starter', price=10.0, picture='pic1', description='1 description')
        Dish.objects.create(dishid=2, dishname='Dish 2', type='Starter', price=15.0, picture='pic2', description='2 description')

    def test_menu_view(self):
        response = self.client.get(reverse('menu'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

        dishes = response.context['data']
        self.assertEqual(len(dishes), 2)
        self.assertEqual(dishes[0]['dishid'], 1)
        self.assertEqual(dishes[0]['dishname'], 'Dish 1')
        self.assertEqual(dishes[1]['dishid'], 2)
        self.assertEqual(dishes[1]['dishname'], 'Dish 2')

# test aboutus view
class AboutUsViewTestCase(TestCase):
    def test_aboutus_view(self):

        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus.html')


# test contactus view
class ContactUsViewTestCase(TestCase):
    def test_contactus_view_get_request(self):

        response = self.client.get(reverse('contactus'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contactus.html')

    def test_contactus_view_post_request_with_valid_data(self):
        response = self.client.post(reverse('contactus'), {
            'your_name': 'John Doe',
            'your_email': 'john@example.com',
            'your_title': 'Test Message',
            'your_content': 'This is a test message.',
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contactus.html')

        self.assertEqual(Receive.objects.count(), 1)
        message = Receive.objects.first()
        self.assertEqual(message.name, 'John Doe')
        self.assertEqual(message.email, 'john@example.com')
        self.assertEqual(message.title, 'Test Message')
        self.assertEqual(message.content, 'This is a test message.')

#test aboutus view
class FaqsViewTestCase(TestCase):
    def test_aboutus_view(self):

        response = self.client.get(reverse('faqs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs.html')