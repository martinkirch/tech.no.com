<html>
<head>
    <title>tech.no.com</title>
</head>
<body>
App
<script src='/static/js/underscore-min.js'></script>
<script src='/static/js/json2.js'></script>
<script src='/static/js/jquery-1.8.3.min.js'></script>
<script src='/static/js/backbone-min.js'></script>
<script>
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
</script>
</body>
</html>
