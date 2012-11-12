function dispmichel(d) {
    eps = d.data;
    html = "";
    html += '<ul class="thumbnails">'
    for (i in eps) {
        slug = eps[i].slug;
        console.log(eps[i]);
        url = "/episode/" + slug;
        name = eps[i].name;

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
  url = d.pictures.medium;
  $("#avatar").html("<img src='" + url + "' />");
}

function start() {
  $.getScript("http://api.mixcloud.com/michelplatiniste/cloudcasts/?callback=dispmichel");
  $.getScript("http://api.mixcloud.com/michelplatiniste/?callback=showpic");
}
