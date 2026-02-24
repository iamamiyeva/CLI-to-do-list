# CLI-to-do-list

Simple command line task manager written in Python.

This project allows users to create and manage tasks directly from the terminal. It was built to practice core Python fundamentals such as lists, dictionaries, loops, and input validation.

Current Features:
 - Add task
 - List tasks
 - Delete task by ID
 - Priority selection
 - Tag system

In Progress:
 - Mark task as done
 - Filter by tag
 - Task statistics
 - Optional JSON file saving

Task Structure:

Each task is stored as a dictionary:

{

    "ID": int,
    
    "Title": str,
    
    "Done": bool,
    
    "Priority": str,
    
    
    "Tags": list
}

Purpose:

  This project is part of my learning process while improving my Python programming skills.
