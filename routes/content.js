
var path = require('path');
var fs = require('fs');
var express = require('express');

var router = express.Router();

// Width & Height
router.get('/b-1', function(req, res) {
  res.render('b-1');
}); 

// Width & Height Python
router.get('/py-1', function(req, res) {
  res.render('py-1');
}); 

// Create Empty Maze challenge
router.get('/py-1a', function(req, res) {
  res.render('py-1a');
});

// Width & Height Python using variables
router.get('/py-2', function(req, res) {
  res.render('py-2');
}); 

// Width & Height Python challenge fix var name
router.get('/py-3', function(req, res) {
  res.render('py-3');
}); 

// Create 3 walls, monsters, energies and add player - challenge
router.get('/py-4', function(req, res) {
  res.render('py-4');
}); 

// Multi variable challenge
router.get('/py-5', function(req, res) {
  res.render('py-5');
});

// One variable for all
router.get('/py-5a', function(req, res) {
  res.render('py-5a');
}); 

// One variable for all
router.get('/py-5b', function(req, res) {
  res.render('py-5b');
}); 


// Variable arithmetic
router.get('/py-6', function(req, res) {
  res.render('py-6');
}); 

// Variable arithmetic subtraction
router.get('/py-7', function(req, res) {
  res.render('py-7');
}); 

// Variable arithmetic multiplication
router.get('/py-8', function(req, res) {
  res.render('py-8');
}); 

// Variable arithmetic multiplication
router.get('/py-9', function(req, res) {
  res.render('py-9');
}); 

// Strings intro
router.get('/py-10', function(req, res) {
  res.render('py-10');
}); 

// Strings intro
router.get('/py-11', function(req, res) {
  res.render('py-11');
}); 

// String arithmetic
router.get('/py-12', function(req, res) {
  res.render('py-12');
}); 

// String arithmetic
router.get('/py-13', function(req, res) {
  res.render('py-13');
});

// challenge String arithmetic
router.get('/py-14', function(req, res) {
  res.render('py-14');
});

// Number + string
router.get('/py-15', function(req, res) {
  res.render('py-15');
});

module.exports = router;



