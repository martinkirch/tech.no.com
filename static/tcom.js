function dispmichel(d) {
    var eps = d.data;
    var html = "";
    for (i in eps) {
        var slug = eps[i].slug;
        var url = "/episode/" + slug;
        var name = eps[i].name;
        html += '   <div class="col-md-4 episode-thumbnail">'
        html += '    <a href="' + url + '">'
        html += '      <img src="'  + eps[i].pictures.large + '" />';
        html += '      <h3>' + name + '</h3>'
        html += '    </a>'
        html += '   </div>'

    }
    $("#michelcasts").append(html);
}

function start() {
  $.getScript("http://api.mixcloud.com/michelplatiniste/cloudcasts/?callback=dispmichel");
}

function disp_episode(d) {
  var name = d.name;

  var html = "";
  html += '<h2>' + name + '</h2>';
  var dllink = window.location + '/download';
  html += '<a href="' + dllink + '"><i class="glyphicon glyphicon-download"></i> Download this episode</a>'
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
