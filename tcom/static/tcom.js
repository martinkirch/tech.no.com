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
