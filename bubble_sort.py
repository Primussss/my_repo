#function for accenpting percentage of students
def input_percentage():
      
      number_of_students = int(input("Enter the number of students : "))
      for i in range (number_of_students):
            perc.append(float(input("Enter the percent of students(0)".format(i+1))))
            return perc


#function for printing percentage of students
def print_percentage(perc):
      for i in range(len(perc)):
          print(perc[i],sep = "\n")      

#function for performing partition of data
def percentage_partition(perc,start,end):
      pivot = perc[start]
      lower_bound = start + 1
      upper_bound = end

      while True:
            while lower_bound <= upper_bound and perc[lower_bound] <= pivot:
                  lower_bound += 1

            while lower_bound <= upper_bound and perc[upper_bound] >= pivot:
                  upper_bound -= 1 

            if lower_bound <= upper_bound:
                  perc[lower_bound],perc[upper_bound] = perc[upper_bound],perc[lower_bound]

            else:
                  break

      perc[start],perc[upper_bound] = perc[upper_bound],perc[start]
      return upper_bound

#function for performing quick sort on the data

def Quick_sort(perc,start,end):
      while start < end:
            partition = percentage_partition(perc,start,end)
            Quick_sort(perc,start,partition-1)
            Quick_sort(perc,partition+1,end)
            return perc
      
#function for displaying top five percentage fo students

def display_top_five(perc):
      print("top five percentage are :")
      if len(perc) < 5:
            start,stop = len(perc)-1, -1
      else:
            start,stop = len(perc)-1, len(perc) - 6
      for i in range(start,stop,-1):
            print(perc[i],sep = "\n")

#Main

unsorted_percentage = []
sorted_percentage = []
flag = 1

while flag == 1:
      print("\n---------Menu----------")
      print("1. Accept the percentage of Students")
      print("2. Display the percentage of Students")
      print("3. Perform Quick sort on the Data")
      print("4. Exit")

      ch = int(input("Enter choice (from 1 to 4) : "))

      if ch == 1:
            unsorted_percentage = input_percentage()

      elif ch == 2:
            print_percentage(unsorted_percentage)

      elif ch == 3:
            print("Percentage of students after performing quick sort : ")
            sorted_percentage = Quick_sort(unsorted_percentage,0,len(unsorted_percentage)-1)
            print_percentage(sorted_percentage)
            a = input("Do you want to display the top  percentages of the students (yes/no) : ")
            if a == 'yes':
                  display_top_five(sorted_percentage)

      elif ch == 4:
            print("Thanks for using this program!!")
            flag = 0   
      else:
            print("Invalid choice") 


#<-----------------------------------------END OF PROGRAM----------------------------------------->                                      

  