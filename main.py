from gui import GUI
gui = GUI()                         # Generating GUI instance
root = gui.create_main_window()     # generate main window for user
gui.create_main_frame(root)         # generate the initial frame in main window
root.mainloop()
