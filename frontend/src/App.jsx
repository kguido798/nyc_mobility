import { useEffect, useState } from "react";
import RevenueChart from "./components/RevenueChart";
function App() {
  const [health, setHealth] = useState("");
  const [trips, setTrips] = useState([]);
  const [stats, setStats] = useState({});
  const [chartData, setChartData] = useState([]);
  useEffect(() => {
  fetch("http://127.0.0.1:5000/api/stats/revenue-by-day")
  .then(res => res.json())
  .then(data => setChartData(data));
  fetch("http://127.0.0.1:5000/api/health")
    .then(res => res.json())
    .then(data => setHealth(data.status));

  fetch("http://127.0.0.1:5000/api/trips?limit=5")
    .then(res => res.json())
    .then(data => setTrips(data));

  fetch("http://127.0.0.1:5000/api/stats/summary")
    .then(res => res.json())
    .then(data => setStats(data));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>NYC Mobility Dashboard</h1>

      <h3>API Status: {health}</h3>

      <div
  style={{
    display: "grid",
    gridTemplateColumns: "repeat(4, 1fr)",
    gap: "20px",
    marginBottom: "30px",
  }}
>
  <div className="card">
    <h3>Total Trips</h3>
    <h2>{Number(stats.totalTrips).toLocaleString()}</h2>
  </div>

  <div className="card">
    <h3>Average Fare</h3>
    <h2>${Number(stats.averageFare).toFixed(2)}</h2>
  </div>

  <div className="card">
    <h3>Average Distance</h3>
    <h2>{Number(stats.averageDistance).toFixed(2)} mi</h2>
  </div>

  <div className="card">
    <h3>Total Revenue</h3>
    <h2>${Number(stats.totalRevenue).toLocaleString()}</h2>
  </div>
</div>
<RevenueChart chartData={chartData} />
      <h2>Recent Trips</h2>

<table
  style={{
    width: "100%",
    borderCollapse: "collapse",
    backgroundColor: "white",
    color: "black",
  }}
>
  <thead>
    <tr>
      <th>Trip ID</th>
      <th>Pickup Zone</th>
      <th>Dropoff Zone</th>
      <th>Distance (mi)</th>
      <th>Fare ($)</th>
      <th>Total ($)</th>
    </tr>
  </thead>

  <tbody>
    {trips.map((t) => (
      <tr key={t.trip_id}>
        <td>{t.trip_id}</td>
        <td>{t.pickup_location_id}</td>
        <td>{t.dropoff_location_id}</td>
        <td>{t.trip_distance}</td>
        <td>{t.fare_amount}</td>
        <td>{t.total_amount}</td>
      </tr>
    ))}
  </tbody>
</table>
    </div>
  );
}

export default App;