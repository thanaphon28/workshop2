# จงแสดง "banana"
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
print(fruits)

# จงแก้ไขข้อมูลจาก "apple" เป็น "kiwi"
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)

# จงเพิ่ม "kiwi" ไปยัง fruits list fruits = ["apple", "banana", "cherry"]
kiwiAdd = ["kiwi"]
fruitsAdded = fruits + kiwiAdd
print(fruitsAdded)

# จงเพิ่ม "lemon" ไประหว่าง "apple" กับ "ิิbananna"
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)

# จงลบ "cherry" จาก list fruits = ["apple", "banana", "cherry"]
del fruits[-1]
print(fruits)

# จงแสดงตัวสุดท้ายของ fruits
fruits = ["apple", "banana", "cherry"]
lastFruits = fruits[-1]
print(lastFruits)

# จงแสดงจำนวนของ fruits
fruits = ["apple", "banana", "cherry"]
countFruits = 0
for fruitsList in fruits:
    countFruits = countFruits + 1
    print(countFruits)