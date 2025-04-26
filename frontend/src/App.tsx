import { useState } from 'react'
import { useAsk } from './hooks/useAsk'
import ChatBubble from './components/ChatBubble'

function App() {
  const [question, setQuestion] = useState('')
  const [submittedQuestion, setSubmittedQuestion] = useState('');
  const { ask, answer, isLoading, error } = useAsk()

  const [page, setPage] = useState(1)
  const [allQuestionsAnswered, setAllQuestionsAnswered] = useState(true)
  const [breed, setBreed] = useState("")
  const [matches, setMatches] = useState(0)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    const currentQuestion = question.trim();
    if (!currentQuestion) return
    
    setSubmittedQuestion(currentQuestion);
    setQuestion('');
    await ask(currentQuestion);
  }

  const changePage = (page: number) => {
    setPage(page)
  }

  const changeBreed = (breed: string, matches: number) => {
    setBreed(breed)
    setMatches(matches)
    setPage(5)
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-2xl">

        {page == 1 ? <>
          <img src="../public/landing.png" />

        {/* {error && (
          <div className="p-4 mb-4 text-red-700 bg-red-100 rounded-lg">
            Error: {error}
          </div>
        )} */}

        {/* <div className="mb-4 space-y-4">
          {submittedQuestion && answer && (
            <div className="flex flex-col space-y-4">
              <ChatBubble type="user" message={submittedQuestion} />
              <ChatBubble type="assistant" message={answer} />
            </div>
          )}
        </div> */}

        {/* <form onSubmit={handleSubmit} className="flex flex-col space-y-2">
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
        </form> */}

          <button
            type="submit"
            className="py-2 px-4 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 disabled:opacity-50"
            onClick={() => changePage(2)}
          >
            Next page
          </button>
        </> : null}

        {page == 2 ? <>
          <header className="mb-8 text-center">
            <h1 className="text-xl font-bold text-white header">Hi, Welcome to Fetch!</h1>
            <p className="text-white"><span className="blue text-bold">You deserve to be happy!</span> I'd love to help you find your future best friend...</p>
            <p className="text-white"></p>
          </header>

          <img src="../public/icon_page2.png" style={{width: "300px", margin:  "0 auto"}} />
          <p className="blue">
            Start A Future Best Friend Happiness Quiz to help me fetch your perfect friend.
          </p>
          <button
              type="submit"
              className="py-2 px-4 bg-white text-black rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 disabled:opacity-50"
              onClick={() => changePage(3)}
            >
              Start Quiz
            </button>
        </> : null}

        {page == 3 ? <>
          <header className="mb-8 text-center">
            <img src="../public/icon_3rddog.png" style={{width: "300px", margin:  "0 auto"}} />
            <p className="text-white">First I'll match you with your ideal breed for maximum happiness..</p>
          </header>

          <div className="col-span-full">
            <label htmlFor="about" className="block text-sm/6 font-medium text-gray-900">How much are you spending on grooming?</label>
            <div className="mt-2">
              <div>
                $0-50 <input type="radio" name="grooming" value="1" />
              </div>
              <div>
                $50-100 <input type="radio" name="grooming" value="2" />
              </div>
              <div>
              $100+ <input type="radio" name="grooming" value="3" />
              </div>
            </div>
            <p className="mt-3 text-sm/6 text-gray-600">Write a few sentences about yourself.</p>
          </div>
          

          {allQuestionsAnswered ? <>
            <button
              type="submit"
              className="py-2 px-4 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 disabled:opacity-50"
              onClick={() => changePage(4)}
            >
              First we will match you with your ideal breed for maximium happiness
            </button>
            
          </> : null}
        </> : null}

        {page == 4 ? <>
          <button
              type="submit"
              className="py-2 px-4 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 disabled:opacity-50"
              onClick={() => changeBreed("a", 10)}
            >
              choose me
            </button>
            <button
              type="submit"
              className="py-2 px-4 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 disabled:opacity-50"
              onClick={() => changeBreed("b", 20)}
            >
              choose me
            </button>
            <button
              type="submit"
              className="py-2 px-4 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 disabled:opacity-50"
              onClick={() => changeBreed("c", 30)}
            >
              choose me
            </button>
        </> : null}

        {breed !== "" ? <>
          <p>
            Based on your Best Friend Breed, We found ~{matches} for you
          </p>

          [matches]
        </> : null}
      </div>
    </div>
  )
}

export default App 