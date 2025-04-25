import React from "react";
import { Stock } from "./types/stock";

interface StockCardProps {
  stock: Stock;
}

const StockCard: React.FC<StockCardProps> = ({ stock }) => {
  // Determine the text color based on the stock's change value
  const changeColor = stock.change.startsWith("+") ? "text-green-600" : "text-red-600";

  return (
    <div className="border rounded-lg shadow-md p-4 flex flex-col items-center bg-white">
      <h3 className="text-xl font-bold mb-2">{stock.symbol}</h3>
      <p className="mb-1 text-center">{stock.name}</p>
      <p className="mb-1">Price: {stock.price || "N/A"}</p>
      <p className={changeColor}>Change: {stock.change}</p>
      <p className={changeColor}>Percent Change: {stock.percent_change}</p>
    </div>
  );
};

export default StockCard;