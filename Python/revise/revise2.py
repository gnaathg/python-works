src = "CHICKEN"

trg = "HEN"

word_cnt = {}

for w in src :

    if w in word_cnt :

        word_cnt[w] += 1

    else :

        word_cnt[w] = 1

is_kngro_wrd = True


for ch in trg :

    if ch in word_cnt and word_cnt.get(ch) > 0 :

        word_cnt[ch] -= 1

    else :

        is_kngro_wrd = False

        break

print(is_kngro_wrd)