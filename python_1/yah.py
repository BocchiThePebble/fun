import tkinter as tk
import time
import threading



class CookieClickerGame:
    def __init__(self, root):
        # Game variables
        self.cookies = 0
        #this is the code that shows you how many cookies you have so you can know if your able to buy something
        self.cookies_per_click = 1
        #this is the code that actually makes you cookies 
        self.cookies_per_second = 0
        self.cursors = 0
        self.grandmas = 0
        self.clicks = 0
        self.achievements = []
        self.clicks_per_second = 0
        self.click_count = 0

        # Prices for upgrades
        self.cursor_price = 15
        self.grandma_price = 100

        # Achievement thresholds
        self.achievement_thresholds = {
            'First Click!': 1,
            'Fifty Clicks!': 50,
            'One Hundred Cookies!': 100,
            'One Thousand Cookies!': 1000
        }

        # Setup the GUI
        self.root = root
        root.title("Cookie Clicker")
        root.geometry("400x500")

        # Cookie counter display
        self.cookie_display = tk.Label(root, text=f"Cookies: {self.cookies}", font=('Arial', 16))
        self.cookie_display.pack()

        # Cookies per second display
        self.cps_display = tk.Label(root, text=f"Cookies per Second: {self.cookies_per_second}", font=('Arial', 12))
        self.cps_display.pack()

        # Clicks per second display
        self.clicks_per_second_display = tk.Label(root, text=f"Clicks per Second: {self.clicks_per_second}", font=('Arial', 12), fg='green')
        self.clicks_per_second_display.pack()

        # Achievements display
        self.achievement_display = tk.Label(root, text="Achievements: None", font=('Arial', 10), fg='blue')
        self.achievement_display.pack()

        # Cookie click button
        self.cookie_button = tk.Button(root, text="Click Me!", font=('Arial', 20), command=self.click_cookie)
        self.cookie_button.pack(pady=20)

        # Upgrade buttons
        self.cursor_button = tk.Button(root, text="Buy Cursor (15 cookies)", command=self.purchase_cursor)
        self.cursor_button.pack()

        self.grandma_button = tk.Button(root, text="Buy Grandma (100 cookies)", command=self.purchase_grandma)
        self.grandma_button.pack()

        # Start threads for cookie generation and CPS calculation
        threading.Thread(target=self.generate_cookies, daemon=True).start()
        threading.Thread(target=self.calculate_clicks_per_second, daemon=True).start()

    def click_cookie(self):
        self.cookies += self.cookies_per_click
        self.clicks += 1
        self.click_count += 1  # Count each click for CPS
        self.update_display()
        self.check_achievements()

    def purchase_cursor(self):
        if self.cookies >= self.cursor_price:
            self.cookies -= self.cursor_price
            self.cursors += 1
            self.cookies_per_second += 1
            self.update_display()

    def purchase_grandma(self):
        if self.cookies >= self.grandma_price:
            self.cookies -= self.grandma_price
            self.grandmas += 1
            self.cookies_per_second += 5
            self.update_display()
# this functins updates display in the user interface 
    def update_display(self):
        self.cookie_display.config(text=f"Cookies: {self.cookies}")
        self.cps_display.config(text=f"Cookies per Second: {self.cookies_per_second}")
        self.clicks_per_second_display.config(text=f"Clicks per Second: {self.clicks_per_second}")
        self.achievement_display.config(text=f"Achievements: {', '.join(self.achievements) or 'None'}")

    def check_achievements(self):
        for achievement, threshold in self.achievement_thresholds.items():
            if achievement not in self.achievements and (
                    (achievement == 'First Click!' and self.clicks >= threshold) or
                    (self.cookies >= threshold)):
                self.achievements.append(achievement)

    def generate_cookies(self):
        while True:
            time.sleep(1)
            self.cookies += self.cookies_per_second
            self.update_display()

    def calculate_clicks_per_second(self):
        while True:
            time.sleep(1)
            self.clicks_per_second = self.click_count
            self.click_count = 0  # Reset for the next second
            self.update_display()

# Run the game
root = tk.Tk()
app = CookieClickerGame(root)
root.mainloop()
