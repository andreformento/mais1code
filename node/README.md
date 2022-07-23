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
  FROM node:0.10.28
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
  docker run -p 3000:3000 node-web-app
  ```

7. sua aplicação está rodando e pode ser acessada pelo browser através de http://localhost:3000

8. após qualquer alteração realizada na aplicação basta executar os passos `5` e `6` novamente
