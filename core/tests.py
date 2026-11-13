from django.test import TestCase
from django.urls import reverse

class RouteTests(TestCase):
    def test_homepage_specialties_menu_link(self):
        response = self.client.get(reverse('home'))

        self.assertContains(
            response,
            f'href="{reverse("menu")}" class="btn-view-menu">View Menu &amp; Brews</a>',
        )
        self.assertContains(response, '<div class="specialties-text-group">')

    def test_all_routes_return_200(self):
        routes = [
            ('home', 'core/home.html'),
            ('menu', 'core/menu.html'),
            ('stay', 'core/stay.html'),
            ('heritage', 'core/heritage.html'),
            ('trail_guide', 'core/trail_guide.html'),
            ('gallery', 'core/gallery.html'),
            ('guestbook', 'core/guestbook.html'),
            ('contact', 'core/contact.html'),
            ('book_table', 'core/book_table.html'),
        ]
        for url_name, template_name in routes:
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template_name)
