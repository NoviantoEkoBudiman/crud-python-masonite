from masonite.controllers import Controller
from masonite.views import View
from app.models.Post import Post
from masonite.request import Request
from masonite.response import Response

class BlogController(Controller):
    def show(self, view: View):
        return view.render("blog")

    def store(self, request: Request, response: Response):
        Post.create(
            title = request.input('title'),
            body = request.input('body'),
            author_id = request.user().id
        )
        return response.redirect("/blog")