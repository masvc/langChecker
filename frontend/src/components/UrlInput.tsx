import React, { useState } from 'react';
import axios from 'axios';

const UrlInput: React.FC = () => {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/analyze', { url });
      setResult(response.data);
      setError(null);
    } catch (err) {
      setError('エラーが発生しました。URLを確認してください。');
      setResult(null);
    }
  };

  return (
    <div className="max-w-md mx-auto p-4">
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="URLを入力してください"
          className="w-full p-2 border rounded"
        />
        <button
          type="submit"
          className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
        >
          分析する
        </button>
      </form>
      
      {error && <div className="mt-4 text-red-500">{error}</div>}
      
      {result && (
        <div className="mt-4">
          <h2 className="text-xl font-bold">分析結果</h2>
          <pre className="mt-2 p-4 bg-gray-100 rounded">
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

export default UrlInput; 