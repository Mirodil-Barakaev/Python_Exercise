def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

print(to_celsius(100))    
print(to_fahrenheit(0))   
print(to_celsius(32))     
print(to_fahrenheit(100)) 
