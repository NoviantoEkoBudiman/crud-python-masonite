from masonite.controllers import Controller
from masonite.views import View
from app.models.Post import Post
from masonite.request import Request
from masonite.response import Response

class PostController(Controller):

    def show(self, view: View):
        posts = Post.all()
        return view.render("posts", {"posts" : posts})

    def single(self, view: View, request: Request):
        post = Post.find(request.param("id"))
        return view.render("single", {"post" : post})

    def update(self, view: View, request: Request):
        post = Post.find(request.param("id"))
        print(post)
        return view.render("update", {"post" : post})

    def store(self, request: Request, response: Response):
        post = Post.find(request.param("id"))
        post.title = request.input("title")
        post.body = request.input("body")

        post.save()
        return response.redirect("/posts")

    def delete(self, request: Request, response: Response):
        post = Post.find(request.param("id"))
        post.delete()
        return response.redirect("/posts")