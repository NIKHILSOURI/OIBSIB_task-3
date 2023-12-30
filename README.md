# OIBSIB_task-3
1. **Class Definition (`PasswordGenerator`):**
   - The class represents a password generator application.
   - It initializes the Tkinter root window and sets the window title to "Password Generator."
   - Instance variables (`length_var`, `include_upper_var`, `include_lower_var`, `include_digits_var`, `include_symbols_var`) are created to manage user preferences for password generation.

2. **User Interface Setup Function (`setup_ui`):**
   - This function defines and configures the Tkinter widgets for the GUI.
   - It includes labels, entry fields, checkbuttons, and buttons for password length, character type preferences (uppercase, lowercase, digits, symbols), and password generation/copying actions.
   - The widgets are organized in a grid layout within the Tkinter window.

3. **Password Generation Function (`generate_password`):**
   - This function is triggered when the user clicks the "Generate Password" button.
   - It constructs a character set based on the user's preferences (uppercase, lowercase, digits, symbols).
   - If no character set is selected, a warning message is displayed.
   - Otherwise, a password of the specified length is generated and shown in a pop-up dialog.

4. **Copy to Clipboard Function (`copy_to_clipboard`):**
   - This function is triggered when the user clicks the "Copy to Clipboard" button.
   - It attempts to retrieve the currently generated password from the clipboard using the `pyperclip` library.
   - If a password is found in the clipboard, it is copied back to the clipboard, and a success message is displayed. If no password is found, a warning is shown.

5. **Main Execution Block (`if __name__ == "__main__":):**
   - The main block creates an instance of the Tkinter root window (`root`), and the `PasswordGenerator` class is instantiated with this root window.
   - The Tkinter `mainloop` is then called to start the GUI event loop, allowing the user to interact with the application.
