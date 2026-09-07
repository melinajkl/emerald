FROM node:20-alpine

WORKDIR /app

# Copy dependency definitions
COPY package.json package-lock.json ./

# Install dependencies strictly inside the container
RUN npm ci

# Copy full application code
COPY . .

EXPOSE 3000

# Next.js dev server listening on all network interfaces
CMD ["npx", "next", "dev", "-H", "0.0.0.0", "-p", "3000"]
