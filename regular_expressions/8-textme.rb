#!/usr/bin/env ruby
input = ARGV[0]

# Use regular expressions to extract the required information
sender = input.scan(/\[from:(.*?)\]/).flatten.first
receiver = input.scan(/\[to:(.*?)\]/).flatten.first
flags = input.scan(/\[flags:(.*?)\]/).flatten.first

# Output in the format: [SENDER],[RECEIVER],[FLAGS]
puts "#{sender},#{receiver},#{flags}"
