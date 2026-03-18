FROM node:20-alpine3.22

WORKDIR /app

COPY ["package.json", "yarn.lock", "./"]

RUN yarn install --frozen-lockfile

COPY . .

EXPOSE 5173

CMD ["yarn", "start"]
