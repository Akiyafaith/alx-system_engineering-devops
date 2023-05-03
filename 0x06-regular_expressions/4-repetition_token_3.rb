#!/usr/bin/env ruby

arguments = ARGV[0]
results = arguments.scan(/^hb[^o]+n/)
puts results.join
