# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

# For GitHub Pages
# gem 'github-pages', ">=206", group: :jekyll_plugins

# For local serving
gem "jekyll", "~> 4.0.0"
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
    gem "tzinfo", "~> 1.2"
    gem "tzinfo-data"
end
gem "wdm", "~> 0.1.1", :install_if => Gem.win_platform?
gem "webrick", "~> 1.7"