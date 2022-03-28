FROM node:16.14.2

WORKDIR /project/frontend/

COPY frontend/package.json /project/frontend/
COPY frontend/package-lock.json /project/frontend/

RUN npm install

COPY . /project/frontend/

CMD ["npm", "run", "start"]