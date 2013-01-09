<html>
    <head>
        <title>tech.no.com</title>
        <link rel="stylesheet"
              href="/static/css/bootstrap.css"
              type="text/css"
              media="screen"
              charset="utf-8"
          />
        <style type="text/css"
              media="screen"
              charset="utf-8">
        nav {
            position: fixed;
            top: 10;
            left: 10;
            bottom: 10;
            width: 150px;
        }

        nav .social {
            margin-top: 30px;
        }
        </style>
    </head>
    <body>

    <nav>

        <a href="/"><div id="avatar" class="pagination-centered"></div></a>

        <ul class="nav nav-list">
            <li class="nav-header">tech.no.com</li>
            <li class="active"><a href="/"><i class="icon-list"></i> Episodes</a></li>
            <li><a href="#"><i class="icon-download-alt"></i> Podcast</a></li>
        </ul>
        <ul class="nav nav-list social">
            <li><a href="http://twitter.com/mplatiniste"><i class="icon-comment"></i> Twitter</a></li>
            <li><a href="http://mixcloud.com/michelplatiniste"><i class="icon-music"></i> Mixcloud</a></li>
            <li><a href="mailto:michel@tech.no.com"><i class="icon-envelope"></i> Email</a></li>
        </ul>

    </nav>

    <div class="container">
        <div id="appbody">
        </div>
    </div>

    </body>
    <script type="text/javascript" src='/static/js/underscore-min.js'></script>
    <script type="text/javascript" src='/static/js/json2.js'></script>
    <script type="text/javascript" src='/static/js/jquery-1.8.3.min.js'></script>
    <script type="text/javascript" src='/static/js/backbone-min.js'></script>
    <script type="text/javascript" src='/static/js/coffee-script.js'></script>
    <script type="text/coffeescript" src='/static/coffee/app.coffee'></script>
    <script type="text/javascript" src='/static/js/app.js'></script>
</html>
