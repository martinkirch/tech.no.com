function updateHome(d) {
    var eps = d.data;
    var html = "";
    html += '<ul class="thumbnails">'
    for (i in eps) {
        var slug = eps[i].slug;
        var url = "#/episode/" + slug;
        var name = eps[i].name;

        html += '  <li class="span4">';
        html += '   <a href="' + url + '">'
        html += '    <div class="thumbnail">'
        html += '      <img src="'  + eps[i].pictures.large + '" />';
        html += '      <h3>' + name + '</h3>'
        html += '    </div>'
        html += '   </a>'
        html += '  </li>'

    }
    html += '</ul>'
    $("#appbody").append(html);
}

function dispEpisode(d) {
  var name = d.name;

  var html = "";
  html += '<h2>' + name + '</h2>';
  html += '<div id="michelplayer"></div>';

  $("#appbody").html(html);

  var url = "http://api.mixcloud.com/michelplatiniste/"
          + d.slug
          + "/embed-json/?callback=setupPlayer&width=500";
  $.getScript(url);
}

function setupPlayer(d) {
  $("#michelplayer").html(d.html);
}

function updatePic(d) {
  var url = d.pictures.medium;
  $("#avatar").html("<img src='" + url + "' />");
}

var HomeView = Backbone.View.extend({
    initialize: function() {
        this.render();
    },
    render: function() {
        $.getScript("http://api.mixcloud.com/michelplatiniste/cloudcasts/?callback=updateHome");
        $.getScript("http://api.mixcloud.com/michelplatiniste/?callback=updatePic");
    }
});

var EpisodeView = Backbone.View.extend({
    initialize: function() {
        this.render();
        var slug = this.options.slug;
        $.getScript("http://api.mixcloud.com/michelplatiniste/"+slug+"?callback=dispEpisode");
    },
});

var AppRouter = Backbone.Router.extend({
    routes: {
        "episode/:slug": "getEpisode",
        "*actions": "defaultRoute"
    }
});
var app_router = new AppRouter;
app_router.on('route:defaultRoute', function(actions) {
    new HomeView();
});
app_router.on('route:getEpisode', function(slug) {
    new EpisodeView({slug: slug});
});

Backbone.history.start();
