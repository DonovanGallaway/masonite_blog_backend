"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Blog.create({"title":"Litany Against Fear", "body":"I must not fear. Fear is the mind-killer"})
        Blog.create({"title":"Laughing Man", "body":"What I thought I'd do is I'd pretend I was one of those deaf-mutes"})
        Blog.create({"title":"Firefly", "body":"If this is showing, your seed route was gorram shiny"})