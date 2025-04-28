import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Stock {
  symbol: string;
  price: string;
  change: string;
  percent_change: string;
}

const TopGainers: React.FC = () => {
  const [gainers, setGainers] = useState<Stock[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/top-gainers')
      .then(response => {
        setGainers(response.data.gainers);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching gainers:', error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Top Gainers</h2>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <table className="w-full text-sm text-left border border-gray-700">
          <thead className="bg-gray-800 text-white">
            <tr>
              <th className="px-4 py-2">Symbol</th>
              <th className="px-4 py-2">Company</th>
              <th className="px-4 py-2">Change</th>
              <th className="px-4 py-2">% Change</th>
            </tr>
          </thead>
          <tbody>
            {gainers.map((stock, idx) => (
              <tr key={idx} className="border-t border-gray-700">
                <td className="px-4 py-2 font-semibold">{stock.symbol}</td>
                <td className="px-4 py-2">{stock.price}</td>
                <td className="px-4 py-2">{stock.percent_change.split(' ')[1]}</td>
                <td className="px-4 py-2 text-green-500">{stock.percent_change.split(' ')[2]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default TopGainers;
