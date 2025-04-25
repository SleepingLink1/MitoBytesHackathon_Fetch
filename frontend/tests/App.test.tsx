import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from '../src/App';
import * as useAskModule from '../src/hooks/useAsk';

// Mock the useAsk hook
vi.mock('../src/hooks/useAsk', () => ({
  useAsk: vi.fn(),
}));

describe('App', () => {
  it('renders the app title', () => {
    vi.mocked(useAskModule.useAsk).mockReturnValue({
      ask: vi.fn(),
      answer: '',
      isLoading: false,
      error: null,
    });

    render(<App />);
    expect(screen.getByText('LLM Chat Interface')).toBeInTheDocument();
  });

  it('disables the button when loading', () => {
    vi.mocked(useAskModule.useAsk).mockReturnValue({
      ask: vi.fn(),
      answer: '',
      isLoading: true,
      error: null,
    });

    render(<App />);
    expect(screen.getByRole('button')).toBeDisabled();
    expect(screen.getByRole('button')).toHaveTextContent('Loading...');
  });

  it('displays error message when there is an error', () => {
    vi.mocked(useAskModule.useAsk).mockReturnValue({
      ask: vi.fn(),
      answer: '',
      isLoading: false,
      error: 'Test error message',
    });

    render(<App />);
    expect(screen.getByText('Error: Test error message')).toBeInTheDocument();
  });

  it('calls ask with the question when form is submitted', async () => {
    const mockAsk = vi.fn();
    vi.mocked(useAskModule.useAsk).mockReturnValue({
      ask: mockAsk,
      answer: '',
      isLoading: false,
      error: null,
    });

    render(<App />);
    
    const textarea = screen.getByPlaceholderText('Type your question here...');
    fireEvent.change(textarea, { target: { value: 'What is the meaning of life?' } });
    
    const button = screen.getByRole('button', { name: 'Ask' });
    fireEvent.click(button);
    
    await waitFor(() => {
      expect(mockAsk).toHaveBeenCalledWith('What is the meaning of life?');
    });
  });
}); 