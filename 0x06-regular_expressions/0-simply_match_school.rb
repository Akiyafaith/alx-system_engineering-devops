#!/usr/bin/env ruby
require 'onigmo'

input_arg = ARGV[0]

if /School/i === input_arg
  puts "School"
end
