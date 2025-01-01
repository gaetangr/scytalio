FROM node:18-slim

WORKDIR /frontend

COPY package.json ./
COPY package-lock.json ./
RUN npm install --no-cache

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]