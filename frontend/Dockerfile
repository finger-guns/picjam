# frontend/Dockerfile

FROM node:20

WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

COPY pnpm-lock.yaml package.json ./
RUN pnpm install

COPY . .

CMD ["pnpm", "dev"]
