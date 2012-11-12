function embedit(d) {
    $("#michelcast").append(d['html']);
}

function dispmichel(d) {
    eps = d.data;
    for (i in eps) {
        slug = eps[i].slug;
        url = "http://api.mixcloud.com/michelplatiniste/"
            + slug
            + "/embed-json/?callback=embedit&width=500&height=64";
        $.getScript(url);
    }
}

function showpic(d) {
  url = d.pictures.medium;
  $("#avatar").html("<img src='" + url + "' />");
}

function start() {
  $.getScript("http://api.mixcloud.com/michelplatiniste/cloudcasts/?callback=dispmichel&limit=3");
  $.getScript("http://api.mixcloud.com/michelplatiniste/?callback=showpic");
}
