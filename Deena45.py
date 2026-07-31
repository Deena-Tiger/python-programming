def numtowords(num):
a = {“0” : “” , “1” : “one” , “2” : “Two” , “3” : “Three” , “4” : “Four” , “5” : “Five” , “6” : “six” , “7” : “Seven” , “8” : “Eight”
, “9” : “Nine”}
c = {
“2”: “Twenty”, “3”: “Thirty”, “4”: “Forty”, “5”: “Fifty”, “6”: “Sixty”,
“7”: “Seventy”, “8”: “Eighty”, “9”: “Ninety”
}
num = str(num)
if len(num) == 4:
forma = a[num[0]] +” ” +”Thousand” +” ” +a[num[1]] +” ” +”Hundred” +” ” +c[num[2]] +” ” +a[num[3]]
elif len(num) == 3:
forma = a[num[0]] +” ” +”Hundered” +” ” +c[num[1]] +” ” +a[num[2]]
elif len(num) == 2:
forma = c[num[0]] +” ” +a[num[1]]
else:
forma = a[num]

print(forma)

num = int(input(“Enter your number : “))
numtowords(num)
