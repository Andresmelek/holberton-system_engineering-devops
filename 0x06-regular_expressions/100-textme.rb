#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:|to:|flag:)([A-Za-z0-9.+-:]{0,9}+\b/).join + ","
