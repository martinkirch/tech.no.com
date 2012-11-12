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
    </head>
    <body>

    <nav>
        <ul class="nav nav-list">
            <li class="nav-header">Episodes</li>
            <li>Podcast</li>
            <li>Twitter</li>
            <li>Mixcloud</li>
        </ul>
    </nav>

      <div class="container">
        ${self.body()}
      </div>

    </body>
</html>
