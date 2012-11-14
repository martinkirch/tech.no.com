function dispmichel(d) {
    var eps = d.data;
    var html = "";
    html += '<ul class="thumbnails">'
    for (i in eps) {
        var slug = eps[i].slug;
        var url = "/episode/" + slug;
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
    $("#michelcasts").append(html);
}

function showpic(d) {
  var url = d.pictures.medium;
  $("#avatar").html("<img src='" + url + "' />");
}

function start() {
  $.getScript("http://api.mixcloud.com/michelplatiniste/cloudcasts/?callback=dispmichel");
  $.getScript("http://api.mixcloud.com/michelplatiniste/?callback=showpic");
}

function disp_episode(d) {
  var name = d.name;

  var html = "";
  html += '<h2>' + name + '</h2>';
  html += '<div id="michelplayer"></div>';

  $("#michelcast").html(html);

  var url = "http://api.mixcloud.com/michelplatiniste/"
          + d.slug
          + "/embed-json/?callback=setupplayer&width=500";
  $.getScript(url);
}

function setupplayer(d) {
  $("#michelplayer").html(d.html);
}
