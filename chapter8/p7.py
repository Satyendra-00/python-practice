l=["rohan","sohan","mohan","gohan","tohan","satyendra"]
def rem(l,word):
    n=[]
    for item in l:
        cleaned_item = item.strip()
        if cleaned_item != word:
            n.append(cleaned_item)
    return n
print(rem(l,"an"))
