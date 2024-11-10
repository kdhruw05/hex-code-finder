from tkinter import Tk, Label, Button, filedialog, Canvas
from PIL import Image, ImageTk

class HexCodeFinder:
    def __init__(self, master):
        self.master = master
        self.master.title("Hex Code Finder")
        
        self.label = Label(master, text="Upload an image to find hex codes of pixels.")
        self.label.pack()
        
        self.upload_button = Button(master, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()
        
        self.canvas = Canvas(master)
        self.canvas.pack()
        
        self.hex_code_label = Label(master, text="")
        self.hex_code_label.pack()
        
        self.image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.image.thumbnail((800, 600))  # Resize image to fit within the canvas
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas.config(width=self.tk_image.width(), height=self.tk_image.height())
            self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)
            self.canvas.bind("<Button-1>", self.get_hex_code)
            self.hex_code_label.config(text="Click on the image to get the hex code of the pixel.")
            print(f"Image loaded: {file_path}")  # Debugging information

    def get_hex_code(self, event):
        if self.image is None:
            return
        x, y = event.x, event.y
        print(f"Clicked at: ({x}, {y})")  # Debugging information
        rgb = self.image.getpixel((x, y))
        hex_code = '#{:02x}{:02x}{:02x}'.format(*rgb)
        self.hex_code_label.config(text=f"Hex Code: {hex_code}")
        print(f"Hex Code: {hex_code}")  # Debugging information

if __name__ == "__main__":
    root = Tk()
    app = HexCodeFinder(root)
    root.mainloop()
