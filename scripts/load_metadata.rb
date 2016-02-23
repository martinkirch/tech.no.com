require 'open-uri'
require 'rest-client'

def prepare_dir(base)
  path = "_data/#{base}/"
  unless File.directory? path
    Dir.mkdir path
  end
  path
end

def episodes
    url = 'https://api.mixcloud.com/michelplatiniste/cloudcasts'
    r = RestClient.get url, {:params => {:limit => 50}}
    j = JSON.parse(r)
    Hash[j['data'].map { |ep| [ep['slug'], ep] }]
end

def get_pics(eps)
    directory = prepare_dir 'thumbnails'
    eps.each do |slug, ep|
      path = directory + slug + '.yml'
      File.write path, ep['pictures']['large']
    end
end

def episode_url(slug)
  "https://s3-eu-west-1.amazonaws.com/files.tech.no.com/podcasts/#{slug}.mp3"
end

def get_size(slug)
  r = RestClient.head (episode_url slug)
  r.headers[:content_length]
end

def get_sizes(eps)
  directory = prepare_dir 'sizes'
  eps.each_key do |slug|
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

def find_not_uploaded(eps)
  here = Dir["_data/episodes/*.yml"].map{|f| File.basename f, '.yml'}
  there = eps.keys
  here.select{|local_ep| not there.include?(local_ep)}
end

def upload(slug)
  puts "Uploading #{slug}"
  mp3file = Tempfile.new('mixcloudupload')
  url = episode_url slug
  begin
    mp3file << open(url).read
  ensure
    mp3file.close
    mp3file.unlink
  end
end

eps = episodes
get_pics eps
get_sizes eps

not_uploaded = find_not_uploaded(eps)
not_uploaded.each { |name| upload(name) }

unless not_uploaded.empty?
  eps = episodes.select{|slug, _| not_uploaded.include? slug}
  get_pics eps
  get_sizes eps
end
