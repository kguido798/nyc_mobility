NYC Mobility Dashboard

React, Flask, MySQL, and Chart.js have been utilized well in this full-stack data analytics platform to look into and see cab transportation data in New York City.

Team: Devnote
Rene Guido Kayigamba
Elijah Kabatsi 
Nyirihirwe Yves 

Project Description

By reviewing and analyzing taxi travel data, Mobility Dashboard is used  to offer insights into NYC transportation trends. The system is actually using an interactive web dashboard to fetch, store, process, and nicely show the mobility data.
This application allows the clients to:
View statistics on transportation
See the travel patterns
Track the number of trips
Analyse the patterns of taxi mobility
See the interactive charts to visualize data.
Objectives
This project's main goals are:
Make use of a relational database to keep and manage NYC taxi trip data.
Give users access to data via RESTful APIs.
To use dashboards to see trends in transportation
Clearview of your full-stack web development skills..
Actually use data analytics ways on actual datasets.
Features
Dashboard Analytics
Total trips overview
Trip trend visualization
Statistical summaries
Interactive charts
Backend Services
REST API endpoints
Database connectivity
Data aggregation
Error handling
Data Visualization
Chart.js integration
Responsive charts
Real-time API data loading
Database Management
MySQL database integration
Large dataset handling
Query optimization
Technology Stack
Frontend
React
Vite
Chart.js
React Chart.js 2
Backend
Flask
Python
Database
MySQL
System Architecture
Frontend (React + Vite)
          |
          v
Backend API (Flask)
          |
          v
MySQL Database
          |
          v
NYC Taxi Dataset
Dataset
The project uses NYC Taxi Trip Records containing:
Pickup locations
Dropoff locations
Trip distances
Fare amounts
Passenger counts
Trip durations
Example dataset:
yellow_tripdata_2025-01.parquet
Installation Guide
1. Clone Repository
git clone https://github.com/kguido798/nyc_mobility.git
cd nyc_mobility

2. Backend Setup
Create virtual environment:
python -m venv venv

Activate environment:
Windows:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run Flask server:
python app.py

Backend URL:
http://127.0.0.1:5000
3. Frontend Setup
Navigate to frontend folder:
cd nyc_mobility
cd frontend

Install dependencies:
npm install

Start development server:
npm run dev

Frontend URL:
http://localhost:5173
API Endpoints
Health Check
GET /api/health

Response:
{
  "status": "healthy"
}
Trips Endpoint
GET /api/trips

It will return trip records from the database.
Statistics Endpoint
GET /api/stats

Returns summarized transportation statistics.
For more information check the screenshots folder
Running the Application
Start backend:
cd backend
python app.py

Start frontend:
cd frontend
npm run dev

Open browser:
http://localhost:5173
Testing
Just paste the links in chrome and make sure both app.py and app.jsx
Verify backend:
http://127.0.0.1:5000/api/health

Expected response:
{
  "status": "healthy"
}

Verify frontend dashboard loads and displays data correctly.
Challenges Encountered
Importing large taxi datasets
Configuring MySQL LOCAL INFILE
API integration between frontend and backend
Handling CORS policies
Managing large Git repositories
Optimizing dashboard performance
Future Improvements
Interactive maps
User authentication
Advanced filtering
Real-time transportation monitoring

Demo video:
https://youtu.be/eQI58Oq0nqA


