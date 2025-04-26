import { useEffect, useState } from "react";

type ResponseType = "boolean" | "list" | "number";

interface Question {
  name: string;
  description: string;
  responseType: ResponseType;
  options: string[] | null;
}

interface Answers {
  [key: string]: boolean | string | number;
}

export default function PetSurveyForm() {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [answers, setAnswers] = useState<Answers>({});

  useEffect(() => {
    async function fetchQuestions() {
      const response = await fetch("/api/questions"); // <-- adjust API endpoint
      const data: Question[] = await response.json();
      setQuestions(data);
    }

    fetchQuestions();
  }, []);

  function handleChange(name: string, value: boolean | string | number) {
    setAnswers((prev) => ({
      ...prev,
      [name]: value
    }));
  }

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    const finalPayload = { ...answers };
    console.log("Submitting JSON:", JSON.stringify(finalPayload, null, 2));

    // Example: send to API
    /*
    fetch('/api/submit-responses', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(finalPayload),
    });
    */
  }

  return (
    <form className="space-y-4 p-4" onSubmit={handleSubmit}>
      {questions.map((q) => (
        <div key={q.name} className="flex flex-col space-y-2">
          <label className="font-semibold">{q.description}</label>

          {q.responseType === "boolean" && (
            <input
              type="checkbox"
              checked={Boolean(answers[q.name])}
              onChange={(e) => handleChange(q.name, e.target.checked)}
            />
          )}

          {q.responseType === "list" && q.options && (
            <select
              value={(answers[q.name] as string) || ""}
              onChange={(e) => handleChange(q.name, e.target.value)}
              className="border p-2 rounded"
            >
              <option value="">Select an option</option>
              {q.options.map((opt) => (
                <option key={opt} value={opt}>
                  {opt}
                </option>
              ))}
            </select>
          )}

          {q.responseType === "number" && (
            <input
              type="number"
              value={answers[q.name] !== undefined ? answers[q.name] : ""}
              onChange={(e) => handleChange(q.name, Number(e.target.value))}
              className="border p-2 rounded"
            />
          )}
        </div>
      ))}

      <button
        type="submit"
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Submit
      </button>

      <pre className="mt-6 bg-gray-100 p-4 rounded">{JSON.stringify(answers, null, 2)}</pre>
    </form>
  );
}

