import { useState } from 'react'
import { useAsk } from './hooks/useAsk'
import ChatBubble from './components/ChatBubble'
import PetSurveyForm from './components/PetSurveyForm'

function App() {
  const [question, setQuestion] = useState('')
  const [surveyAnswers, setSurveyAnswers] = useState({});
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

  const submitAnswer = () => {
    changePage(4)
  }

  function handleAnswersChange(updatedAnswers: Record<string, boolean | string | number>) {
    setSurveyAnswers(updatedAnswers);
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-2xl">

        {page == 1 ? <>
          <img src="../public/landing.png" />

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
            <h1 className="text-3xl font-bold text-white header mb-4">Hi, Welcome to Fetch!</h1>
            <p className="text-white"><span className="blue text-bold">You deserve to be happy!</span> Everyone knows life is just better with a dog. When you’re ready, I’d love to help you find your future best friend...</p>
            <p className="text-white"></p>
          </header>

          <img src="../public/icon_page2.png" style={{width: "300px", margin:  "0 auto"}} />
          <p className="blue text-center mb-4">
            Start A Future Best Friend Happiness Quiz to help me fetch your perfect friend.
          </p>
          <div>
          <button
              type="submit"
              className="py-2 px-4 bg-white text-black rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 disabled:opacity-50"
              onClick={() => changePage(3)}
            >
              Start Quiz
            </button>
          </div>
          
        </> : null}

        {page == 3 ? <>
          <header className="mb-8 text-center">
            <img src="../public/icon_3rddog.png" style={{width: "300px", margin:  "0 auto"}} />
            <p className="text-white">First I'll match you with your ideal breed for maximum happiness..</p>
          </header>

          <PetSurveyForm onAnswersChange={handleAnswersChange} />

          {allQuestionsAnswered ? <>
            <button
              type="submit"
              className="py-2 px-4 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 disabled:opacity-50"
              onClick={() => submitAnswer()}
            >
              see results!
            </button>
            
          </> : null}
        </> : null}

        {page == 4 ? <>

        <div className="columns-3">
        <div>
          <img src="../public/corgi.png" style={{width: "300px", margin:  "0 auto"}} />
          <button
              type="submit"
              className="py-2 px-4 border border-black text-white rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 disabled:opacity-50"
              onClick={() => changeBreed("a", 10)}
            >
              Choose me!
            </button>
        </div>
        <div>
          <img src="../public/goldenretriever.png" style={{width: "300px", margin:  "0 auto"}} />
          <button
              type="submit"
              className="py-2 px-4 border border-black text-white rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 disabled:opacity-50"
              onClick={() => changeBreed("b", 20)}
            >
              Choose me!
            </button>
          </div>
          <div>
            <img src="../public/husky.png" style={{width: "300px", margin:  "0 auto"}} />
            <button
              type="submit"
              className="py-2 px-4 border border-black text-white rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 disabled:opacity-50"
              onClick={() => changeBreed("c", 30)}
            >
              Choose me!
            </button>
            </div>
        </div>
        
          
            
            
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
