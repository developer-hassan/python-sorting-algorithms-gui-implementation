# Sorting Algorithms Implementation Using Python GUI

## Introduction

This project is being developed to implement different sorting algorithms (i.e., Insertion sort, Heap Sort, Quick Sort, Counting Sort) to analyze their working structure and to test their running time differences. It is also using a python GUI using tkinter framework to better visualize the inputs and results. Using tkinter, a UI is developed which will take necessary inputs about the array to be sorted and will then generate the array based on those inputs. As a result, the sorted array will be displayed along with the time taken by the sorting algorithm (chosen by the user) to sort that array. Our generation system can work with different input sizes.

## Tools and Technologies

* Visual Studio Code, as a code editor
* Python, as a high-level programming language
* Tkinter, as a framework for GUI implementation

## Project Division

The whole project is divided into 4 portions:

* Generator Portion which contains the code related to random array generation.
* Sorter portion which contains the complete implementation of all four sorting algorithms
* GUI portion which merges the functionality of the above two portions as well as contains the code for the whole front end of the project.
* Main Portion which calls the instances for all other portions.

## Main Features

This project comprises of the following features:

* Random array generation of user defined sizes, between min and max parameter specified by user so you don’t have to type 10,000 elements
* Sorting in 4 different algorithms – Insertion Sort, Heap Sort, Quick Sort, and Counting Sort
* Ability to track the time taken for sorting by different algorithms Helps in analyzing and comparing the algorithms performance
* Input validation and error checking
