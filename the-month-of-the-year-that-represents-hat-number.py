#!/usr/bin/env python3

# Created by: Sam. Garcon
# Created on: June 2021
# This program do Number is Positive, Negative or zero

 import calendar
 
def main():
    # this function display the month of the year that represents that number
    
    # input
    for month_idx in range(1, 13):
    print (calendar.month_name[month_idx])
    print (calendar.month_abbr[month_idx])
    print ("")
    
if __name__ == "__main__":
    main()
