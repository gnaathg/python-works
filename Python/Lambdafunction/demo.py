add = lambda n1,n2 : n1 + n2

print(add(9,10))

sub = lambda n1,n2 : n1 - n2

print(sub(8,9))

cube = lambda n : n**3

print(cube(9))

max_two = lambda n1 , n2 : n1 if n1 > n2 else n2

print(max_two(77,90))

min_two = lambda n1 , n2 : n1 if n1 < n2 else n2

print(min_two(88,26))

last_digit_max = lambda n1 , n2 : n1 if n1 % 10 > n2 % 10 else n2

print(last_digit_max(127,872))

odd_even = lambda n : "even" if n % 2 == 0 else "odd"

print(odd_even(10))