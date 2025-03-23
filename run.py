from src import StartUp

app = StartUp.create_app()

if __name__ == '__main__':
    app.run(debug=True)