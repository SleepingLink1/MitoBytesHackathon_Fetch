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
      // const response = await fetch("/api/questions"); // <-- Adjust API endpoint
      //const data: Question[] = await response.json();
      const data = [
        {
          name: "weight_limit",
          description: "do you have a weight restriction for your dog?",
          responseType: "boolean",
          options: null
        },
        {
          name: "coffee",
          description: "what coffees does your dog like?",
          responseType: "options",
          options: [ { "key":'sumatra', "value":'sumatra'}, {'key':'columbian','value':'columbian'}]
        },
        {
          name: "how_many",
          description: "how many dogs?",
          responseType: "number",
          options: null
        },
        ];
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

  async function handleSubmit(e: React.FormEvent) {
    const response = await fetch("http://localhost:8000/submit-survey", {
      method: "POST",
      body: JSON.stringify({
        "grooming_spending": "$0-50",
        "running_miles": "0-1",
        "couch_fur_happiness": 0,
        "vacuum_times": "0",
        "happy_with_large_dogs": true,
        "happy_with_small_dogs": true,
        "hoa_pet_contract": "string",
        "other_pets": [
          "cat"
        ],
        "kids_around_friend": true,
        "travel_distance": "0 miles",
        "home_address": "string",
        "paid_transport": true,
        "envisioned_age": "0-5months",
        "plan_to_travel": true,
        "journey_payment": "$0-$50",
        "food_spending": 0,
        "has_yard": true,
        "personality_traits": "string",
        "active_dogs_enjoyment": "very much",
        "value_compatibility": "very much",
        "cute_dogs": "very much",
        "intact_requirement": true,
        "only_rescue": true,
        "gender_preference": "a female"
      }, null, 2)
    });
    console.log(response);
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
      <input type="submit" />
    </form>
  );
}
