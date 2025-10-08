def build_sentecese(*words,sep=""):
   return sep.join(words)
    

res = build_sentecese("Hello","Eshmat","How","are","you",sep=" ")
print(res)