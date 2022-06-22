from django.test import TestCase
from .models import NeighbourHood, Posts, Contacts, User, Business

# Create your tests here.
class NeighbourHoodTest(TestCase):
    '''
    test class for NeighbourHood model
    '''
    def setUp(self):
        '''
        test method to create Image instances called before all tests
        '''
        self.new_category = Business(name='testing')
        self.new_category.save_category()
        
        self.new_posts = User(city='Nairobi', country='Kenya')
        self.new_posts.save_posts()
        
        self.new_picture = NeighbourHood(image_link='NeighbourHood/picture.jpeg', title='Image title', description='sth random', category=self.new_category, posts=self.new_posts)
        self.new_picture.save_image()
        self.another_picture = NeighbourHood(image_link='NeighbourHood/photo.jpg', title='Another title', description='sth else more random', category=self.new_category, posts=self.new_posts)
        self.another_picture.save_image()

    def tearDown(self):
        '''
        test method to delete Image instances after each test is run
        '''
        Business.objects.all().delete()
        User.objects.all().delete()
        NeighbourHood.objects.all().delete()

    def test_instances(self):
        '''
        test method to assert instances created during setUp
        '''
        self.assertTrue(isinstance(self.new_picture,NeighbourHood))
        self.assertTrue(isinstance(self.new_category, Business))
        self.assertTrue(isinstance(self.new_posts, User))

    def test_save_image(self):
        '''
        test method to ensure an Image instance has been correctly saved
        '''
        self.assertTrue(len(NeighbourHood.objects.all()) == 2)

    def test_delete_image(self):
        '''
        test method to ensure an Image instance has been correctly deleted
        '''
        self.new_picture.delete_image()
        self.assertTrue(len(NeighbourHood.objects.all()) == 1)

    def test_update_image(self):
        '''
        test method to ensure an Image instance has been correctly updated
        '''
        update_test = self.new_picture.update_image('NeighbourHood/updated.png')
        self.assertEqual(update_test.image_link, 'NeighbourHood/updated.png')

    def test_get_all(self):
        '''
        test method to ensure all instances of Image class have been retrieved
        '''
        pictures = NeighbourHood.get_all()
        # print(pictures)

    def test_get_image_by_id(self):
        '''
        test method to ensure Image instances can be retrieved by id
        '''
        obtained_image = NeighbourHood.get_image_by_id(self.another_picture.id)
        # print(obtained_image.title)

    def test_search_image(self):
        '''
        test method to ensure correct searching of an multiple image instances by category
        '''
        obtained_image = NeighbourHood.search_image(self.new_picture.category)
        # print(obtained_image)

    def test_filter_by_posts(self):
        '''
        test method to obtain image insatnces by posts
        '''
        obtained_image = NeighbourHood.filter_by_posts(self.another_picture.posts)
        print(obtained_image)



class BusinessTest(TestCase):
    '''
    test class for Business model
    '''
    def setUp(self):
        '''
        test method to create Business instances called before all tests
        '''
        self.new_business = Business(name='businessA')
        self.new_business.save_business()

    def tearDown(self):
        '''
        test method to delete Business instances after each test is run
        '''
        Business.objects.all().delete()

    def test_save_business(self):
        '''
        test method to ensure a business instance has been correctly saved
        '''
        self.assertTrue(len(Business.objects.all()) == 1)     

    def test_delete_business(self):
        '''
        test method to ensure a business instance has been correctly deleted
        '''
        self.new_business.save_business()
        self.new_business.delete_business()
        self.assertTrue(len(Business.objects.all()) == 0)    

    def test_update_business(self):
        '''
        test method to ensure a business instance has been correctly updated
        '''
        update_cat = Business.update_business('businessA', 'differentCat')
        self.assertEqual(update_cat.name, 'differentCat')




class PostsTest(TestCase):
    '''
    test class for Posts model
    '''
    def setUp(self):
        '''
        test method to create Posts instances called before all tests
        '''
        self.new_Posts = Posts(city='lost city', country='unknown')
        self.new_Posts.save_Posts()

    def test_save_Posts(self):
        '''
        test method to ensure a Posts instance has been correctly saved
        '''
        self.assertTrue(len(Posts.objects.all()) == 1)     

    def test_delete_Posts(self):
        '''
        test method to ensure a Posts instance has been correctly deleted
        '''
        self.new_posts.save_posts()
        self.new_posts.delete_posts()
        self.assertTrue(len(Posts.objects.all()) == 0)

    def test_update_posts(self):
        '''
        test method to ensure a posts instance has been correctly updated
        '''
        update_locale = Posts.update_posts('unknown', 'paperTown')
        self.assertEqual(update_locale.city, 'paperTown')

    def test_get_all(self):
        '''
        test method to ensure all instances of Posts class have been retrieved
        '''
        Posts = Posts.get_all()
        print(Posts)

class UserTest(TestCase):
    '''
    test class for User model
    '''
    def setUp(self):
        '''
        test method to create User instances called before all tests
        '''
        self.new_User = User(city='lost city', country='unknown')
        self.new_User.save_User()

    def test_save_User(self):
        '''
        test method to ensure a User instance has been correctly saved
        '''
        self.assertTrue(len(User.objects.all()) == 1)     

    def test_delete_User(self):
        '''
        test method to ensure a User instance has been correctly deleted
        '''
        self.new_User.save_User()
        self.new_User.delete_User()
        self.assertTrue(len(User.objects.all()) == 0)

    def test_update_User(self):
        '''
        test method to ensure a User instance has been correctly updated
        '''
        update_locale = User.update_User('unknown', 'paperTown')
        self.assertEqual(update_locale.city, 'paperTown')

    def test_get_all(self):
        '''
        test method to ensure all instances of User class have been retrieved
        '''
        User = User.get_all()
        print(User)

class ContactsTest(TestCase):
    '''
    test class for Contacts model
    '''
    def setUp(self):
        '''
        test method to create Contacts instances called before all tests
        '''
        self.new_Contacts = Contacts(city='lost city', country='unknown')
        self.new_Contacts.save_Contacts()

    def test_save_Contacts(self):
        '''
        test method to ensure a Contacts instance has been correctly saved
        '''
        self.assertTrue(len(Contacts.objects.all()) == 1)     

    def test_delete_Contacts(self):
        '''
        test method to ensure a Contacts instance has been correctly deleted
        '''
        self.new_Contacts.save_Contacts()
        self.new_Contacts.delete_Contacts()
        self.assertTrue(len(Contacts.objects.all()) == 0)

    def test_update_Contacts(self):
        '''
        test method to ensure a Contacts instance has been correctly updated
        '''
        update_locale = Contacts.update_Contacts('unknown', 'paperTown')
        self.assertEqual(update_locale.city, 'paperTown')

    def test_get_all(self):
        '''
        test method to ensure all instances of Contacts class have been retrieved
        '''
        Contacts = Contacts.get_all()
        print(Contacts)