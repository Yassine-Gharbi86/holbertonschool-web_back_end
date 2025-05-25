const express = require('express');
const fs = require('fs');
const process = require('process');

const app = express();
const port = 1245;


function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const header = lines.shift().split(',');
      const students = lines.map((line) => line.split(','));
      const counts = {};
      for (const student of students) {
        const firstname = student[0];
        const field = student[3];
        if (!counts[field]) counts[field] = [];
        counts[field].push(firstname);
      }
      const total = students.length;
      resolve({ total, counts });
    });
  });
}

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.type('text/plain');
  const dbFile = process.argv[2];
  try {
    const { total, counts } = await countStudents(dbFile);
    let response = 'This is the list of our students';
    response += `\nNumber of students: ${total}`;
    for (const [field, students] of Object.entries(counts)) {
      response += `\nNumber of students in ${field}: ${students.length}. List: ${students.join(', ')}`;
    }
    res.send(response);
  } catch (err) {
    res.send(err.message);
  }
});

if (require.main === module) {
  app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
  });
}

module.exports = app;

