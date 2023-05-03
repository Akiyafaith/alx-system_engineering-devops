#!/usr/bin/env ruby

argument = ARGV[0]
match = argument.scan(/^\d{10}$/)
puts match.join
