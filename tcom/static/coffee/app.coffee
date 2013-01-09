window.updateHome = (d) ->
  eps = d.data
  html = ""
  html += '<ul class="thumbnails">'

  for ep in eps
    slug = ep.slug
    url = "#/episode/" + slug
    name = ep.name

    html += '  <li class="span4">'
    html += '   <a href="' + url + '">'
    html += '    <div class="thumbnail">'
    html += '      <img src="'  + ep.pictures.large + '" />'
    html += '      <h3>' + name + '</h3>'
    html += '    </div>'
    html += '   </a>'
    html += '  </li>'
  html += '</ul>'
  $("#appbody").append(html)

window.dispEpisode = (d) ->
  name = d.name

  html = ""
  html += '<h2>' + name + '</h2>'
  html += '<div id="michelplayer"></div>'

  $("#appbody").html(html)

  url = "http://api.mixcloud.com/michelplatiniste/" +
          d.slug +
          "/embed-json/?callback=setupPlayer&width=500"
  $.getScript(url)

window.setupPlayer = (d) ->
  $("#michelplayer").html(d.html)

window.updatePic = (d) ->
  url = d.pictures.medium
  $("#avatar").html("<img src='" + url + "' />")

HomeView = Backbone.View.extend(
  initialize: () ->
    this.render()
  render: () ->
    $.getScript("http://api.mixcloud.com/michelplatiniste/cloudcasts/?callback=updateHome")
    $.getScript("http://api.mixcloud.com/michelplatiniste/?callback=updatePic")
)

EpisodeView = Backbone.View.extend(
  initialize: () ->
    this.render()
    slug = this.options.slug
    $.getScript("http://api.mixcloud.com/michelplatiniste/"+slug+"?callback=dispEpisode")
)

AppRouter = Backbone.Router.extend(
  routes:
    "episode/:slug": "getEpisode"
    "*actions": "defaultRoute"
)

app_router = new AppRouter
app_router.on('route:defaultRoute', (actions) ->
  new HomeView()
)
app_router.on('route:getEpisode', (slug) ->
  new EpisodeView(
    slug: slug
  )
)

Backbone.history.start()
