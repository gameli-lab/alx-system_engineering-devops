#!/usr/bin/env ruby
#Regex

inp = ARGV[0]

pattern = /hbt{2,5}n/

if inp.match?(pattern)
  return (1)
else
  return (0)
