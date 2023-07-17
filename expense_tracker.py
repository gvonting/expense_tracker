#!python3
from datetime import datetime
from csv import writer
import csv
import os


'''
#!TODO

- Add error handling for out of range datetimes
- Show descriptions in each category and their prices

'''
actions = ['Record Purchase', 'Print Summary']

purchase_types = ['auto-repair-maintenance', 'takeout-restaurants', 'bills-utilities', 'healthcare', 'gas', 'groceries', 'merchandise', 'leisure-travel', 'services']

#Create dictionaries, key values of purchase types and default values of 0 
monthly_totals = dict.fromkeys(purchase_types, 0)
yearly_totals = dict.fromkeys(purchase_types, 0)

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
'september', 'october', 'november', 'december']

#Path to store and retrieve data
main_path = ''

#This function is used to record a purchase
def record_purchase():
    flag = True

    while flag == True:
        made_today = input('\nWas this purchase made today? (yes, no): ')

        if made_today == 'yes':
            purchase_date = datetime.now()
            purchase_date_formatted = purchase_date.strftime("%Y/%m/%d")

        else:
            purchase_date = input('\nInput purchase_date formatted in: YYYY/MM/DD: ')
            year, month, day = map(int, purchase_date.split('/'))
            purchase_date = datetime(year, month, day)
            purchase_date_formatted = purchase_date.strftime("%Y/%m/%d")

        #Isolate the month and year
        purchase_year = purchase_date.strftime("%Y")

        #format purchase month
        purchase_month = (purchase_date.strftime("%m"))
        purchase_month_stripped = purchase_month.lstrip('0')
        purchase_month_string = months[int(purchase_month_stripped) - 1]

        #Define operating path
        year_path = main_path + purchase_year
        month_file = main_path + purchase_year + '/' + purchase_month + '_' + purchase_month_string + '_' + purchase_year + '.csv'

        #Check directory for the year folder and month file
        #check for main year folder, if none, create the directory
        if not os.path.isdir(year_path):
            os.mkdir(year_path)
        
        #Check for month file, if none, create the file and add headers
        if not os.path.isfile(month_file):
            header = ('date,amount,type,description')
            with open(month_file, 'w') as f:
                f.write(header)



        purchase_amount = input('\nTotal price of purchase: ')

        #Ask user for purchase type
        print('\n')
        for i in range(len(purchase_types)):
            print(str(i) + ': ' + purchase_types[i])
        purchase_type_input = input('\nWhat type of purchase was this: ')
        purchase_type = purchase_types[int(purchase_type_input)]


        purchase_description = input('\nDescription of purchase: ')

        #Formats purchase info into one line and appends it to the csv file
        purchase_info = ('\n' + purchase_date_formatted + ',' + purchase_amount + ',' + purchase_type + ',' + purchase_description)
        with open (month_file, 'a') as f:
            f.write(purchase_info)

        
        
        another_purchase = input('\nRecord another purchase? (yes, no): ')
        if another_purchase == 'no':
            flag = False


#grand_total finds the total amount for the dictionary passed to it
def grand_total(dictionary):
    grand_total = 0
    for key in dictionary:
        grand_total = grand_total + dictionary[key]
    return grand_total

#print_totals cleanly prints the total amounts 
def print_totals(dictionary, total):
    for key in dictionary:
        percentage_total = dictionary[key] / total
        print(f'{key:>24}: {float(dictionary[key]):>13.2f}$ || {percentage_total:>2.2%}')
    print('-' * 50)
    print(f'{"Total":>24}: {total:>13.2f}$')


#Prints the summary of the data based on the year the user wants to see
def print_summary():
    summary_year = input('\nWhat year: ')
    year_folder = main_path + summary_year + '/'

    #Need to get all the files that are in the directory
    all_files = sorted(os.listdir(year_folder))
    #print(all_files)

    for i in all_files:
        #print(year_folder + i)
        expense_file_path = year_folder + i
        expense_file = open(expense_file_path)
        expense_reader = csv.reader(expense_file)
        expense_list = list(expense_reader)
        #print(expense_list)
        for row in expense_list:
            #print(row[1])
            for item_type in purchase_types:
                if item_type in row:
                    #print(f'This purchase was {item_type} for {row[1]}')
                    monthly_totals[item_type] = monthly_totals[item_type] + float(row[1])
                    yearly_totals[item_type] = yearly_totals[item_type] + float(row[1])
        print('\n')
        print(f'Expenses for {i}')
        grand_monthly_total = grand_total(monthly_totals)
        #Print out the totals for each month
        print_totals(monthly_totals, grand_monthly_total)
        print('\n')


        #Reset values in monthly total to 0
        for key in monthly_totals:
            monthly_totals[key] = 0
        #Set the values for the monthly totals to 0 each iteration here
    print(f'This is the yearly totals for {summary_year}')
    grand_yearly_total = grand_total(yearly_totals)
    print_totals(yearly_totals, grand_yearly_total)



for i in range(len(actions)):
    print(str(i) + ': ' + actions[i])

user_action = int(input('\nWhat action will you like to take: '))



if user_action == 0:
    record_purchase()

if user_action == 1:
    print_summary()


