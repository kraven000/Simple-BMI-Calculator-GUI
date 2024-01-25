from tkinter import*
import tkinter.messagebox as msg

def process():
    try:
        float_weight = float(weight.get())
        float_height = float(height.get())
        bmi = round(float_weight/float_height**2)
        
        del float_height
        del float_weight
        
        classificaton = None
        if bmi<18:
            classificaton = "Underweight"
        elif bmi>=18 and bmi<25:
            classificaton = "Normal"
        elif bmi>=25 and bmi<30:
            classificaton = "Overweight"
        elif bmi>=30:
            classificaton = "Obese"

        msg.showinfo(title="Your BMI",message=f"Your BMI IS:- {bmi}.\n{classificaton}.")
    except:
        msg.showerror(title="Error",message="Please Input Your Height or Weight")


root = Tk()
root.geometry("600x150")
root.maxsize(600,150)
icon = PhotoImage(file="icon.png")
root.iconphoto(True,icon)
root.title("BMI CALCULATOR")

# Taking Height
Label(root,text="Enter Your Height in (meters):- ",font="Aerial 14 bold",padx=0).place(x=0,y=1)

height = StringVar()
Entry(root,textvariable=height,borderwidth=0).place(x=380,y=1)


# Taking Weight
Label(root,text="Enter Your Weight in (kilograms):- ",font="Aerial 14 bold",padx=0).place(x=0,y=30)

weight = StringVar()
Entry(root,textvariable=weight,borderwidth=0).place(x=380,y=30)


# Making Submit Button
Button(root,text="SUBMIT!!!",borderwidth=0,font="Aerial 8 bold",border=1,command=process).place(x=0,y=60)

Button(root,text="Exit!!",borderwidth=0,font="Aerial 8 bold",border=1,command=exit).place(x=100,y=60)


root.mainloop()