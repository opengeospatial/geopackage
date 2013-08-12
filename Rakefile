task :default => :preview

desc 'Setup the environment to run Awestruct'
task :setup, [:env] => :init do |task, args|
  next if !which('awestruct').nil?

  if args[:env] == 'local'
    require 'fileutils'
    FileUtils.remove_file 'Gemfile.lock', true
    FileUtils.remove_dir '.bundle', true
    system 'bundle install --binstubs=_bin --path=.bundle'
  else
    system 'bundle install'
  end

  msg 'Run awestruct using `awestruct` or `rake`'
  # Don't execute any more tasks, need to reset env
  exit 0
end

desc 'Update the environment to run Awestruct'
task :update => :init do
  system 'bundle update'
  # Don't execute any more tasks, need to reset env
  exit 0
end

desc 'Build and preview the site locally in development mode'
task :preview => :check do
  run_awestruct '-d'
end

# provide a serve task for those used to Jekyll commands
desc 'An alias to the preview task'
task :serve => :preview

desc 'Generate the site using the specified profile (default: development)'
task :gen, [:profile] => :check do |task, args|
  profile = args[:profile] || 'development'
  profile = 'production' if profile == 'prod'
  run_awestruct "-P #{profile} -g --force"
end

desc 'Generate the site and deploy to production'
task :deploy => :check do
  run_awestruct '-P production -g --force --deploy'
end

desc 'Clean out generated site and temporary files'
task :clean, :spec do |task, args|
  require 'fileutils'
  dirs = ['.awestruct', '.sass-cache', '_site']
  if args[:spec] == 'all'
    dirs << '_tmp'
  end
  dirs.each do |dir|
    FileUtils.remove_dir dir unless !File.directory? dir
  end
end

# Perform initialization steps, such as setting up the PATH
task :init do
  # Detect using gems local to project
  if File.exist? '_bin'
    ENV['PATH'] = "_bin#{File::PATH_SEPARATOR}#{ENV['PATH']}"
    ENV['GEM_HOME'] = '.bundle'
  end
end

desc 'Check to ensure the environment is properly configured'
task :check => :init do
  begin
    require 'bundler'
    Bundler.setup
  rescue Exception => e
    msg e.message, :warn
    exit e.status_code
  end
end

# Execute Awestruct
def run_awestruct(args)
  system "bundle exec awestruct #{args}"
end

# Print a message to STDOUT
def msg(text, level = :info)
  case level
  when :warn
    puts "\e[31m#{text}\e[0m"
  else
    puts "\e[33m#{text}\e[0m"
  end
end

desc 'Generate site from Travis CI and publish site to GitHub Pages'
task :travis do
  # if this is a pull request, do a simple build of the site and stop
  if ENV['TRAVIS_PULL_REQUEST'].to_s.to_i > 0
    puts 'Pull request detected. Executing build only.'
    system 'bundle exec awestruct -P production -g'
    next
  end

  repo = %x(git config remote.origin.url).gsub(/^git:/, 'https:')
  deploy_branch = 'gh-pages'
  if repo.match(/github\.com\.git$/)
    deploy_branch = 'master'
  end
  system "git remote set-url --push origin #{repo}"
  system "git remote set-branches --add origin #{deploy_branch}"
  system 'git fetch -q'
  system "git config user.name '#{ENV['GIT_NAME']}'"
  system "git config user.email '#{ENV['GIT_EMAIL']}'"
  system 'git config credential.helper "store --file=.git/credentials"'
  File.open('.git/credentials', 'w') do |f|
    f.write("https://#{ENV['GH_TOKEN']}:@github.com")
  end
  system "git branch #{deploy_branch} origin/#{deploy_branch}"
  system 'bundle exec awestruct -P production -g --deploy'
  File.delete '.git/credentials'
end