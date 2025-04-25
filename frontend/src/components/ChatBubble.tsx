import React from 'react';

interface ChatBubbleProps {
  type: 'user' | 'assistant';
  message: string;
}

const ChatBubble: React.FC<ChatBubbleProps> = ({ type, message }) => {
  const isUser = type === 'user';
  
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div 
        className={`max-w-[80%] p-3 rounded-lg ${
          isUser 
            ? 'bg-indigo-600 text-white rounded-br-none' 
            : 'bg-gray-200 text-gray-800 rounded-bl-none'
        }`}
      >
        <p className="whitespace-pre-wrap break-words">{message}</p>
      </div>
    </div>
  );
};

export default ChatBubble; 