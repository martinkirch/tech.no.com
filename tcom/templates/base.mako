<html>
    <head>
        <title>tech.no.com</title>
        <link rel="stylesheet"
              href="${request.static_url('tcom:static/css/bootstrap.css')}"
              type="text/css"
              media="screen"
              charset="utf-8"
          />
        <style type="text/css"
              media="screen"
              charset="utf-8">
        nav {
            position: fixed;
            top: 0;
            left: 0;
            bottom: 0;
            width: 150px;
        }
        </style>
        <script type="text/javascript"
                src="${request.static_url('tcom:static/tcom.js')}"
        ></script>
    </head>
    <body>

    <nav>
        <ul class="nav nav-list">
            <li class="nav-header">tech.no.com</li>
            <li><i class="icon-list"></i> Episodes</li>
            <li><i class="icon-download-alt"></i> Podcast</li>
            <li><i class="icon-comment"></i> Twitter</li>
            <li><i class="icon-music"></i> Mixcloud</li>
            <li><i class="icon-envelope"></i> Email</li>
        </ul>
    </nav>

      <div class="container">
        <div id="michelcast"></div>
        ${self.body()}
      </div>

      <script type="text/javascript"
              src="${request.static_url('tcom:static/jquery-1.8.2.min.js')}"
       ></script>
       <script type="text/javascript"
               src="http://api.mixcloud.com/michelplatiniste/cloudcasts/?callback=dispmichel&limit=3"
        ></script>
    </body>
</html>
