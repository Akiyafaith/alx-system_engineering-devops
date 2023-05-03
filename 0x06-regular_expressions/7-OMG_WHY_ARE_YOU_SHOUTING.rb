#!/usr/bin/env ruby

input = ARGV[0]
match = input.scan(/[A-Z]/)
puts match.join
