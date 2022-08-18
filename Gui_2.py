from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd

root= Tk()

root['background']='#6CD99E'
root.title('Minor Project')
root.geometry('500x400')
root.iconbitmap(r'C:\Users\user\Documents\pic.ico')   # Here 'r' is written before path because single backward slash is used in path and python 3 gives error for single backward slash in path. So either use double backward slash in path or write 'r' before path. 

def plot():
    df=pd.read_csv('2022-05-11.csv')

    time=df['Time']

    temp=df['Temperature']

    plt.plot(time, temp)
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Temperature Vs Time Plot')
    plt.show()
    
blank1=Label(root, text='                                                                                   ', bg='#6CD99E')
blank1.grid(row=0, column=0)

college_name=Label(root, text='Shri Ramdeobaba college of Engineering and Management', font=("Varela Round", 25))
college_name.grid(row=0, column=1, padx=0, pady=10)

blank2=Label(root, text=' ', bg='#6CD99E')
blank2.grid(row=1, column=0)

dept=Label(root, text='Department of Electrical Engineering', font=("Varela Round", 25))
dept.grid(row=1, column=1, padx=0, pady=10)

blank3=Label(root, text=' ', bg='#6CD99E')
blank3.grid(row=2, column=0)

topic=Label(root, text='Real Time Temperature Sensing', font=("Varela Round", 25))
topic.grid(row=2, column=1, padx=0, pady=10)

blank4=Label(root, text=' ', bg='#6CD99E')
blank4.grid(row=3, column=0)

plot_button=Button(root, text='Plot', font=('Varela Round', 12), bg='#2F6E4C', command=plot)
plot_button.grid(row=3, column=1, padx=5, pady=5)

blank5=Label(root, text=' ', bg='#6CD99E')
blank5.grid(row=4, column=0)

quit_button=Button(root, text='Quit', font=('Varela Round', 12), bg='#2F6E4C', command=root.destroy)
quit_button.grid(row=4, column=1, padx=5, pady=5)


root.mainloop()
