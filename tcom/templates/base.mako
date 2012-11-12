<html>
    <head>
        <title>tech.no.com</title>
        <link rel="stylesheet"
              href="${request.static_url('tcom:static/bootstrap.css')}"
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
            width: 100px;
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
            <li>Episodes</li>
            <li>Podcast</li>
            <li>Twitter</li>
            <li>Mixcloud</li>
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
               src="http://api.mixcloud.com/michelplatiniste/cloudcasts/?callback=dispmichel&limit=5"
        ></script>
    </body>
</html>
