# 📅 Walla Walla Event Manager

A Python-based event management application built using a **microservices architecture**, enabling users to create, manage, and interact with local events.

## 🚀 Overview

Developed a modular system that separates core functionality into independent services, improving scalability, maintainability, and code organization.

## 💡 Key Features

- Event creation with **holiday validation**
- View and delete user-specific events
- Event-based **forum system** for user interaction
- Job board for posting and claiming event-related tasks

## 🏗️ Architecture & Design

- Designed and implemented **4 independent microservices**:
  - `Holiday.py` – Date validation (holiday detection)
  - `Delete.py` – Event retrieval and deletion
  - `Forum.py` – Comment system for events
  - `JobList.py` – Job posting and assignment system  

- **Loose coupling**:
  - No direct imports between services
  - All communication handled through the main application

- Emphasizes:
  - Separation of concerns  
  - Modular design  
  - Real-world backend architecture concepts  

## 🛠️ Tech Stack

- Python  
- Microservices architecture  
- File-based persistence (text files)  
- Subprocess-based service communication  


## ▶️ Running the Project

```
bash
git clone https://github.com/Garciajaime/event-manager-microservices.git
cd event-manager-microservices
# In sepereate terminals
python Holiday.py
python Delete.py
python Forum.py
python JobList.py
python main.py
```

## 🎥 Demo

Includes a video walkthrough demonstrating full system functionality and architecture.

## 📈 Key Takeaways

- Applied microservices principles in a standalone application
- Built a complete CRUD-based system with multiple interacting components
- Structured code to reflect real-world backend design patterns

## 👨‍💻 Author

Abraham Garcia  
Computer Science Student 
