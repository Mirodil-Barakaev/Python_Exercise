lst=["Azamjon", "Eshmat", "Toshmat"]
def GetMaxName(lst: list[str])-> str:
    ism = lst[0]
    for i in range(1,len(lst)):
        if len(ism) <= len(lst[i]):
            ism = lst[i]
        
    return ism
print(GetMaxName(lst))