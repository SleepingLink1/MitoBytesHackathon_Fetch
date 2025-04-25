import { useState } from 'react';
import axios from 'axios';

interface AskResponse {
  answer: string;
}

export function useAsk() {
  const [answer, setAnswer] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const ask = async (question: string): Promise<void> => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await axios.post<AskResponse>('/api/ask', { question });
      setAnswer(response.data.answer);
    } catch (err) {
      const errorMessage = axios.isAxiosError(err) 
        ? err.response?.data?.detail || err.message 
        : 'Failed to get response';
      setError(errorMessage);
      console.error('Error asking question:', err);
    } finally {
      setIsLoading(false);
    }
  };

  return {
    ask,
    answer,
    isLoading,
    error,
  };
} 