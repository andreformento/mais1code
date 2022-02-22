var express = require('express');
var router = express.Router();

var listaDeUsuarios = []

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Bruno' });
});


router.get('/sobre', function(req, res, next) {
  res.render('sobre', { minhaVariavel: 'Marriel' });
});

router.post('/usuarios', function(req, res, next) {
  listaDeUsuarios.push({nome: req.body.nomeDoUsuario, idade: req.body.idadeDoUsuario})
  console.log("lista: " + listaDeUsuarios)

  res.render('usuarios', { listaDeUsuarios: listaDeUsuarios });
});

module.exports = router;
