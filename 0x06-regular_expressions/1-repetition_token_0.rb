#!/usr/bin/env ruby
arg = ARGV[0]

match =arg.scan(/^hb[t]{2,}n/i)
puts match.join
