<html>
    <head>
        <title>tech.no.com</title>
        <link rel="stylesheet"
              href="${request.static_url('tcom:static/bootstrap.css')}"
              type="text/css"
              media="screen"
              charset="utf-8"
          />
          % for reqt in (css_links or []):
            <link rel="stylesheet"
                  href="${request.static_url('deform:static/%s' % reqt)}"
                  type="text/css" />
          % endfor
          % for reqt in (js_links or []):
            <script type="text/javascript"
                    src="${request.static_url('deform:static/%s' % reqt)}"
             ></script>
          % endfor
    </head>
    <body>

      <div class="navbar navbar-inverse">
        <div class="navbar-inner">
          <div class="container" style="width: auto;">
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </a>
            <a class="brand" href="#">
              tech.no.com
            </a>
            <div class="nav-collapse">
              <ul class="nav">
                <li class="active"><a href="#">Home</a></li>
              </ul>
            </div><!-- /.nav-collapse -->
          </div>
        </div><!-- /navbar-inner -->
      </div><!-- /navbar -->

      <div class="container">
        ${self.body()}
      </div>

    </body>
</html>
