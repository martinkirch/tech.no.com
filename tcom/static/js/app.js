var AppRouter = Backbone.Router.extend({
    routes: {
        "episode/:slug": "getEpisode",
        "*actions": "defaultRoute"
    }
});
var app_router = new AppRouter;
app_router.on('route:defaultRoute', function(actions){
    alert('/');
});
app_router.on('route:getEpisode', function(slug){
    alert("Get post number " + slug);
});

Backbone.history.start();
