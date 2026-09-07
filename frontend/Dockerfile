FROM node:20-alpine

# Enable pnpm via Corepack
RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app

# Copy lockfile and package manifest first for efficient caching
COPY package.json pnpm-lock.yaml ./

# Install dependencies strictly from lockfile
RUN pnpm install --no-frozen-lockfile

# Copy remaining source code
COPY . .

# Expose Next.js port
EXPOSE 5173

# Run Next.js in dev mode
CMD ["pnpm", "run", "dev"]