import clsx from 'clsx'

export default function Card({ children, className, hover = false, ...props }) {
  return (
    <div
      className={clsx(
        'bg-white rounded-xl shadow-soft p-6',
        hover && 'transition-shadow hover:shadow-medium cursor-pointer',
        className
      )}
      {...props}
    >
      {children}
    </div>
  )
}
