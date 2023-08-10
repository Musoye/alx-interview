#!/usr/bin/node
const request = require('request')

function (url, arg) {
  request(url, (error, response, body) {
	  console.log(body)
  }
}

