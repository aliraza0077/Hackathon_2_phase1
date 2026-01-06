import React from 'react';

export interface Todo {
  id: number;
  title: string;
  description?: string;
  is_completed: boolean;
}

interface TodoItemProps {
  todo: Todo;
  onToggle: (id: number, is_completed: boolean) => void;
  onDelete: (id: number) => void;
  onEdit: (todo: Todo) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({ todo, onToggle, onDelete, onEdit }) => {
  return (
    <div className="flex items-start justify-between p-4 bg-white border-b border-gray-100 hover:bg-gray-50 transition-colors group">
      <div className="flex items-start gap-4">
        <div className="pt-1">
          <input
            type="checkbox"
            checked={todo.is_completed}
            onChange={(e) => onToggle(todo.id, e.target.checked)}
            className="w-5 h-5 cursor-pointer accent-blue-600 rounded"
          />
        </div>
        <div className="flex flex-col">
          <span className={`text-lg font-medium leading-tight ${todo.is_completed ? 'line-through text-gray-400' : 'text-gray-900'}`}>
            {todo.title}
          </span>
          {todo.description && (
            <p className={`text-sm mt-1 ${todo.is_completed ? 'text-gray-300' : 'text-gray-500'}`}>
              {todo.description}
            </p>
          )}
        </div>
      </div>
      <div className="flex items-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
        <button
          onClick={() => onEdit(todo)}
          className="text-blue-500 hover:text-blue-700 hover:bg-blue-50 p-1.5 rounded-md transition-colors"
          title="Edit"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
          </svg>
        </button>
        <button
          onClick={() => onDelete(todo.id)}
          className="text-red-500 hover:text-red-700 hover:bg-red-50 p-1.5 rounded-md transition-colors"
          title="Delete"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v2m3 4s5 0 6 0" />
          </svg>
        </button>
      </div>
    </div>
  );
};

export default TodoItem;
