# Importing tkinter and random modules 
from tkinter import *
import random 

# creating a simple window using Tk()
window = Tk() 

# setting the background of window 
window.configure(bg="aqua") 

# Setting length vs breadth of the window above created
window.geometry("600x600") 

# setting the title of window
window.title("Dice Simulator") 

 
c = Canvas(window, width=600, height=600,bg='aqua')
c.pack()
# Creating function to roll the dices 
def roll_dices(): 
	# These values indicate dots on the dices. 
	# For eg: \u2680 corresponds to 1 dot, 
	# \u2681 corresponds to 2 dots etc. 
    
	dice_dots = ['\u2680', '\u2681', 
				'\u2682', '\u2683', 
				'\u2684', '\u2685'] 
	# Generating random dots on the dices 
	label.configure( 
		text=f'{random.choice(dice_dots)}{random.choice(dice_dots)}') 
   
	label.pack() 


# create a button for window
button = Button(window, text="Roll!", 
					width=10, height=2, 
					font=15, bg="aqua", 
					bd=2) 
button.configure(command=roll_dices)
# Setting the position of the button 
button.pack(padx=10, pady=10) 
label2 = Label(window, text='Not rolled yet', font=('Times',20,'bold'),bg='purple',fg='yellow',width=12)
c.create_window(40, 50, window=label2)

label3 = Label(window, text='Winning rule: The player wins if he/she gets a sum of perfect 12 on rolling 2 dice within 6 rolls', font=('Times',12,'bold'),fg='white',bg="green")
c.create_window( 50,22,window=label3)
# # Adding Label 
label = Label(window, font=("times", 250), 
			bg="aqua", fg="purple") 

window.mainloop() 
