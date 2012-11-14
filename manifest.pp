Exec {
    path => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
}

include webapp::python

vcsrepo {'/usr/local/src/tcom':
  ensure   => latest,
  provider => git,
  source   => 'gitolite@localhost:site.git',
  revision => 'master',
}

python::pip::install{'tcom':
  package => '/usr/local/src/tcom',
  venv    => '/usr/local/venv/tcom',
  owner   => 'www-data',
  group   => 'www-data',
  require => Webapp::Python::Instance['tcom'],
}

webapp::python::instance { 'tcom':
    ensure         => present,
    domain         => $fqdn,
    paste          => true,
    paste_settings => 'production.ini',
    requirements   => true,
}
