/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    unoptimized: true,
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**',
      },
    ],
  },
  // Desabilita o aviso de <img>
  eslint: {
    ignoreDuringBuilds: true,
  },
}

export default nextConfig
