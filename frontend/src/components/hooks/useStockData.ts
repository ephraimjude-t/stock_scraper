// src/hooks/useStockData.ts
import { useState, useEffect, useCallback } from "react";
import { Stock } from "../types/stock";

export const useStockData = (dataEndpoint: string, startEndpoint: string) => {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  const fetchStocks = useCallback(async () => {
    try {
      // Trigger the daily update process
      await fetch(startEndpoint);

      // Then fetch the data from the specified endpoint (gainers or losers)
      const res = await fetch(dataEndpoint);
      if (!res.ok) {
        throw new Error(`Network error: ${res.statusText}`);
      }
      const data: Stock[] = await res.json();
      setStocks(data);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [dataEndpoint, startEndpoint]);

  useEffect(() => {
    fetchStocks();

    // Optional: Auto-refresh the data every 24 hours if needed.
    const intervalId = setInterval(fetchStocks, 86400000);
    return () => clearInterval(intervalId);
  }, [fetchStocks]);

  return { stocks, loading, error };
};