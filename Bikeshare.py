import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

import CoreCalculations as cc
def main():
    #window
    root = tk.Tk()
    root.title("Bike Share Project")

    #City label
    Label2 = tk.Label(text='City')
    Label2.grid(row=0, column=0, sticky='w')

    #Chicago checkbox
    Checkbutton1 = tk.Checkbutton()
    Checkbutton1.grid(column=0, row=2, sticky='w')
    chicago_checkbutton1_var = tk.BooleanVar()
    Checkbutton1.configure(variable=chicago_checkbutton1_var)
    Checkbutton1.configure(text='Chicago')

    #New York checkbox
    Checkbutton2 = tk.Checkbutton(text='New York')
    Checkbutton2.grid(column=0, row=3, sticky='w')
    NY_checkbutton2_var = tk.BooleanVar()
    Checkbutton2.configure(variable=NY_checkbutton2_var)

    #Washington checkbox
    Checkbutton3 = tk.Checkbutton()
    Checkbutton3.grid(column=0, row=4, sticky='w')
    washington_checkbutton3_var = tk.BooleanVar()
    Checkbutton3.configure(variable=washington_checkbutton3_var) #onvalue = 1 by default
    Checkbutton3.configure(text='Washington')

    # month label
    Label_month = tk.Label()
    Label_month.grid(column=0, row=5, sticky='w')
    Label_month.configure(text='Month')

    # months checkboxes
    checkboxes_months = []
    months = ['Select All','January', 'February', 'March', 'April', 'May', 'June']
    #event handler for months checkboxes
    checkboxes_months_variables = []
    def deselect_select_all_months():
        for i in range(1,7):
            if checkboxes_months_variables[i].get() == False:  # deselected item
                checkboxes_months[0].deselect()
    for i, item in enumerate(months):
        checkboxes_months.append(tk.Checkbutton(text=item))
        checkboxes_months[i].grid(column=0, row=6+i, sticky='w')#.pack(side='top', column=0)#.place(x=300, y=i*25+50, height=25)
        checkboxes_months_variables.append(tk.BooleanVar())
        checkboxes_months[i].configure(variable=checkboxes_months_variables[i])
        if i > 0: #not the Select all checkbox
            checkboxes_months_variables[i].trace_add("write", lambda *args: deselect_select_all_months())
    def select_all_months():
        if checkboxes_months_variables[0].get(): # is checked
            for i, item in enumerate(checkboxes_months):
                checkboxes_months[i].select()#item.select()


    #select all months event handler
    checkboxes_months_variables[0].trace_add("write",lambda *args:select_all_months())

    # day name label
    Label_day_name = tk.Label(text='Day name')
    Label_day_name.grid(column=0, row=13, sticky='w')

    # day names checkboxes
    day_names = ['Select All', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    checkboxes_day_names = []

    #event handler for day names checkboxes
    checkboxes_days_variables = []
    def deselect_select_all_days():
        for i in range(1,8):
            if checkboxes_days_variables[i].get() == False:  # deselected item
                checkboxes_day_names[0].deselect()
    for i, item in enumerate(day_names):
        checkboxes_day_names.append(tk.Checkbutton(text=item))
        checkboxes_day_names[i].grid(column=0, row=14+i, sticky='w')#.pack(side='top', column=0)#.place(x=300, y=i*25+50, height=25)
        checkboxes_days_variables.append(tk.BooleanVar())
        checkboxes_day_names[i].configure(variable=checkboxes_days_variables[i])
        if i > 0: #not the Select all checkbox
            checkboxes_days_variables[i].trace_add("write", lambda *args: deselect_select_all_days())
    def select_all_days():
        if checkboxes_days_variables[0].get(): # is checked
            for i, item in enumerate(checkboxes_day_names):
                checkboxes_day_names[i].select()#item.select()

    checkboxes_days_variables[0].trace_add("write", lambda *args: select_all_days())

    # day label
    Label_day_number = tk.Label(text="Day numbers")
    Label_day_number.grid(column=0, row=22, sticky='w')#.pack(side='top', column=0)#.place(x=650, y=50, height=25)

    # days checkboxes
    Entry_day_numbers = tk.Entry()
    Entry_day_numbers.grid(column=0, row=23, sticky='w')
    Label_hint_days = tk.Label(text="Enter day numbers from 1 to 31, separated by commas, eg.:3, 4, 5; \n or range, eg.: 15-30; or * if you want all days")
    Label_hint_days.grid(column=0, row=24, sticky='w')

    #hour label
    Label_hour = tk.Label(text='Hours:')
    Label_hour.grid(column=0, row=25, sticky='w')

    #hour Entry
    Entry_hours = tk.Entry()
    Entry_hours.grid(column=0, row=26, sticky='w')
    Label_hint_hours = tk.Label(
        text="Enter hour numbers from 0 to 23, separated by commas, eg.:3, 4, 5;\n or range, eg.: 0-11; or * if you want all hours of the day")
    Label_hint_hours.grid(column=0, row=27, sticky='w')

    # find label
    Label3 = tk.Label()
    Label3.grid(column=1, row=0, sticky='w')#.pack(side='top', column=0)#.place(x=20, y=300, height=25, width=34) #y+=25
    Label3.configure(text='Find')

    #broad options combobox
    combobox1_var = tk.StringVar()
    TCombobox1 = tk.OptionMenu(root, combobox1_var, 'Popular times of travel', 'Popular stations and trip', 'Trip duration', 'User info')
    TCombobox1.grid(column=2, row=0, sticky='w')
    def load_combobox_2_according_to_combobox_1():
        #empty combobox 2 from previous values
        combobox2_var.set('')

        #get the selected item from the broad options combobox
        x = combobox1_var.get()
        if x == 'Popular times of travel':
            combobox2_values = ['Most common month in the first 6 months in 2017', 'Most common day of week',
                                              'Most common hour of day', 'Most common day in the first 6 months in 2017']
        elif x == 'Popular stations and trip':
            combobox2_values=['Most common start station', 'Most common end station', 'Most common trip from start to end']
        elif x == 'Trip duration':
            combobox2_values=['Total travel time', 'Average travel time', 'Minimum travel time trip', 'Maximum travel time trip',
                        'Standard deviation of travel time']
        elif x == 'User info':
            #added for any city
            combobox2_values=['Compare statistically between Subscribers and Customers']
            #added for New York or Chicago only
            if NY_checkbutton2_var.get()==1 or chicago_checkbutton1_var.get()==1:  # values.append --> needs review  & what if the user checked Washington and NYC or Chicago? would you bring the statistics of only one of them? would you give a user a hint about this?
                 combobox2_values.append('Compare statistically between Males and Females')
                 combobox2_values.append('Youngest users')
                 combobox2_values.append('Oldest users')
                 combobox2_values.append('Common (Mode) age of users')
                 combobox2_values.append('Average age of users')
                 combobox2_values.append('Median of ages')

        #refresh combobox 2 with the appropriate menu: it actually creates a new OptionMenu at the same place
        Combobox2 = tk.OptionMenu(root, combobox2_var, *combobox2_values)
        Combobox2.grid(column=2, row=2, sticky='w')
    combobox1_var.trace_add("write",lambda *args:load_combobox_2_according_to_combobox_1()) # event handler whenever the user changes the selected item

    # Specifically label
    Label4 = tk.Label(text='Specifically')
    Label4.grid(column=1, row=2, sticky='w')

    #fine options combobox
    combobox2_var = tk.StringVar()
    Combobox2 = tk.OptionMenu(root, combobox2_var, value=[])#will fill later
    Combobox2.grid(column=2, row=2, sticky='w')

    def button_filter_event_handler():#(chicago, NY, washington, months, day_names, day_numbers, hours):
        if ((not chicago_checkbutton1_var.get()) and (not NY_checkbutton2_var.get())) and (not washington_checkbutton3_var.get()):
            tk.messagebox.showerror(title='Bikeshare Project', message='Please check at least one city')
        else:
            data = cc.load_data(chicago_checkbutton1_var.get(), NY_checkbutton2_var.get(), washington_checkbutton3_var.get())
            #filter by months
            if checkboxes_months_variables[0].get()==False: # select all is not checked else if select all is checked, the data needn't to be filtered
                checked_months = []
                for i, item in enumerate(checkboxes_months_variables):
                    if item.get() == 1: #checked
                        checked_months.append(i)
                if(len(checked_months)>0):
                    data = cc.filter_by_months(data, *checked_months)
                else:
                    tk.messagebox.showerror('Bikeshare Project', 'Please check at least one month')
                    return None

            #filter by day names
            if checkboxes_days_variables[0].get()==False: # select all is not checked else no need to be filtered
                checked_day_names = []
                for i, item in enumerate(checkboxes_days_variables):
                    if item.get() == 1:  # checked
                        checked_day_names.append(day_names[i])
                if(len(checked_day_names)>0):
                    data = cc.filter_by_days_in_week(data, *checked_day_names)
                else:
                    tk.messagebox.showerror('Bikeshare Project', 'Please check at least one day name')
                    return None

            #filter by day numbers
            entered_string_days = Entry_day_numbers.get()
            error = False
            may_be_error = False
            numbers_list = []
            if not entered_string_days == '*':
                if entered_string_days.isnumeric():
                    data = cc.filter_by_days_in_month(data, int(entered_string_days))
                else:
                    numbers = entered_string_days.split(',')
                    for number in numbers:
                        if not number.isnumeric():#may be error, or may be a range
                            may_be_error = True
                            break
                    if not may_be_error: # all numbers are numeric
                        # better add a check here on the range of the numbers entered
                        data = cc.filter_by_days_in_month(data, *numbers)
                    else: # check if it is a range not error
                        range_string = entered_string_days.split('-')
                        if not len(range_string) == 2:
                            error = True
                        elif range_string[0].isnumeric and range_string[1].isnumeric and int(range_string[1])>=int(range_string[0]) and int(range_string[0])>0 and int(range_string[1])<32:
                            #fill the array that is going to be sent to filter by day numbers function
                            for i in range(int(range_string[0]), int(range_string[1])+1):#+1 to include the second value in the range
                                numbers_list.append(i)
                            data = cc.filter_by_days_in_month(data, *numbers_list)
                        else:
                            error = True
                    if error:
                        tk.messagebox.showerror('Bikeshare Project', 'Enter day numbers from 1 to 31, separated by commas, \neg.:3, 4, 5\nor range, eg.: 15-30\nor * if you want all days')
                        return None
            #filter by hours
            entered_string_hours = Entry_hours.get()
            error = False
            may_be_error = False
            numbers_list = []
            if not entered_string_hours == '*':
                if entered_string_hours.isnumeric():
                    data = cc.filter_by_hour(data, int(entered_string_hours))
                else:
                    numbers = entered_string_hours.split(',')
                    for number in numbers:
                        if not number.isnumeric():  # may be error, or may be a range
                            may_be_error = True
                            break
                    if not may_be_error:  # all numbers are numeric
                        #better add a check here on the range of the numbers entered
                        data = cc.filter_by_hour(data, *numbers)
                    else:  # check if it is a range not error
                        range_string = entered_string_hours.split('-')
                        if not len(range_string) == 2:
                            error = True
                        elif range_string[0].isnumeric and range_string[1].isnumeric and int(range_string[1]) >= int(range_string[0]) and int(range_string[0])>=0 and int(range_string[1])<24:
                            # fill the array that is going to be sent to filter by day numbers function
                            for i in range(int(range_string[0]),
                                           int(range_string[1]) + 1):  # +1 to include the second value in the range
                                numbers_list.append(i)
                            data = cc.filter_by_hour(data, *numbers_list)
                        else:
                            error = True
                    if error:
                        tk.messagebox.showerror('Bikeshare Project',
                                                'Enter hour numbers from 0 to 23, separated by commas, \neg.:3, 4, 5\nor range, eg.: 15-23\nor * if you want all hours in a day')
                        return None
        selected_fine_option = combobox2_var.get()
        if data.empty:
            Text_filtered_data.insert(tk.INSERT, 'Returned data after selected filters is empty\n')
            return None
        my_text = ''
        if selected_fine_option == 'Most common month in the first 6 months in 2017':
            my_text = 'The most common month users make trips, according to the selected filters, is: '+str(cc.max_month(data))
        elif selected_fine_option == 'Most common day of week':
            my_text = 'The most common day name users make trips, according to the selected filters, is:'+str(cc.max_day_week(data))
        elif selected_fine_option == 'Most common hour of day':
            my_text = 'The most common hour of a day users make trips, according to the selected filters, is:'+str(cc.max_hour_day(data))
        elif selected_fine_option == 'Most common day in the first 6 months in 2017':
            my_text = 'The date when maximum number of users made trips, according to the selected filters, is:'+str(cc.max_date(data))
        elif selected_fine_option == 'Most common start station':
            my_text = 'According to the selected filters, users mostly start their trips from '+cc.max_start_station(data)
        elif selected_fine_option == 'Most common end station':
            my_text = 'According to the selected filters, users mostly end their trips to '+ cc.max_end_station(data)
        elif selected_fine_option == 'Most common trip from start to end':
            my_text = 'According to the selected filters, the most common trip is: '+cc.common_trip(data)
        elif selected_fine_option == 'Total travel time':
            seconds = cc.total_travel_time(data)
            my_text = 'According to the selected filters, the total travel time of all trips is '+ str(seconds) +' seconds.\nThis is equal to '+str(seconds/60)+ ' minutes.\nThis is equal to '+str(seconds/(60*60))+' hours.'
        elif selected_fine_option == 'Average travel time':
            seconds = cc.average_travel_time(data)
            my_text = 'According to the selected filters, the average time of trips is '+ str(seconds)+' seconds.\nThis is equal to '+str(seconds/60)+ ' minutes.\nThis is equal to '+str(seconds/(60*60))+' hours.'
        elif selected_fine_option == 'Minimum travel time trip':
            my_text = 'According to the selected filters, the fastest trip took only '+str(cc.min_travel_time_trip(data))+' seconds.'
        elif selected_fine_option == 'Maximum travel time trip':
            seconds = cc.max_travel_time_trip(data)
            my_text = 'According to the selected filters, the slowest trip took '+str(seconds)+' seconds.\nThis is equal to '+str(seconds/60)+ ' minutes.\nThis is equal to '+str(seconds/(60*60))+' hours.'
        elif selected_fine_option == 'Standard deviation of travel time':
            my_text = 'According to the selected filters, the standard deviation of duration of trips is '+str(cc.standard_deviation_of_travel_time(data))
        elif selected_fine_option == 'Compare statistically between Subscribers and Customers':
            my_text = cc.compare_subscribers_customers(data)
        elif selected_fine_option == 'Compare statistically between Males and Females':
            my_text = cc.compare_female_males(data)
        elif selected_fine_option == 'Youngest users':
            my_text = 'According to the selected filters, the youngest age of users is '+str(cc.youngest_users(data))+ ' years old.'
        elif selected_fine_option == 'Oldest users':
            my_text = 'According to the selected filters, the youngest age of users is '+str(cc.oldest_users(data))+ ' years old.'
        elif selected_fine_option == 'Common (Mode) age of users':
            my_text = 'According to the selected filters, the most common age of users is '+str(cc.mode_age(data))
        elif selected_fine_option == 'Average age of users':
            my_text = 'According to the selected filters, the average age of users is '+str(cc.average_age(data))
        elif selected_fine_option == 'Median of ages':
            median = cc.median_age(data)
            my_text = 'According to the selected filters, the number of users whose age is above '+str(median)+ ' is equal to the number of users whose age is umder '+str(median)

        Text_filtered_data.insert(tk.INSERT, '\n')
        Text_filtered_data.insert(tk.INSERT, my_text)
        Text_filtered_data.insert(tk.INSERT, '\n')
        yes = tk.messagebox.askyesno(title='Show filtered raw data?', message='Show next 5 rows in the filtered data?')
        next_five = 0
        x = data.count()[0]
        while(yes and x/5 > next_five):
            if x/5 - next_five < 5: #last 5
                Text_filtered_data.insert(tk.INSERT, data[next_five*5:])
                Text_filtered_data.insert(tk.INSERT, '\n')
            Text_filtered_data.insert(tk.INSERT, data[next_five*5:next_five*5 + 5])
            next_five+=1
            yes = tk.messagebox.askyesno(title='Show filtered raw data?', message='Show next 5 rows in the filtered data?')

    #Filter Button
    Button_filter = tk.Button()
    Button_filter.configure(text="Filter!", command=button_filter_event_handler)
    #notice that the there is no () in command, don't call the function
    Button_filter.grid(column=1, row=3, sticky='w')

    # filtered data
    Text_filtered_data = tk.scrolledtext.ScrolledText(wrap= tk.WORD) #make the whole word together
    Text_filtered_data.grid(columnspan=2, rowspan=33, row=4, column=1, sticky='e')

    tk.mainloop()

if __name__ == '__main__':
    main()

