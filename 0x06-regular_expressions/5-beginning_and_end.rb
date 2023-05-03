#!/usr/bin/env ruby

input_arg = ARGV[0]

match = input_arg.scan(/^h.n/)
puts match.join
