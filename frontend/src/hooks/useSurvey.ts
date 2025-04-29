import { useState } from 'react';
import axios from 'axios';

interface SurveyQuestionOption {
    key: string,
    value: string
}

interface SurveyQuestion {
    name: string,
    description: string,
    responseType: string,
    options: Array<SurveyQuestionOption> | null,
}

export function useSurvey() {
    const [questions, setQuestions] = useState<SurveyQuestion[]>([]);
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);
    const [possibleBreed, setPossibleBreed] = useState<any>({});

    const survey = async (): Promise<void> => {
        setIsLoading(true);
        setError(null);

        try {
            const response = await axios.get<SurveyQuestion[]>('/api/survey');
            setQuestions(response.data);
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

    const submitSurvey = async (answers: any): Promise<void> => {
        setIsLoading(true);
        setError(null);

        try {
            const response = await axios.post<any>('/api/submit-survey', answers);
            console.log(response);
            setPossibleBreed(response.data);
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
        survey,
        submitSurvey,
        questions,
        isLoading,
        error,
    };
} 