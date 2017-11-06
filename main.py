def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while ((leftmark <= rightmark) and (alist[leftmark].get_id() <= pivotvalue.get_id())):
           leftmark = leftmark + 1

       while ((alist[rightmark].get_id() >= pivotvalue.get_id()) and (rightmark >= leftmark)):
           rightmark = rightmark -1 

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

def binarySearch(aList, sid):
    start = 0
    end = len(aList)-1
    done = False
    count = 0
    
    while not done and start <= end:
        mid = (start+end) // 2
        count +=1
        if (sid > aList[mid].get_id()):
            start = mid+1
        elif (sid < aList[mid].get_id()):
            end = mid-1
        else:
            done = True
    if done == True:
        return aList[mid].__str__()
    else:
        return "Not found."


class Student(object):
    def __init__(self, sid, gpa, age, credit):
        self.sid = sid
        self.gpa = gpa
        self.age = age
        self.credit = credit

    def get_id(self):
        return self.sid

    def get_gpa(self):
        return self.gpa

    def get_age(self):
        return self.age

    def get_credit(self):
        return self.credit

    def update_id(self, id):
        self.sid = id

    def update_gpa(self, gpa):
        self.gpa = gpa

    def update_age(self, age):
        self.age = age

    def update_credit(self, credit):
        self.credit = credit
      
    def __str__(self):
       info = ("+ Student ID: %s\tCumulative GPA: %s\tAge: %s\t Total Courses Credits: %s" % (self.sid, self.gpa, self.age, self.credit))
       return info

    

def main():
    fp = open("LCSC-Student_Records.dat")
    aList = []

    while True:
        line = fp.readline()

        if line == "":
            break

        line = line.strip()
        word = line.split()

        student = Student(word[0],word[1],word[2],word[3])

        aList.append(student)

    quickSort(aList)

    students_ids = ["74261880", "47355068", "57518851", "85055902", "67183075"]

    for id in students_ids:
       print(binarySearch(aList, id))

    

main()
