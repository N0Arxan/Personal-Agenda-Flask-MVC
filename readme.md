
# Flask MVC Project

Welcome to the **Flask MVC Personal-Agenda**! This project follows the Model-View-Controller (MVC) architecture and is designed for rapid development with Flask and MongoDB (Atlas) and has basic user auhtentication.

---

## ✨ Getting Started

Before you start using the project, please make sure to complete the following steps.

### 1. Configuration

Update the `config.py` file with your own settings. Open `config.py` and change the values accordingly:

```python
class Config:
    # Flask settings
    SECRET_KEY = 'YOUR_SECRET_KEY'  # Replace with your unique secret key

    # MongoDB (Atlas) settings
    MONGO_URI = 'MONGO_URI'    # Replace with your MongoDB URI
    DATABASE = 'DATABASE_NAME'        # Replace with your database name
```

---

### 2. Setup Virtual Environment and Install Dependencies

It is recommended to create a virtual environment to manage your project dependencies. Open your terminal and run:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

Once the dependencies are installed, you can run the project with:

```bash
python run.py
```

---

### 3. Database Queries & Sample Data

Inside the root folder, you will find a folder named `db-queries` which contains useful scripts:

- **sample_data.py**: This script loads sample data into your database. Use it to populate your database with initial data for testing or development.
- **trigger.js**: This JavaScript file is a template for setting up a trigger on the MongoDB Atlas dashboard. Customize it as needed for your project requirements.

---

## 🚀 Running the Project

After completing the steps above, simply run:

```bash
python run.py
```

Your Flask application should now be up and running. Open your browser and navigate to `http://localhost:5000` (or your specified port) to see your project in action!

---

## 📚 Project Structure

Here is an overview of the main project structure:

```
.
├── src/                 # Application package (models, views, controllers)
├── config.py            # Configuration file for Flask and MongoDB settings
├── db-queries/          # Folder for database query scripts and triggers
│   ├── sample_data.py   # Script for loading sample data
│   └── trigger.js       # Script for creating a MongoDB Atlas trigger
├── requirements.txt     # List of dependencies
└── run.py               # Entry point to run the project
```

---

## 💡 Customization & Further Development

- **Secret Key**: Make sure your `SECRET_KEY` in `config.py` is kept secret. You can generate a new one using Python’s `os.urandom(24)`.
- **MongoDB**: Replace the placeholder values with your actual MongoDB Atlas connection string and database name.
- **Triggers**: Customize the `trigger.js` file according to the triggers you want to create on the MongoDB Atlas dashboard.

---

## 🙏 Contributing

Contributions are welcome! Please fork the repository, create a new branch for your feature or bugfix, and submit a pull request.

---

## 🔗 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy coding! 🚀
