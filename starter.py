# @1 değişkenler ve veri tipleri
# - Python'da değişkenlerini tanımlarken veri tipi belirtmeye gerek yoktur.

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

print("\n")

# @2 koşullu ifadeler if elif else - karşılaştırma ifadeleri ve mantıksal operatörlerle kullanılabilir

if number > pi:
    print("number is greater than Pi")

# # 
if number > pi and number <= 10:
    print("number is between Pi and 10")
elif number > 10:
    print("number is far away from Pi")
else:
    print("number is smaller than or equal to Pi")

# # 
print("\n")

# @3 döngüler for ve while döngüleri
print("\nfor loop ")
for i in range(number):
    print(number, " - ", i)

count = 0
print("\nwhile loop ")
while count < number:
    print(number, " - ", count)
    count += 1

# for ve while arasındaki fark: for; belirli bir sayıda döndürmek için, while; koşul sağlandığı sürece döndürmek içindir
# break ve continue kullanılabilir

print("before crash break loop")
count = 10
while count <= number:
    if count == 0:
        break
    result = number / count
    print("number/count = ", round(result, 2))
    count -= 1

# # 
print("\n")

# @4 listeler ve diziler 
# listeler ve diziler hem karmaşık bir o kadar da iş çözücüdür
# bu bölüm 3 ana başlık altında incelenebilir.
# oluşturma - düzeltme - erişim

array1 = ["0 - member", 12, "true"]
print("array1's first member is [0] = ", array1[0])
print("-\n")

# sona ekleme yapmak için .append, eleman silmek için .pop bunlar array sınıfına ait fonksiyonlardır
array1.append("Hello")
array1.pop(0)
array1.insert(0, "0. eleman")

for i in range(len(array1)):
    print("Eleman - ", i, " - ", array1[i])

print("-\n")

# for döngüsü ile dizi oluşturalım 
# 2'nin 10. kuvvetine kadar olan sayıların olduğu bir dizi

array2 = []  # kaçıncı kuvvet olduğu
array3 = []  # kuvvetin değeri

for i in range(11):
    array2.append(i)
    count = 2
    i1 = 1
    while i1 < i:
        count = count * 2
        i1 += 1
    array3.append(count)
array3[0] = 1
     
# for i in range(len(array2)):
#      print("Element - ", array2[i] , " - ",array3[i])

print("-\n")

# aynısını 2 boyutlu dizi ile yapmakta mümkün
# hatta oluşturmaya bile gerek yok, zaten elimizde var iki adet dizi yapmamız gereken iç içe for döngüsü

arraypower2 = [[0, 0] for _ in range(11)]  # belli bir sayıda boş çok boyutlu dizi oluşturma

for i in range(len(array2)):
    arraypower2[i][0] = array2[i]
    arraypower2[i][1] = array3[i]

for i in range(len(arraypower2)):
    print("2 nin ", arraypower2[i][0], ". kuvveti = ", arraypower2[i][1])

print("-\n")

# @fonksiyonlar
# fonksiyonlar parametre alabilir ve bu parametreye varsayılan bir değer atanabilir
# fonksiyonlar return ile geri veri döndürebilir

def merhaba():
    print("hello world")
     
merhaba()

def parametreli(x):
    return x * x

print("Parametre 10, karesi - ", parametreli(10))

# birden fazla parametre de alabilir

def carpim(x, y):
    return x * y

print("10 * 2 - ", carpim(10, 2))

# esnek parametre *args ile anahtar kelime ile parametre, **kwargs ile oluşturulur

def summary(*args):
    suma = 0
    for num in args:
        suma += num
    return suma

print(summary(12, 13, 14, 15))
