export default function Card({ children, hover = false, className = '' }) {
  const hoverClasses = hover 
    ? 'hover:shadow-lg hover:-translate-y-1 cursor-pointer' 
    : '';

  return (
    <div className={`bg-white rounded-xl shadow-sm border border-border p-6 transition-all duration-300 ${hoverClasses} ${className}`}>
      {children}
    </div>
  );
}
