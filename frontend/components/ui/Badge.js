export default function Badge({ children, variant = 'default', className = '' }) {
  const variants = {
    default: 'bg-primary/10 text-primary',
    secondary: 'bg-secondary/10 text-secondary',
    outline: 'bg-transparent border border-primary text-primary',
    success: 'bg-success/10 text-success',
  };

  return (
    <span className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-medium uppercase ${variants[variant]} ${className}`}>
      {children}
    </span>
  );
}
