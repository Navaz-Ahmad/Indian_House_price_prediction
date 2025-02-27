

# Indian House Price Prediction

Indian House Price Prediction is a machine learning web application that estimates property prices across India based on various features such as area, number of bedrooms, location, and available amenities. The project is built using Python, Flask, and XGBoost, and is deployed on Heroku.

## Features

- **Real-time Predictions:**  
  Users can input property details via a user-friendly web interface and receive immediate price estimates.
  
- **Intuitive UI:**  
  The application uses HTML and CSS to provide a clear and consistent design, including dropdown menus for selecting cities and locations.

- **End-to-End Pipeline:**  
  The project covers data preprocessing, model training, and deployment, demonstrating a complete machine learning workflow.

## Project Structure

```
project/
├── deployment/
│   └── app.py          # Flask application that serves the web interface and API
├── models/
│   └── lgb_model.pkl   # Saved XGBoost model for house price prediction
├── templates/
│   └── index.html      # HTML template(s) for the web interface
├── requirements.txt    # Python dependencies required for the project
└── Procfile            # Defines the web process for Heroku deployment
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/indian-house-price-prediction.git
   cd indian-house-price-prediction
   ```

2. **Create a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application Locally

1. **Start the Flask App:**

   ```bash
   python deployment/app.py
   ```

2. **Access the Application:**  
   Open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

3. **Use the Interface:**  
   Enter property details in the form and click "Predict" to get the estimated house price.

## Deployment on Heroku

1. **Create a Procfile:**  
   Ensure that the `Procfile` in your repository contains the following line:
   
   ```
   web: gunicorn deployment.app:app
   ```

2. **Commit Your Changes:**

   ```bash
   git add .
   git commit -m "Prepare project for Heroku deployment"
   ```

3. **Create a Heroku App and Deploy:**

   - Log in to Heroku:
   
     ```bash
     heroku login
     ```
   
   - Create a new app:
   
     ```bash
     heroku create your-app-name
     ```
   
   - Push your code to Heroku:
   
     ```bash
     git push heroku master
     ```
     (If your branch is named `main`, use `git push heroku main`)

4. **Open Your Deployed App:**  
   Once the deployment is complete, run:
   
   ```bash
   heroku open
   ```

## Technologies Used

- **Python:** Core programming language.
- **Flask:** Web framework for building the API and web interface.
- **XGBoost:** Machine learning library used for training the prediction model.
- **pandas & numpy:** Data processing and numerical computations.
- **Gunicorn:** Production WSGI server for Heroku deployment.
- **Heroku:** Cloud platform used for hosting the application.
- **Git & GitHub:** Version control and code hosting.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Thanks to the contributors of the libraries and tools used in this project.
- Special thanks to the GitHub Student Developer Pack for providing additional resources for deployment.



