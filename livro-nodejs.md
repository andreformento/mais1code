# Rodando node com docker

1. clone o projeto pelo terminal
  ```shell
  git clone git@github.com:caio-ribeiro-pereira/livro-nodejs.git
  ```

2. entre na pasta da aplicação _(para os outros capítulos, entre na pasta respectiva)_
  ```shell
  cd livro-nodejs/capitulo-4/ntalk
  ```

3. crie o arquivo de configuração do docker chamado Dockerfile _(com a primeira maiuscula)_
  ```shell
  touch Dockerfile
  ```

4. use um editor de texto e coloque dentro desse arquivo o seguinte conteúdo

- até o capítulo 9 você usa `app.js`:
  ```Dockerfile
  FROM node:18.6-alpine3.15
  WORKDIR /usr/src/app
  COPY package*.json ./
  RUN npm install
  COPY . .
  EXPOSE 8080
  CMD [ "node", "app.js" ]
  ```

- no capítulo 10 você usa `server.js` (só muda a ultima linha):
  ```Dockerfile
  FROM node:18.6-alpine3.15
  WORKDIR /usr/src/app
  COPY package*.json ./
  RUN npm install
  COPY . .
  EXPOSE 8080
  CMD [ "node", "server.js" ]
  ```

5. construa (build) a imagem docker com a sua aplicação
  ```shell
  docker build . -t node-web-app
  ```

6. execute o container através da imagem recem criada
  ```shell
  docker run --init -p 3000:3000 node-web-app
  ```

7. sua aplicação está rodando e pode ser acessada pelo browser através de http://localhost:3000

8. após qualquer alteração realizada no código basta executar os passos `5` e `6` novamente que a imagem vai ser reconstruída e o container vai ser reiniciado
