#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const result = {};
    for (const task of tasks) {
      if (task.completed) {
        if (result[task.userId] === undefined) {
          result[task.userId] = 0;
        }
        result[task.userId]++;
      }
    }
    console.log(result);
  }
});
