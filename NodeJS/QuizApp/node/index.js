const express =  require('express');
const app = express();
const mysql = require('mysql')
const cors = require('cors');
const bodyParser = require('body-parser');

const db = mysql.createPool({
    host : "localhost",
    user : "root",
    password : "",
    database : "quizzDB",
    port : 3306
});

app.use(cors());
app.use(bodyParser.urlencoded({extended : true}));
app.use(bodyParser.json());

app.get('/tests/questions', (req, res) => {
    
    const sqlGet = "SELECT * from questionQuiz";
    db.query(sqlGet, (err, result) => {
        if(err){
            console.log(err);
        }else{
            res.send(result);
        }
    });
});

app.get('/tests/answers', (req, res) => {
    // const id = req.params.id;
    // console.log(id);
    const sqlGet = "SELECT a.idanswerQuiz, q.idquestionQuiz, a.answers, a.isCorrect from questionQuiz q, answerQuiz a"
    +" where q.idquestionQuiz = a.idquestionQuiz";
    db.query(sqlGet, (err, result) => {
        if(err){
            console.log(err);
        }else{
            res.send(result);
        }
    });
});

app.post('/data', (req, res) => {
    const firstName = req.body.firstName
    const lastName = req.body.lastName
    const email = req.body.email
    
    const sqlPost = "INSERT INTO userQuiz (firstName, lastName, email) VALUES (?, ?, ?)";
    db.query(sqlPost, [firstName, lastName, email], (err, result) => {
        if(err){
            console.log(err);
        }else{
            res.send(result);
        }
    })
})

app.listen(3001);
console.log("listenning");