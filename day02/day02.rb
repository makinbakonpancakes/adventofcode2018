data = File.readlines('input.txt').map(&:chars)
counter = data.map{ |x| x.group_by &:itself}
twos = counter.count{ |x| x.any?{ |x,y| y.count == 2 }}
threes = counter.count{ |x| x.any?{ |x,y| y.count == 3 } }
p twos * threes
data.map{ |x| data.map { |y|
            a = x.zip(y).count{ |x,y| x!=y }
            (p x.join, y.join
             1/0) if a == 1
          }}

