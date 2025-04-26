import { useEffect, useState } from "react";

type ResponseType = "options" | "string" | "boolean" | "number";

interface Option {
  key: string;
  value: string;
}

interface Question {
  name: string;
  description: string;
  responseType: ResponseType;
  options: Option[] | null;
}

interface Answers {
  [key: string]: boolean | string | number;
}

interface PetSurveyFormProps {
  onAnswersChange: (answers: Answers) => void;
}

export default function PetSurveyForm({ onAnswersChange }: PetSurveyFormProps) {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [answers, setAnswers] = useState<Answers>({});

  useEffect(() => {
    async function fetchQuestions() {
      const response = await fetch("/api/questions"); // <-- Adjust API endpoint
      const data: Question[] = await response.json();
      setQuestions(data);
    }

    fetchQuestions();
  }, []);

  function handleChange(name: string, value: boolean | string | number) {
    setAnswers((prev) => {
      const updated = {
        ...prev,
        [name]: value
      };
      onAnswersChange(updated);
      return updated;
    });
  }

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    console.log("Submitting JSON:", JSON.stringify(answers, null, 2));
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

          {(q.responseType === "string" || q.responseType === "number") && (
            <input
              type="text"
              value={answers[q.name] !== undefined ? answers[q.name] : ""}
              onChange={(e) => handleChange(q.name, e.target.value)}
              className="border p-2 rounded"
            />
          )}

          {q.responseType === "options" && q.options && (
            <select
              value={(answers[q.name] as string) || ""}
              onChange={(e) => handleChange(q.name, e.target.value)}
              className="border p-2 rounded"
            >
              <option value="">Select an option</option>
              {q.options.map((opt) => (
                <option key={opt.key} value={opt.key}>
                  {opt.value}
                </option>
              ))}
            </select>
          )}
        </div>
      ))}
    </form>
  );
}
