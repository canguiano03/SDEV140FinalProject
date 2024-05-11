import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
# Creates the root window
root = tk.Tk()

# Menu Items dict
menuItems =[{ 
            
        "name": "Orange Chicken",
        "price": "9.99",
        "image": "orange_chicken.jpg",
        "orders": IntVar(value=0) # Sets the orders to zero

    },
{ 
    "name": "Sweet and Sour Pork",
    "price": "12.99",
    "image": "sweet_sour_pork.jpg",
    "orders": IntVar(value=0) # Sets the orders to zero

}
]

# Creates the second window to order food
def openNewWindow():
    orderSystem = Toplevel(root) 
    
    orderSystem.title("Ordering System") # Title for second window
    
    orderSystem.geometry("1920x1080") # Size of the second window
    # Title that displays in the window
    label = tk.Label(orderSystem, text="Chinese Food Ordering System", font=('Georgia', 18))
    label.pack(padx=20, pady=20)

    # Increase calculation for amount of food items
    def increase(var, item):
        var.set(var.get() + 1)
        item["orders"].set(var.get())
     # Decrease calculation for amount of food items
    def decrease(var, item):
         if var.get() > 0:
            var.set(var.get() - 1)
            item["orders"].set(var.get())
    # Closes the ordering system window
    def Close(window): 
        window.destroy() 

    # Loop for all current and future food items to display on second window
    for item in menuItems:
        frame = Frame(orderSystem)  # Frames for menu items
        frame.pack(padx=10, pady=20) # Padding for menu images

        # Label for name and price of the menu items
        text_label = tk.Label(frame, text="{}: ${:.2f}".format(item['name'], float(item['price'])), font=('Georgia', 16)) 
        text_label.pack() # Pack for name and prices of menu items

        # Loads the image for each menu item
        image = Image.open(item['image']) # Opens images
        image.thumbnail((300, 300)) # Sizes the images
        photo = ImageTk.PhotoImage(image) # Creates PhotoImage from images
        image_label = tk.Label(frame, image=photo) # Label for images
        image_label.image = photo # Ensure image is not being garbage collected
        image_label.pack() # Incase image needs modified

        # Stores the orders variable
        number = IntVar()
        number.set(item["orders"].get()) # Ensures that the orders variable is 0
        # Button to increase amount of menu item
        button_increase = Button(frame, text="Increase", command=lambda num=number, itm=item: increase(num, itm))
        button_increase.pack(pady=5) # Padding for increase button
        # Button to decrease amount of menu item
        button_decrease = Button(frame, text="Decrease", command=lambda num=number, itm=item: decrease(num, itm))
        button_decrease.pack(pady=5) # Padding for decrease button
        label = Label(frame, textvariable=number) # Displays the amount of each menu item
        label.pack(pady=5) # Padding for amount of each menu item
    
    # This is the food calculation for total cost
    def calculateTotalCost():

        totalCost = 0 # Stores the total cost and starts it at 0
        # Loops through all menu items
        for item in menuItems:
            orders = item["orders"].get() # Gets the amount of orders
            price = float(item["price"]) # Gets the price of the menu items
            cost = orders * price # Calculates the cost of the menu items by multiplying the amount by the price
            totalCost += cost # Ensures that the totalCost and cost are the same
        tax = totalCost * 0.07 # Calculates the tax for the totalCost with a 7% sales tax
        totalCostTax = totalCost + tax # Calculates the total cost by combining it with the tax
        print("Total Cost:", totalCostTax) # Prints the totalcostTax variable
        outcome_lable.config(text=f"Total Cost: ${totalCostTax:.2f}") # Displays the total cost tax rounded to the nearest hundredth

    # Button to initate the calculation of the total cost
    calculate_cost_button = Button(orderSystem, text="Calculate Total Cost", command=calculateTotalCost)
    calculate_cost_button.pack() # Calculate Total Cost button pack
    # Displays the total price of the food
    outcome_lable=tk.Label(orderSystem, text="", font=("Georgia", 20, "bold"))
    outcome_lable.pack(pady=50) # Padding for the display of total price
    # Exit button
    exit_button = Button(orderSystem, text="Exit", command=lambda: Close(orderSystem))
    exit_button.pack() # Pack for exit button

# The main home page

root.geometry("1920x1080") # Size of the root window
root.title("Chinese Food Home Page") # Title for the root window

# Title that displays in the home window
label = tk.Label(root, text="Chinese Restaurant Home", font=('Georgia', 18))
label.pack(padx=20, pady=20) # Padding for title

# Frame for dragon image
frame3 = Frame(root)
frame3.pack(padx=20, pady=20) # Padding for frame3
# Dragon image
image3 = Image.open("dragon.jpg") # Opens the dragon image
image3.thumbnail((300, 300)) # Size of dragon image
photo3 = ImageTk.PhotoImage(image3) # Creates PhotoImage from image3
image_label3 = tk.Label(frame3, image=photo3) # Label for dragon image
image_label3.image = photo3 # Ensure image is not being garbage collected
image_label3.pack() # Pack for image 3

# Button to open the second window
button = tk.Button(root, text="Order Here!", font=("Georgia", 18), command=openNewWindow) # Order Here button that takes user to ordering window
button.pack(padx=50, pady= 50) # Order here Button padding
# Exits out of the GUI
exit_button = Button(root, text="Exit", command=root.destroy) # Exit button 
exit_button.pack(pady=50) # Exit button padding
root.mainloop()