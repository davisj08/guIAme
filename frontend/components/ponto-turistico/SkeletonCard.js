// components/ponto-turistico/SkeletonCard.js
export default function SkeletonCard() {
  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden">
      <div className="relative h-48 w-full bg-gray-200">
        <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white to-transparent -translate-x-full animate-shimmer"></div>
      </div>
      <div className="p-4">
        <div className="h-4 w-1/3 bg-gray-200 rounded mb-3"></div>
        <div className="h-6 w-3/4 bg-gray-200 rounded mb-2"></div>
        <div className="h-4 w-full bg-gray-200 rounded"></div>
        <div className="h-4 w-5/6 bg-gray-200 rounded mt-1"></div>
      </div>
    </div>
  )
}