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
            top: 10;
            left: 10;
            bottom: 10;
            width: 150px;
        }

        nav .social {
            margin-top: 30px;
        }
        </style>
        <script type="text/javascript"
                src="${request.static_url('tcom:static/tcom.js')}"
        ></script>
        <script type="text/javascript"
                src="${request.static_url('tcom:static/jquery-1.8.2.min.js')}"
         ></script>
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
        ${self.body()}
      </div>

      <script type="text/javascript">
        start();
      </script>
    </body>
</html>
