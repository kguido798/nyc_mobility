import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from "chart.js";

import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

function RevenueChart({ chartData }) {
  const data = {
    labels: chartData.map(item => item.trip_date),
    datasets: [
      {
        label: "Revenue ($)",
        data: chartData.map(item => item.revenue),
      }
    ]
  };

  return (
    <div
      style={{
        background: "white",
        padding: "20px",
        borderRadius: "12px",
        marginBottom: "30px"
      }}
    >
      <Line data={data} />
    </div>
  );
}

export default RevenueChart;