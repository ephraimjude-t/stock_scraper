// src/components/StockCard.tsx
import React from "react";
import { Stock } from "./types/stock";

interface StockCardProps {
  stock: Stock;
}

const StockCard: React.FC<StockCardProps> = ({ stock }) => {
  const changeColor = stock.change?.startsWith("+") ? "text-green-600" : "text-red-600";

  return (
    <div className="border rounded-lg shadow-md p-4 flex flex-col items-center bg-white opacity-50">
      <h3 className="text-xl font-bold mb-2">{stock.symbol || "N/A"}</h3>
      <p className="mb-1 text-center">{stock.name}</p> {/* ✅ Corrected name */}
      <p className="mb-1">Price: {stock.price}</p> {/* ✅ Handled missing price */}
      <p className={changeColor}>Change: {stock.change}</p>
      <p className={changeColor}>Percent Change: {stock.percent_change}</p>
    </div>
  );
};

export default StockCard;