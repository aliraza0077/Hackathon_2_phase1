import React, { useState } from 'react';

interface TodoFormProps {
  onAdd: (title: string, description?: string) => void;
}

const TodoForm: React.FC<TodoFormProps> = ({ onAdd }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (title.trim()) {
      onAdd(title, description || undefined);
      setTitle('');
      setDescription('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 mb-10 bg-blue-50/50 p-5 rounded-xl border border-blue-100">
      <div className="flex flex-col gap-3">
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="What needs to be done?"
          className="w-full p-3 border-none bg-white rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 text-gray-900 placeholder:text-gray-400 font-medium"
        />
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Add a description (optional)..."
          rows={2}
          className="w-full p-3 border-none bg-white rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 text-gray-900 placeholder:text-gray-400 resize-none text-sm"
        />
      </div>
      <button
        type="submit"
        disabled={!title.trim()}
        className="w-full bg-blue-600 text-white font-bold py-3 rounded-lg hover:bg-blue-700 disabled:bg-blue-300 disabled:cursor-not-allowed transition-all shadow-md active:scale-[0.98]"
      >
        Add Task
      </button>
    </form>
  );
};

export default TodoForm;
