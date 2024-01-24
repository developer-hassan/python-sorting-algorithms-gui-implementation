import tkinter as tk
from tkinter import ttk
from datetime import datetime
from generator import Generator
from sorter import Sorter

class GUI:
    '''
    Front-end of application
    '''

    def __init__(self) -> None:
        '''
        Constructor to initialize attributes
        '''

        # UI elements
        self.__heading_font = ("Arial", 20, "bold")
        self.__subheading_font = ("Arial", 16, "bold")
        self.__size_placeholder = "e.g. 500"
        self.__lower_placeholder = "e.g. 20"
        self.__upper_placeholder = "e.g. 100"
        self.__main_window_color = "#7a6548"
        self.__frame_bg_color = "#a3947e"
        self.__lbl_btn_bg_color = "#634726"

        # Desktop Application widgets
        self.__array_size = None
        self.__lower_bound = None
        self.__upper_bound = None
        self.__generate_array_btn = None
        self.__generated_array = None
        self.__algorithm_selection = None
        self.__go_btn = None
        self.__result_frame = None
        self.__sorted_array = None
        self.__running_time = None

    '''
    Different private events
    '''

    def __create_frame(self, master: tk.Misc, width: int, bg: str, thickness: int) -> tk.Frame:
        '''
        Creates the frame with some general attibutes
        '''
        return tk.Frame(master, width=width, highlightbackground=bg, highlightthickness=thickness)

    def __validate_enteries(self, user_input: str):
        '''
        Validates the content of entries to prevent non-numeric digit to be entered in the entry.
        '''
        # It passes if the text-box contains the placeholders
        if user_input in [self.__size_placeholder, self.__upper_placeholder, self.__lower_placeholder]:
            return True

        if len(user_input) != 0:
            # Allows the input if it is a digit
            return user_input.isdigit()
        # Allows the empty text-box
        return True

    def __remove_placeholder(self, entry: tk.Entry):
        '''
        Removes the placeholder from entry and sets the text to black
        '''
        # changes the text color to black
        entry.configure(fg="black")
        try:
            # Checks Whether the text-box text is convertable to integer
            int(entry.get())
        except:
            # If not then it will clear the text_box
            entry.delete(0, tk.END)

    def __apply_placeholder(self, entry: tk.Entry, placeholder: str):
        '''
        Applies the placeholder to entry and sets text color to grey
        '''
        # If entry is empty
        if entry.get() == '':

            # Set it to gray, remove any text and add the placeholder
            entry.configure(fg="grey")
            entry.insert(0, placeholder)

    def __reset(self):
        '''
        Resets the input enteries and destroys the result frame
        '''
        # Does not reset if the result frame is not yet created
        if self.__result_frame is None:
            return

        # Destroys the result frame
        self.__result_frame.destroy()

        # Clears the data in array size entry box and applies placeholder
        self.__array_size.delete(0, tk.END)
        self.__apply_placeholder(self.__array_size, self.__size_placeholder)

        # Clears the data in lower bound entry box and applies placeholder
        self.__lower_bound.delete(0, tk.END)
        self.__apply_placeholder(self.__lower_bound, self.__lower_placeholder)

        # Clears the data in upper bound entry box and applies placeholder
        self.__upper_bound.delete(0, tk.END)
        self.__apply_placeholder(self.__upper_bound, self.__upper_placeholder)

        # Clears the previous generated array
        self.__generated_array.delete(0, tk.END)

        # Clears the reference of frame
        self.__result_frame = None

    def __create_result_frame(self, root: tk.Misc):
        '''
        Private method that creates the frame once the GO Button is clicked
        '''
        # does not create frame if it is already created
        if self.__result_frame is not None:
            return

        # Creates the place the result frame
        self.__result_frame = self.__create_frame(
            root, 1350, self.__frame_bg_color, 3)
        self.__result_frame.grid(
            row=1, column=0, padx=50, pady=0, ipadx=30, ipady=150)
        self.__result_frame.configure(bg=self.__frame_bg_color)

        # creates and positions the Heading label of Result Area
        select_algorithm = tk.Label(self.__result_frame,
                                    text="Displaying the Result",
                                    font=self.__heading_font,
                                    bg=self.__lbl_btn_bg_color,
                                    width=30,
                                    padx=10,
                                    pady=10,
                                    )
        select_algorithm.place(x=450, y=10)

        # Label for the sorted array
        sorted_array_lbl = tk.Label(self.__result_frame,
                                    text="Sorted Array",
                                    font=self.__subheading_font,
                                    bg=self.__lbl_btn_bg_color,
                                    width=13)
        sorted_array_lbl.place(x=10, y=80)

        # Text-box that will display the sorted array
        self.__sorted_array = tk.Entry(self.__result_frame,
                                       width=110,
                                       borderwidth=5,
                                       font=self.__subheading_font)
        self.__sorted_array.place(x=10, y=110)

        # Label for the running-time
        runing_time_lbl = tk.Label(self.__result_frame,
                                   text="Running Time",
                                   font=self.__subheading_font,
                                   bg=self.__lbl_btn_bg_color,
                                   width=13)
        runing_time_lbl.place(x=10, y=180)

        # Text-box that will display the running-time
        self.__running_time = tk.Entry(self.__result_frame,
                                       width=40,
                                       borderwidth=5,
                                       font=self.__subheading_font)
        self.__running_time.place(x=10, y=210)

        # Creates the button which clears the current states of inputs and results
        self.__generate_reset_button(root)

    def __generate_array(self):
        '''
        Takes the array parameters from the text-boxes and use Generator's method
        to generate an array and display it in generated array text-box.
        '''
        if self.__array_size.get() == self.__size_placeholder or self.__lower_bound.get() == self.__lower_placeholder or self.__upper_bound.get() == self.__upper_placeholder:
            return

        # taking parameters for array generation
        size = int(self.__array_size.get())
        low = int(self.__lower_bound.get())
        up = int(self.__upper_bound.get())

        # do not create array if the lower bound is greater than upper bound
        if low > up:
            self.__generated_array.insert(0, "Array cannot be generated")
            return

        # call Generator's method to generate array with upper parameters
        array = Generator.create_random_array(size, low, up)

        # Clears the previous content and fill the entry with random generated array
        self.__generated_array.delete(0, tk.END)
        self.__generated_array.insert(0, array)

    def __generate_result(self, root):
        '''
        Creates the result frame and applies the selected algorithm to sort the input array
        '''
        if self.__generated_array.get() == '':
            return

        # creates the result frame
        self.__create_result_frame(root)

        # applies the selected algorithm
        self.__apply_algorithm()

    def __generate_reset_button(self, root):
        reset_button = tk.Button(root,
                                 text="Reset",
                                 bg=self.__lbl_btn_bg_color,
                                 font=self.__subheading_font,
                                 command=self.__reset,
                                 width=10)
        reset_button.place(x=1320, y=750)

    def __apply_algorithm(self):
        '''
        Applies the user selected algorithm to sort the array and displays it's running time.
        '''
        # takes the name of algorithm from text box
        algorithm = self.__algorithm_selection.get()

        # clears the previous data in resulting text-boxes
        self.__sorted_array.delete(0, tk.END)
        self.__running_time.delete(0, tk.END)

        # Creates the integer array from string to apply sorting algorithm
        array_from_string = self.__generated_array.get().split(' ')
        integer_array = []

        for string_number in array_from_string:
            integer_array.append(int(string_number))

        start_time = datetime.now()

        try:
            # If user selects the insertion sort, then its algorithm is called and time is saved
            if algorithm == "Insertion Sort":
                answer = Sorter.insertion_sort(integer_array)

            # If user selects the heap sort, then its algorithm is called and time is saved
            elif algorithm == "Heap Sort":
                answer = Sorter.heap_sort(integer_array)

            # If user selects the quick sort, then its algorithm is called and time is saved
            elif algorithm == "Quick Sort":
                answer = Sorter.quick_sort(integer_array)

            # If user selects the counting sort, then its algorithm is called and time is saved
            else:
                answer = Sorter.counting_sort(integer_array)

            end_time = datetime.now()

            # storing the running time
            time_taken = end_time - start_time

            # fill the entries with running time and sorted array
            self.__running_time.insert(0, time_taken)
            self.__sorted_array.insert(0, answer)

        except:
            self.__running_time.insert(0, "Not Calculated")
            self.__sorted_array.insert(
                0, "Error! Sorting cannot be performed...")

    '''
    Public methods
    '''

    def create_main_frame(self, root: tk.Misc):
        '''
        Creates the main frame in the start of program
        '''

        # Creating and positioning the frame
        frame = self.__create_frame(root, 1350, self.__frame_bg_color, 3)
        frame.grid(row=0, column=0, padx=50, pady=30, ipadx=30, ipady=190)
        frame.configure(bg=self.__frame_bg_color)

        # Generating the title label
        title_label = tk.Label(frame,
                               text="Sorting Algorithms Implementation",
                               font=self.__heading_font,
                               bg=self.__lbl_btn_bg_color,
                               pady=15,
                               padx=15,
                               width=30
                               )
        title_label.place(x=450, y=10)

        # Label for the array size
        array_size_lbl = tk.Label(frame,
                                  text="Enter the array size: ",
                                  font=self.__subheading_font)
        array_size_lbl.place(x=10, y=100)

        # Text-box in which user input the array size
        self.__array_size = tk.Entry(frame,
                                     width=40,
                                     borderwidth=5,
                                     font=self.__subheading_font)
        self.__array_size.place(x=280, y=100)

        # The placeholder will be removed when user focuses on array size entry
        self.__array_size.bind(
            "<FocusIn>",
            lambda event, entry=self.__array_size: self.__remove_placeholder(entry))
        # The placeholder will be applied when user leaves focus on array size entry without adding size
        self.__array_size.bind(
            "<FocusOut>",
            lambda event, entry=self.__array_size, placeholder=self.__size_placeholder: self.__apply_placeholder(entry, placeholder))

        # Label for lower bound
        min_num_lbl = tk.Label(frame,
                               text="Enter the lower bound: ",
                               font=self.__subheading_font)
        min_num_lbl.place(x=10, y=150)

        # Text-box in which user input the lower bound
        self.__lower_bound = tk.Entry(frame,
                                      width=40,
                                      borderwidth=5,
                                      font=self.__subheading_font)
        self.__lower_bound.place(x=280, y=150)

        # The placeholder will be removed when user focuses on lower bound entry
        self.__lower_bound.bind(
            "<FocusIn>",
            lambda event, entry=self.__lower_bound: self.__remove_placeholder(entry))
        # The placeholder will be applied when user leaves focus on lower bound entry without adding lower bound
        self.__lower_bound.bind(
            "<FocusOut>",
            lambda event, entry=self.__lower_bound, placeholder=self.__lower_placeholder: self.__apply_placeholder(entry, placeholder))

        # Label for upper-bound
        max_num_lbl = tk.Label(frame,
                               text="Enter the upper bound: ",
                               font=self.__subheading_font)
        max_num_lbl.place(x=10, y=200)

        # Text-box in which user input the upper bound
        self.__upper_bound = tk.Entry(frame,
                                      width=40,
                                      borderwidth=5,
                                      font=self.__subheading_font)
        self.__upper_bound.place(x=280, y=200)

        # The placeholder will be removed when user focuses on upper bound entry
        self.__upper_bound.bind(
            "<FocusIn>",
            lambda event, entry=self.__upper_bound: self.__remove_placeholder(entry))

        # The placeholder will be applied when user leaves focus on upper bound entry without adding upper bound
        self.__upper_bound.bind(
            "<FocusOut>",
            lambda event, entry=self.__upper_bound, placeholder=self.__upper_placeholder: self.__apply_placeholder(entry, placeholder))

        # it restricts the non-numeric values to be entered
        registered = root.register(self.__validate_enteries)

        # all the input labels are validated
        self.__array_size.config(
            validate="key", validatecommand=(registered, '%P'))
        self.__lower_bound.config(
            validate="key", validatecommand=(registered, '%P'))
        self.__upper_bound.config(
            validate="key", validatecommand=(registered, '%P'))

        # Apply the placeholder initially on all input entries
        self.__apply_placeholder(self.__array_size, self.__size_placeholder)
        self.__apply_placeholder(self.__lower_bound, self.__lower_placeholder)
        self.__apply_placeholder(self.__upper_bound, self.__upper_placeholder)

        # Button that will generate the random array when clicked
        self.__generate_array_btn = tk.Button(frame,
                                              text="Generate Array",
                                              bg=self.__lbl_btn_bg_color,
                                              font=self.__subheading_font,
                                              width=15,
                                              command=self.__generate_array)
        self.__generate_array_btn.place(x=800, y=150)

        # Label for Generated Array
        generated_lbl = tk.Label(frame,
                                 text="Generated Array",
                                 font=self.__subheading_font,
                                 bg=self.__lbl_btn_bg_color,
                                 width=13,
                                 anchor=tk.W)
        generated_lbl.place(x=10, y=250)

        # Text-box that will display the generated array
        self.__generated_array = tk.Entry(frame,
                                          width=110,
                                          borderwidth=5,
                                          font=self.__subheading_font)
        self.__generated_array.place(x=10, y=280)

        # Label for sorting algorithm selection
        select_algorithm = tk.Label(frame,
                                    text="Select the Sorting Algorithm",
                                    font=self.__subheading_font
                                    )
        select_algorithm.place(x=10, y=330)

        # List that stores the sorting algorithms
        sorting_algorithms = [
            "Insertion Sort",
            "Heap Sort",
            "Quick Sort",
            "Counting Sort"
        ]

        # A combobox that displays the list of algorithms
        self.__algorithm_selection = ttk.Combobox(frame,
                                                  value=sorting_algorithms,
                                                  width=30,
                                                  font=self.__heading_font)
        self.__algorithm_selection.place(x=320, y=328)

        # Initially selects the first item of Combobox
        self.__algorithm_selection.current(0)

        # Button that displays the result of inputted values when created
        self.__go_btn = tk.Button(frame,
                                  text="Go",
                                  bg=self.__lbl_btn_bg_color,
                                  font=self.__subheading_font,
                                  command=lambda root=root: self.__generate_result(
                                      root),
                                  width=15)
        self.__go_btn.place(x=800, y=325)

    def create_main_window(self):
        '''
        Public method for creating a main window
        '''
        # create and returns the main window with following specifications
        root = tk.Tk()
        root.geometry("1920x1024")
        root.title("Project")
        root.iconbitmap("d:/Courses/tkinter/icons/one.ico")
        root.minsize(1920, 1024)
        root.configure(bg=self.__main_window_color)
        return root
