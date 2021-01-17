thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # นำตำแหน่งที่ 1 ออกไป
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()  # เอาตำแหน่งสุดท้ายออกไป หฟากไม่กำหนดตำแหน่ง
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]  # ลบตำแหน่งที่ 0
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()  # การเคลียร์ list ออกหมด
print(thislist)