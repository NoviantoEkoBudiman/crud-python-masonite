from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.get("/blog", "BlogController@show"),
    Route.post("/blog/create","BlogController@store"),
    Route.get("/posts","PostController@show"),
    Route.get("/post/@id","PostController@single").name("detail_post"),
    Route.get("/post/@id/update","PostController@update").name("edit_post"),
    Route.post("/post/@id/update","PostController@store").name("update_post"),
    Route.get("/delete/@id", "PostController@delete").name("delete_post")
]

ROUTES += Auth.routes()