#!/usr/bin/env ruby

inputarg = ARGV[0]
match_result = inputarg.scan(/^hb{0,2}tn/)
puts match_result.join
