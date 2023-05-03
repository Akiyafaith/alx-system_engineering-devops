#!/usr/bin/env ruby

arg = ARGV[0]

match =arg.scan(/h(a)+t/i)
put match.join("\n")
