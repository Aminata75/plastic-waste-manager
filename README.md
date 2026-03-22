# ♻️Plastic Waste Manager

## 📌Overview

Plastic Waste Manager is a full-stack web application built with Python and Flask that allows users to track, manage, and analyze recyclable plastic items. The application provides an intuitive interface for managing inventory while offering insights into recycling impact.


## 🚀Features

	•	Add, view, update and delete plastic items (CRUD functionality)
	•	Track plastic types (PET, HDPE, PVC, etc.)
	•	Display recyclability levels with visual indicators (🟢🟠🔴)
	•	View statistics:
	⁃	Total items
	⁃	Size distribution
	⁃	Average size
	⁃	Estimated CO₂ savings 🌍
	•	Persistent data storage using JSON


## 🛠Technologies Used

	•	Backend: Python, Flask
	•	Frontend: HTML, CSS, Jinja2
	•	Data Storage: JSON


## 🧠Key Concepts

	•	Object Oriented Programming (OOP)
	•	Separation of concerns (backend vs frontend)
	•	Dynamic rendering using Flask templates
	•	Form handling and user input validation


## ⚙️How to Run the Application

	1. Clone the repository:

		•	git clone <your-repo-link>
		•	cd plastic-waste-manager

	2. Install dependencies:

		•	pip install flask

	3. Run the application:

		•	python app.py

	4. Open in browser:

		•	http://127.0.0.1:5000/



## 📂Project Structure

	├ app.py 
	├ main.py 
	├ PlasticWasteManager.py 
	├ UI_helper.py 
	├ utils.py 
	├ inventory.json 
	├ templates/ 
	├ static/ 
	┕ .gitignore 


## ⚠️ Challenges & Solutions

One of the main challenges was transitioning from a command line to a web-based application. Initially, functions relied on print statements, which are not suitable for web applications. This was resolved by refactoring the logic to return data instead, allowing Flask to render it dynamically in HTML templates.


## 🌍Future Improvements

	•	Add data visualization (charts📊)
	•	Implement database storage (SQLite)
	•	Add authentication system
	•	Deploy the application online


## 👩🏾‍💻Author

Aminata Dibassy, as part of a Python Full-Stack Bootcamp project. 

