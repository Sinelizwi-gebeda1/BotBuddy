import customtkinter as ctk
import threading
import time
import subprocess  # Import subprocess to launch the login script
from PIL import Image, ImageTk

class SplashScreen(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Cartoonify Splash Screen")
        
        # Set the window to full-screen mode
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        
        # Set up the splash screen background color
        self.configure(fg_color="white")
        
        # Create a frame that fills the screen
        self.bg_frame = ctk.CTkFrame(self, fg_color="white")
        self.bg_frame.pack(fill="both", expand=True)
        
        # Load the image to be used as the background
        self.bg_image = Image.open("ai.png")  # Path to your image file
        self.bg_image = self.bg_image.resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.Resampling.LANCZOS)  # Resize to fit the screen
        
        # Convert the image to a format tkinter can display
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        
        # Create a label to display the image as background
        self.bg_label = ctk.CTkLabel(self.bg_frame, image=self.bg_image_tk)
        self.bg_label.place(relwidth=1, relheight=1)  # Make the label fill the entire frame
        
        # Start the transition to the login screen after a delay (no progress bar)
        self.after(3000, self.open_login_screen)  # Change the time delay as needed

    def open_login_screen(self):
        self.destroy()  # Destroy the splash screen
        # Use subprocess to open the login.py script
        subprocess.Popen(["python", "main.py"])  # Run the login script in a new process

if __name__ == "__main__":
    app = SplashScreen()
    app.mainloop()
