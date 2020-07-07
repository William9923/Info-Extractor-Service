import apps 

if __name__ == "__main__":
    app = apps.create_app()
    app.run(debug=True, port=3000)