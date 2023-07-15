FROM node:18-alpine as base

WORKDIR /app

COPY package*.json ./ package-lock.json ./

RUN npm install

COPY . .


FROM base as dev

CMD [ "npm", "run", "dev" ]
