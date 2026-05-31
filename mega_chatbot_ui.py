import subprocess
import ollama
import tkinter as tk
import customtkinter as ctk  # Modernized UI Library

# Configuration
MODEL_NAME = "huihui_ai/qwen3.5-abliterated:2b"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AresAI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window Setup
        self.title("Security Analysis Lab")
        self.geometry("900x700")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Initialize History
        self.history = [
            {
                "role": "system",
                "content": "You are a Security Analyst. Categorize logs as INFO, WARNING, or CRITICAL before answering."
            }
        ]

        # --- UI ELEMENTS ---
        # Chat Box (Tkinter Text instead of CTkTextbox for bold support)
        self.chat_box = tk.Text(
            self, 
            font=("Segoe UI", 12), 
            bg="#1e1e1e", 
            fg="#e6e6e6", 
            wrap="word"
        )
        self.chat_box.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Configure bold tag
        self.chat_box.tag_configure("bold", font=("Segoe UI", 12, "bold"))

        # Input Frame
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        self.entry = ctk.CTkEntry(
            self.input_frame, 
            placeholder_text="Ask about your system logs or network traffic...", 
            height=40, 
            font=("Segoe UI", 12)
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.entry.bind("<Return>", lambda e: self.run_chat())

        self.btn = ctk.CTkButton(
            self.input_frame, 
            text="Ask", 
            command=self.run_chat, 
            width=120, 
            height=40, 
            font=("Segoe UI Semibold", 12)
        )
        self.btn.pack(side="right")

        # Save Button
        self.save_btn = ctk.CTkButton(
            self, 
            text="Save Chat", 
            command=self.save_chat, 
            width=120, 
            height=35, 
            font=("Segoe UI Semibold", 12)
        )
        self.save_btn.grid(row=2, column=0, pady=10)

    # --- LOGIC LAYER ---
    def load_logs(self):
        try:
            with open("system_logs.txt", "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "LOG ERROR: system_logs.txt missing."

    def get_network_info(self):
        try:
            result = subprocess.run(["netstat", "-ano"], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f"NET ERROR: {e}"

    def insert_with_format(self, text):
        """Parse text and insert bold where ** markers are used."""
        parts = text.split("**")
        for i, part in enumerate(parts):
            if i % 2 == 1:  # Odd index = bold section
                self.chat_box.insert("end", part, "bold")
            else:
                self.chat_box.insert("end", part)

    def run_chat(self):
        user_input = self.entry.get()
        if not user_input.strip():
            return
        
        self.entry.delete(0, "end")

        # Right-aligned user bubble
        self.chat_box.insert("end", f"\n{' ' * 40}🟦 USER > {user_input}\n")

        logs = self.load_logs()
        network = self.get_network_info()
        
        context = f"LOGS: {logs[:1500]}\nNETWORK: {network[:1500]}"
        self.history.append({"role": "user", "content": f"DATA: {context}\n\nPROMPT: {user_input}"})
        
        try:
            response = ollama.chat(model=MODEL_NAME, messages=self.history)
            answer = response['message']['content']
            self.history.append({"role": "assistant", "content": answer})
            
            # AI response with bold formatting
            self.chat_box.insert("end", "\n\n🟩 AI > ")
            self.insert_with_format(answer)
            self.chat_box.insert("end", "\n")
            self.chat_box.insert("end", "========================================\n")
            self.chat_box.see("end")

            self.auto_save_history(user_input, answer)
        except Exception as e:
            self.chat_box.insert("end", f"SYSTEM ERROR: {e}\n")

    def auto_save_history(self, user_input, answer):
        try:
            with open("chat_history.txt", "a", encoding="utf-8") as f:
                f.write(f"USER: {user_input}\n")
                f.write(f"AI: {answer}\n")
                f.write("========================================\n\n")
        except Exception as e:
            self.chat_box.insert("end", f"SAVE ERROR: {e}\n")

    def save_chat(self):
        try:
            with open("chat_history.txt", "a", encoding="utf-8") as f:
                f.write("\n=== Full Chat Export ===\n")
                f.write(self.chat_box.get("1.0", "end"))
                f.write("\n=== End of Export ===\n\n")
            self.chat_box.insert("end", "\n✅ Chat history appended to chat_history.txt\n")
        except Exception as e:
            self.chat_box.insert("end", f"SAVE ERROR: {e}\n")

if __name__ == "__main__":
    app = AresAI()
    app.mainloop()
