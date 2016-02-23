module Episode

  class Generator < Jekyll::Generator

    def episode(site, hash)
      slug, data = hash
      meta = data['meta']
      if meta.nil?
        date = data['date']
      else
        date = meta['published']
      end
      { 'url' => '/episode/' + slug + '.html',
        'guid' => '/episode/' + slug,
        'title' => data['title'],
        'pic' => site.data['thumbnails'][slug],
        'date' => date,
        'description' => data['desc'],
        'tracks' => data['tracks'],
        'length' => site.data['sizes'][slug],
        'slug' => slug,
      }
    end

    def episodes(site)
      site.data['episodes'].map{|h| episode(site, h)}.sort_by{|h| h['date']}.reverse
    end

    def expose_episodes(site, episodes)
      names = ['index.html', 'podcast.xml']
      site.pages.select {|page| names.include?(page.name)} .each {|page|
        page.data['episodes'] = episodes
      }
    end

    class EpisodePage < Jekyll::Page
      def initialize(site, episode)
        @site = site
        @base = site.source
        @dir = 'episode'
        @name = episode['slug'] + '.html'

        self.process(@name)
        self.read_yaml(File.join(@base, '_layouts'), 'episode.html')
        self.data.merge!(episode)
      end
    end

    def generate_episodes(site, episodes)
      episodes.each { |e|
        site.pages << EpisodePage.new(site, e)
      }
    end

    def generate(site)
      episodes = episodes(site)
      expose_episodes(site, episodes)
      generate_episodes(site, episodes)
    end
  end

end
