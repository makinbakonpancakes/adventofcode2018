require 'date'

data = File.readlines('input.txt').map { |x|
  [DateTime.strptime(x[1..16], "%Y-%m-%d %H:%M"), x[19..-2]] }
data.sort! { |x,y| x[0] <=> y[0] }
guards = Hash.new{ |h,k| h[k] = Array.new(60, 0) }
for d in data
  if d[1].include? "#"
    guard = d[1].match(/#(\d+)/)[1].to_i
  elsif d[1].include? "asleep"
    sleep_t = d[0].min
  else
    wake_t = d[0].min
    (sleep_t...wake_t).each { |t| guards[guard][t] += 1 }
  end
end
sleepy = guards.sort_by { |k, v| guards[k].sum }.reverse.first
p sleepy[0] * sleepy[1].index(sleepy[1].max)
sleepy2 = guards.sort_by { |k, v| guards[k].max }.reverse.first
p sleepy2[0] * sleepy2[1].index(sleepy2[1].max)
