// src/hooks/useStockData.ts
import { useState, useEffect } from "react";
import { Stock } from "../types/stock";

export const useStockData = (dataEndpoint: string, startEndpoint: string) => {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchStocks = async () => {
      try {
        await fetch(startEndpoint);
        const res = await fetch(dataEndpoint);
        const data = await res.json();

        console.log("API Raw Response:", data); // ✅ Debugging output

        // ✅ Manually format the stock data before setting state
        const formattedStocks = data.gainers.map((stock: any) => ({
          symbol: stock.symbol || "N/A",
          name: stock.Name || "Unknown Company", // ✅ Fix capitalization issue
          price: stock.price && stock.price.trim() !== "" ? stock.price : "N/A", // ✅ Handle missing price
          change: stock.change || "N/A",
          percent_change: stock.percent_change || "N/A",
        }));

        setStocks(formattedStocks);
      } catch (err) {
        const errorMessage = err instanceof Error ? err.message : "Unknown error occurred.";
        setError(errorMessage);
      } finally {
        setLoading(false);
      }
    };

    fetchStocks();
  }, [dataEndpoint, startEndpoint]);

  return { stocks, loading, error };
};