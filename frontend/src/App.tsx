import { useState } from 'react'
import { useAsk } from './hooks/useAsk'
import ChatBubble from './components/ChatBubble'

function App() {
  const [question, setQuestion] = useState('')
  const [submittedQuestion, setSubmittedQuestion] = useState('');
  const { ask, answer, isLoading, error } = useAsk()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    const currentQuestion = question.trim();
    if (!currentQuestion) return
    
    setSubmittedQuestion(currentQuestion);
    setQuestion('');
    await ask(currentQuestion);
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-2xl">
        <header className="mb-8 text-center">
          <h1 className="text-3xl font-bold text-indigo-600">LLM Chat Interface</h1>
          <p className="text-gray-600">Ask a question and get an answer from the LLM</p>
        </header>

        {error && (
          <div className="p-4 mb-4 text-red-700 bg-red-100 rounded-lg">
            Error: {error}
          </div>
        )}

        <div className="mb-4 space-y-4">
          {submittedQuestion && answer && (
            <div className="flex flex-col space-y-4">
              <ChatBubble type="user" message={submittedQuestion} />
              <ChatBubble type="assistant" message={answer} />
            </div>
          )}
        </div>

        <form onSubmit={handleSubmit} className="flex flex-col space-y-2">
          <textarea
            className="p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
            rows={3}
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Type your question here..."
            disabled={isLoading}
          />
          <button
            type="submit"
            disabled={isLoading || !question.trim()}
            className="py-2 px-4 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 disabled:opacity-50"
          >
            {isLoading ? 'Loading...' : 'Ask'}
          </button>
        </form>
      </div>
    </div>
  )
}

export default App 