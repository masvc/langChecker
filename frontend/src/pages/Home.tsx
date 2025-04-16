import React from 'react';
import UrlInput from '../components/UrlInput';

const Home: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto py-8">
        <h1 className="text-3xl font-bold text-center mb-8">LangChecker</h1>
        <UrlInput />
      </div>
    </div>
  );
};

export default Home; 