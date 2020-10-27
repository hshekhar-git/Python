

#This python program converts input given in HH:MM:SS to Seconds

import tkinter as tk 
import tkinter.messagebox

root = tk.Tk()

root.title('Time Clock')

def convert():
    """ This function converts the time entered by the user in the hh:mm:ss
        to seconds format. """

    hour_input = int(hours_entry.get())

    min_input = int(minutes_entry.get())

    sec_input = int(seconds_entry.get())

    hours = hour_input * 60
    mins = min_input * 60

    seconds= hours+mins+sec_input   
    
    tkinter.messagebox.showinfo('Conversion Result',
                                " Time in second is {}".format(seconds))







main_window = tkinter.Tk()

top_frame = tkinter.Frame()
bottom_frame = tkinter.Frame()

title_label = tkinter.Label(top_frame, text='Time Converter for Seconds to '
                                            'hh:mm:ss')

#hours entry                                            
hours_label = tkinter.Label(top_frame, text=' Enter hours: ')
hours_entry = tkinter.Entry(top_frame, width=10)
title_label.pack(side='top')
hours_label.pack(side='left')
hours_entry.pack(side='left')

#minutes entry
minutes_label = tkinter.Label(top_frame, text=' Enter minutes: ')
minutes_entry = tkinter.Entry(top_frame, width=10)
title_label.pack(side='top')
minutes_label.pack(side='left')
minutes_entry.pack(side='left')

#seconds entry
seconds_label = tkinter.Label(top_frame, text=' Enter seconds: ')
seconds_entry = tkinter.Entry(top_frame, width=10)
title_label.pack(side='top')
seconds_label.pack(side='left')
seconds_entry.pack(side='left')


#Button Settings
convert_button = tkinter.Button(bottom_frame,
                                text='Convert Seconds',
                                command=convert)
quit_button = tkinter.Button(bottom_frame,
                             text='Quit',
                             command=main_window.destroy)


convert_button.pack(padx=0, side='left')
quit_button.pack(padx=0, side='left')

top_frame.pack()
bottom_frame.pack()

tkinter.mainloop()
