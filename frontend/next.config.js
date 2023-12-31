/** @type {import('next').NextConfig} */
const nextConfig = {
    rewrites: async () => {
        return [
          {
            source: "/api/:path*",
            destination:
              process.env.NODE_ENV !== "development"
              ? "https://library-dbms-backend.vercel.app/api/:path*"
              : "http://127.0.0.1:8000/api/:path*",
          },
        ];
      },
}

module.exports = nextConfig
