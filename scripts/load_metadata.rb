require 'rest-client'

def prepare_dir(base)
  path = "_data/#{base}/"
  unless File.directory? path
    Dir.mkdir path
  end
  path
end


def get_pics
    directory = prepare_dir 'thumbnails'
    url = 'https://api.mixcloud.com/michelplatiniste/cloudcasts'
    r = RestClient.get url, {:params => {:limit => 50}}
    j = JSON.parse(r)
    j['data'].map do |ep|
      slug = ep['slug']
      path = directory + slug + '.yml'
      File.write path, ep['pictures']['large']
      slug
    end
end

def get_size(slug)
  url = "https://s3-eu-west-1.amazonaws.com/files.tech.no.com/podcasts/#{slug}.mp3"
  r = RestClient.head url
  r.headers[:content_length]
end

def get_sizes(slugs)
  directory = prepare_dir 'sizes'
  slugs.each do |slug|
    puts slug
    begin
      sz = get_size slug
    rescue => e
      puts "WARN: could not get size for #{slug}: #{e}"
      sz = 0
    end
    path = directory + slug + '.yml'
    File.write path, sz
  end
end

eps = get_pics
get_sizes eps
