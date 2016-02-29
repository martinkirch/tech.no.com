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
