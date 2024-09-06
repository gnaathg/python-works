text = "RACECAR"

longest_p = ""

for i in range(0,len(text)) :

    right = i

    left = i

    while (left >= 0 and right < len(text) and text[left] == text[right]) :

        current_p = text[left:right+1]

        if len(current_p) > len(longest_p) :

            longest_p =  current_p

        left = left - 1

        right = right + 1

print(longest_p)