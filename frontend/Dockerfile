
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./ package-lock.json ./
RUN npm install
COPY . .
RUN npm run build
ENV HOST=0.0.0.0
EXPOSE 4500-6000
CMD [ "npm", "run", "dev" ]