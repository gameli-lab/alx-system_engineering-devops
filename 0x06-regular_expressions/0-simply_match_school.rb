#Ruby regexp file

input = ARGV[0]

pattern = /School/

matches = input.scan(pattern)

matches.each do
  puts "School"
end
