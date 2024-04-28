import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# The second window
def openNewWindow():
    orderSystem = Toplevel(root)
    
    orderSystem.title("Ordering System")
    
    orderSystem.geometry("1920x1080")
    
    label = tk.Label(orderSystem, text="Chinese Food Ordering System", font=('Georgia', 18))
    label.pack(padx=20, pady=20)

    # Increase and Decrease calculations
    def increase(var):
        var.set(var.get()+1)
    
    def decrease(var):
        if var.get() > 0:
            var.set(var.get() - 1)
    
    def Close(window): 
        window.destroy() 
  

    #Frame for orange chicken
    frame1 = Frame(orderSystem)
    frame1.pack(padx=10, pady=20)
    
    # Loads the orange chicken image
    image1 = Image.open("orange_chicken.jpg")
    image1.thumbnail((300, 300))
    photo1 = ImageTk.PhotoImage(image1)
    image_label1 = tk.Label(frame1, image=photo1)
    image_label1.image = photo1
    image_label1.pack()
    
    # Increase and Decrease buttons for orange chicken
    number1 = IntVar()
    button1_increase = Button(frame1, text="Increase", command=lambda: increase(number1))
    button1_increase.pack(pady=5)  
    button1_decrease = Button(frame1, text="Decrease", command=lambda: decrease(number1))
    button1_decrease.pack(pady=5)  
    label1 = Label(frame1, textvariable=number1)
    label1.pack(pady=5)  


     # Frame for the sweet sour pork
    frame2 = Frame(orderSystem)
    frame2.pack(padx=20, pady=20)


    # Loads the sweet sour pork image
    image2 = Image.open("sweet_sour_pork.jpg")
    image2.thumbnail((300, 300))
    photo2 = ImageTk.PhotoImage(image2)
    image_label2 = tk.Label(frame2, image=photo2)
    image_label2.image = photo2
    image_label2.pack()
    
    # Increase and Decrease buttons for sweet sour pork
    number2 = IntVar()
    button2_increase = Button(frame2, text="Increase", command=lambda: increase(number2))
    button2_increase.pack(pady=5)  
    button2_decrease = Button(frame2, text="Decrease", command=lambda: decrease(number2))
    button2_decrease.pack(pady=5) 
    label2 = Label(frame2, textvariable=number2)
    label2.pack(pady=5)  

    exit_button = Button(orderSystem, text="Exit", command=lambda: Close(orderSystem))
    exit_button.pack(pady=50)
  

# The main home page
root = tk.Tk()

root.geometry("1920x1080")
root.title("Chinese Food Home Page")

label = tk.Label(root, text="Chinese Restaurant Home", font=('Georgia', 18))
label.pack(padx=20, pady=20)
# Button to open the second window
button = tk.Button(root, text="Order Here!", font=("Georgia", 18), command=openNewWindow)
button.pack(padx=100, pady= 100)

exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=50)
root.mainloop()