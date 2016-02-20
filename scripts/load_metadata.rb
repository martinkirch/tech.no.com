require 'rest-client'
require 'yaml'

def get_pics
    thumbnails_dir = '_data/thumbnails/' 
    unless File.directory? thumbnails_dir
      Dir.mkdir thumbnails_dir
    end
    url = 'https://api.mixcloud.com/michelplatiniste/cloudcasts'
    r = RestClient.get url, {:params => {:limit => 50}}
    j = JSON.parse(r)
    j['data'].each do |ep|
      path = thumbnails_dir + ep['slug'] + '.yml'
      File.write path, ep['pictures']['large']
    end
end

get_pics
