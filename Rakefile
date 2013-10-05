desc 'Generate site'
task :build do
  Dir.mkdir 'build' unless File.directory? 'build'

  system './runasciidoctor -D build ./index.adoc'
end

desc 'Generate site from Travis CI and publish site to GitHub Pages'
task :travis do
  # if this is a pull request, do a simple build of the site and stop
  if ENV['TRAVIS_PULL_REQUEST'].to_s.to_i > 0
    puts 'Pull request detected. Executing build only.'
    system './runasciidoctor ./index.adoc'
    next
  end

  repo = %x(git config remote.origin.url).gsub(/^git:/, 'https:')
  deploy_branch = 'gh-pages'

  system "git checkout -b #{deploy_branch} origin/#{deploy_branch}"
  system "git clone . build"
  system "git checkout master"
  Dir.chdir 'build'

  system "git remote set-url --push origin #{repo}"
  system "git config user.name '#{ENV['GIT_NAME']}'"
  system "git config user.email '#{ENV['GIT_EMAIL']}'"
  system 'git config credential.helper "store --file=.git/credentials"'
  File.open('.git/credentials', 'w') do |f|
    f.write("https://#{ENV['GH_TOKEN']}:@github.com")
  end

  system 'git rm -r .'
  system '../runasciidoctor -D . ../index.adoc'
  system 'git add *'
  system 'git commit -m "Publish site to github pages"'
  system 'git push origin'

  File.delete '.git/credentials'
end