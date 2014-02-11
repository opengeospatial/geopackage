require 'fileutils'

task :init_local do
  Dir.mkdir 'build' unless File.directory? 'build'
end

task :generate do
  system './runasciidoctor -D build/spec -a stylesheet=./asciidoctor.css ./spec/index.adoc'
  FileUtils.cp_r 'images/.', 'build/spec'
  FileUtils.cp_r 'stylesheets/.', 'build/spec'
end

desc 'Generate site'
task :build => [:init_local, :generate]

task :init_travis do
  repo = %x(git config remote.origin.url).gsub(/^git:/, 'https:').strip
  deploy_branch = 'gh-pages'

  system "git clone --depth 1 -b #{deploy_branch} #{repo} build"
  Dir.chdir 'build/spec'
  system 'git rm -r .'
  Dir.chdir '../..'
end

task :publish do
  Dir.chdir 'build'
  system "git config user.name '#{ENV['GIT_NAME']}'"
  system "git config user.email '#{ENV['GIT_EMAIL']}'"
  system 'git config credential.helper "store --file=.git/credentials"'
  File.open('.git/credentials', 'w') do |f|
    f.write("https://#{ENV['GH_TOKEN']}:@github.com")
  end

  system 'git add *'
  system 'git commit -m "Publish specification to github pages"'

  system 'git config --global push.default simple'
  system 'git push origin'

  File.delete '.git/credentials'
end

desc 'Generate site from Travis CI and publish site to GitHub Pages'
task :travis => [:init_travis, :build, :publish]
unless ENV['TRAVIS_PULL_REQUEST'].to_s.to_i > 0
  # Only publish when we're not building to validate a pull request
  task :travis => [:publish]
end
