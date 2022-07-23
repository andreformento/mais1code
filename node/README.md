# Rodando node com docker

1. clone o projeto pelo terminal
  ```shell
  git clone git@github.com:caio-ribeiro-pereira/livro-nodejs.git
  ```

2. entre na pasta do projeto
  ```shell
  cd livro-nodejs/projeto/ntalk
  ```

3. crie o arquivo de configuração do docker chamado Dockerfile _(com a primeira maiuscula)_
  ```shell
  touch Dockerfile
  ```

4. use um editor de texto e coloque dentro desse arquivo o seguinte conteúdo
  ```Dockerfile
  FROM node:16.16-alpine3.16
  RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
  WORKDIR /home/node/app
  COPY package*.json ./
  USER node
  RUN npm install
  COPY --chown=node:node . .
  EXPOSE 8090
  CMD [ "node", "index.js" ]
  ```
