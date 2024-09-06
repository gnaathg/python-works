placement = {"testing" : 45, "python" : 33, "java" : 65, "laravel" : 76}

def get_value(key) :

    return placement.get(key)

srt = sorted(placement,key=get_value,reverse=True)

print(srt)