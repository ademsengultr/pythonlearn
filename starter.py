#this is my starter notes for python

########
# 1 değişkenler ve veri tipleri
# -python değişkenlerini tanımlarken veri tipi belirtmeye gerek yoktur.

# bool - int - float - list - string - tuples - dictionaries

number = 10
pi = 3.14
name = "John"
is_adult = True
fruits = ["elma", "armut", "çilek"]
coordinates = (3, 4)
person = {"name": "John", "age": 25}

# print fonksiyonu yazdırma amaçlıdır

print("number = ", number)

# float için virgülden sonrasını yuvarlamak veya belli bir hane göstermek için aşağıdaki yöntemler izlenir


# # float_number = 3.14159
# # cropped_number = round(float_number, 2)
# # print(cropped_number)

# # float_number = 3.14159
# # formatted_number = "{:.2f}".format(float_number)
# # print(formatted_number)

########
# 2 koşullu ifadeler if elif else - karşılaştırma ifadeleri ve mantıksal operatörlerle kullanılabilir

if number > pi:
     print("number is greater than Pi")
###
if number > pi and number <=10:
     print("number is between Pi and 10")
elif number > 10:
     print("number is far away from Pi")
else: print("number is small than Pi")

########
# 3 döngüler for ve while döngüleri
print("\nfor loop ")
for i in range(number):
     print(number," - ", i)

count = 0
print("\nwhile loop ")
while count < number:
     print(number," - ", count)
     count += 1

# for ve while arasındaki fark: for ;belli bir sayıda döndürmek için while ;koşul sağlandığı sürece döndürmek içindir
# break ve continue kullanılabilir

print("before crash break loop")
count = 10
while count <= number:
     if count == 0:
          break
     result = number/count
     print("number/count = ", round(result, 2))
     count -= 1

########
# 3 listeler ve diziler