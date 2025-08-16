import tkinter as tk
from tkinter import ttk
import threading
import time
import keyboard
import pyautogui

class BotController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bot Contrôleur")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Variables
        self.is_running = False
        self.bot_thread = None
        
        # Configuration de pyautogui
        pyautogui.FAILSAFE = False
        
        self.setup_ui()
        self.setup_hotkeys()
        
    def setup_ui(self):
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Titre
        title_label = ttk.Label(main_frame, text="Bot Contrôleur", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Instructions
        instructions = """
        Fonctionnalités:
        • Maintient la touche A enfoncée
        • Spam la touche Z en continu
        • Appuyez sur P pour arrêter le bot
        """
        
        instructions_label = ttk.Label(main_frame, text=instructions, justify=tk.LEFT)
        instructions_label.grid(row=1, column=0, columnspan=2, pady=(0, 20), sticky=tk.W)
        
        # Bouton Start/Stop
        self.start_button = ttk.Button(main_frame, text="Démarrer Bot", command=self.toggle_bot)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=(0, 20))
        
        # Status
        self.status_label = ttk.Label(main_frame, text="Status: Arrêté", font=("Arial", 10))
        self.status_label.grid(row=3, column=0, columnspan=2, pady=(0, 10))
        
        # Indicateur visuel
        self.status_indicator = tk.Canvas(main_frame, width=20, height=20, bg='white', highlightthickness=1)
        self.status_indicator.grid(row=4, column=0, columnspan=2)
        self.status_indicator.create_oval(5, 5, 15, 15, fill='red', tags='indicator')
        
        # Bouton Quitter
        quit_button = ttk.Button(main_frame, text="Quitter", command=self.quit_app)
        quit_button.grid(row=5, column=0, columnspan=2, pady=(20, 0))
        
    def setup_hotkeys(self):
        # Raccourci clavier pour arrêter le bot
        keyboard.add_hotkey('p', self.stop_bot)
        
    def toggle_bot(self):
        if not self.is_running:
            self.start_bot()
        else:
            self.stop_bot()
            
    def start_bot(self):
        if not self.is_running:
            self.is_running = True
            self.bot_thread = threading.Thread(target=self.bot_loop, daemon=True)
            self.bot_thread.start()
            
            self.start_button.config(text="Arrêter Bot")
            self.status_label.config(text="Status: En cours d'exécution")
            self.status_indicator.itemconfig('indicator', fill='green')
            
    def stop_bot(self):
        if self.is_running:
            self.is_running = False
            if self.bot_thread and self.bot_thread.is_alive():
                self.bot_thread.join(timeout=1)
                
            self.start_button.config(text="Démarrer Bot")
            self.status_label.config(text="Status: Arrêté")
            self.status_indicator.itemconfig('indicator', fill='red')
            
    def bot_loop(self):
        try:
            while self.is_running:
                # Maintenir la touche A enfoncée en continu
                pyautogui.keyDown('a')
                
                # Spam la touche Z plusieurs fois
                for _ in range(10):  # Spam Z 10 fois avant de relancer A
                    if not self.is_running:
                        break
                    pyautogui.press('z')
                    time.sleep(0.1)  # Délai entre chaque appui sur Z
                
        except Exception as e:
            print(f"Erreur dans le bot: {e}")
        finally:
            # Relâcher la touche A quand le bot s'arrête
            try:
                pyautogui.keyUp('a')
            except:
                pass
            
    def quit_app(self):
        self.stop_bot()
        self.root.quit()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BotController()
    app.run()
