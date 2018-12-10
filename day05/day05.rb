input = File.read('input.txt').strip.split('')

def react(data)
  stack = [data.first]
  data[1..-1].each { |x|
    if !stack.empty? and (stack.last.ord - x.ord).abs == 32
      stack.pop
    else
      stack << x
    end
  }
  stack.length
end
p react(input)

sizes = []
(?a..?z).each { |char|
  data = input.select { |x| x != char and x != char.upcase }
  sizes << react(data)
  }
p sizes.min
