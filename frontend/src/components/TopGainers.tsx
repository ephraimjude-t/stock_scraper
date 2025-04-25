// src/components/GainersList.tsx
import React from "react";
import StockCard from "./StockCard";
import { useStockData } from "./hooks/useStockData";

const GainersList: React.FC = () => {
  const startEndpoint = "http://localhost:5000/api/start"; // Adjust as needed
  const dataEndpoint = "http://localhost:5000/api/top_gainers";
  const { stocks, loading, error } = useStockData(dataEndpoint, startEndpoint);

  if (loading)
    return <div className="text-center py-4">Loading Top Gainers…</div>;
  if (error)
    return (
      <div className="text-center text-red-600 py-4">Error: {error}</div>
    );

  return (
    <div className="my-8">
      <h2 className="text-2xl font-bold mb-4">Top Gainers</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {stocks.map((stock, idx) => (
          <StockCard key={idx} stock={stock} />
        ))}
      </div>
    </div>
  );
};

export default GainersList;