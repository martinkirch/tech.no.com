window.updateHome = (d) ->
  ul = $('<ul>').addClass('thumbnails')

  for ep in d.data
    li = _.template($('#episode_thumb_template').html(),
      link: "#/episode/" + ep.slug
      pic: ep.pictures.large
      name: ep.name
    )
    ul.append(li)

  $("#appbody").append(ul)

window.dispEpisode = (d) ->
  html = _.template($('#episode_template').html(),
    name: d.name
    slug: d.slug
  )
  $("#appbody").html(html)
  url = "http://api.mixcloud.com/michelplatiniste/" +
          d.slug +
          "/embed-json/?callback=setupPlayer&width=500"
  $.getScript(url)

window.setupPlayer = (d) ->
  $("#michelplayer").html(d.html)

window.updatePic = (d) ->
  img = $('<img>', src: d.pictures.medium)
  $("#avatar").html(img)

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
