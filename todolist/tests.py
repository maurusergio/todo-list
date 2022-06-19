import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Title

class TitleModelTests(TestCase):

    def test_was_published_recently_with_future_title(self):
        """
        was_published_recently() returns False for titles whose pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_title = Title(pub_date=time)
        self.assertIs(future_title.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_title(self):
        """
        was_published_recently() returns True for question whose pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_title = Title(pub_date=time)
        self.assertIs(recent_title.was_published_recently(), True)
    
    def create_title(title_text, days):
        """
        Create a title with the given 'title_text' and published the give number of 'days' offset to 
        now (negative for questions published in the past, positive for questions that have yet to be
        published).
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Title.objects.create(title_text=title_text, pub_date=time)
    
    class TitleIndexViewTexts(TestCase):
        def test_no_titles(self):
            """
            if no title exist, an apropriate message is displayed,
            """
            response = self.client.get(reverse('todolist:index'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "No titles are available.")
            self.assertQueryEqual(response.context['latest_title_list'], [])
        
        def test_past_title(self):
            """
            Titles with a pub_date in the past are displayed on the index page.
            """
            title =  create_title(title_text="Past title.", days=-30)
            response = self.client.get(reverse('todolist:index'))
            self.assertQuerysetEqual(
                response.context['latest_title_list'],
                [title],
            )
        def test_future_title(self):
            """
            Titles with a pub_date in the future aren't displayed on the index
            """
            create_title(title_text="Future question.", days=30)
            response = self.client.get(reverse('todolist:index'))
            self.assertContains(response, "No titles are available.")
            self.assertQuerysetEqual(response.context['latest_title_list'], [])
        
        def test_future_title_and_past_title(self):
            """Even if both past future titles exist, only past titles are displayed."""
            title = create_title(title_text="Past fitle.", days=-30)
            create_title(title_text="Future titile.", days=30)
            self.assertQuerysetEqual(
                response.context['latest_fitle_list'],
                [title],
            )
        def test_two_past_titles(self):
            """ The fitles index page may display multiple titles"""
            question1 = create_title(title_text="Past title 1.", days=-30)
            question2 = create_title(title_text="Past title 2.", days= -5)
            response = self.client.get(reverse('todolist:index'))
            self.assertQuerysetEqual(
                response.context['latest_title_list'],
                [title2,title1],
            )