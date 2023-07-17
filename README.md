This python program allows you to easily input purchases that you made that day, or previously, and saves all the information into a dedicated csv file for that month and year.

In the future I would like to implement a way to print out all the purchases by category with the $ amount and %, as well as the description. As of now the purchase description only lives in the csv file and does not get printed out. It could help in the future to be able to easily go back and print out all the purchases within a certain category with their descriptions instead of opening the csv file and trying to find it manually. Though I do not do this often, so it is something I have not implemented yet.
<br/>
#### Some of the features are:
- Choose options easily by selecting from outputted list
- Creates new folder and file for month and year if data does not exist yet
- Inputs todays date automatically if purchase was made today
- Allows you to input multiple purchases without restarting the program
- Prints out an easy to read summary with spending breakdown by month, with categories in $ amounts and in %, as well as monthly totals and a yearly total for each category
<br/>
#### Print Summary
The ability to print a summary is the main thing that I was looking for in a simple personal finance program. This way I can easily see what type of purchases my money is going to month by month and I can adjust accordingly.
<br/>
#### Record Purchase
The process to input data is very easy, the program starts asking if you want to record purchase, or print summary. Input the number that corresponds with the option you want to select and click enter. 

Next it will ask if the purchase was made today, if it was input "yes" - this will take the local date from your computer as a value, if not you will need to input the date in YYY/MM/DD format on the next line.

After the date you need to input the total price of the purchase, and then select the type of purchase it was using the corresponding number from the output on the next line. Then you will be able to give a short description as to what the purchase was.

Finally you can choose to record another purchase or not, selecting yes will loop through the program again, no will close the program.
<br>
#### CSV Saved Data

The program saves all the data in separate folders for each year and separate files for each month. CSV files have the file name format as: 01_january_2023.csv
