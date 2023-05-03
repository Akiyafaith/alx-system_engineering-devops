#!/usr/bin/env ruby

arg = ARGV[0]

match =arg.scan(/hbt+n/i)
put match.join("\n")
