import clsx from 'clsx'

export default function ChatMessage({ message }) {
  const isUser = message.role === 'user'

  return (
    <div className={clsx('flex', isUser ? 'justify-end' : 'justify-start')}>
      <div
        className={clsx(
          'max-w-lg p-3 rounded-lg',
          isUser ? 'bg-primary-500 text-white' : 'bg-gray-200 text-gray-800'
        )}
      >
        {message.content}
      </div>
    </div>
  )
}
