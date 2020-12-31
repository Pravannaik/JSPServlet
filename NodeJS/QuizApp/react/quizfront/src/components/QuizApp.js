import React, {useState, useEffect} from 'react';
import Axios from 'axios';
import './QuizApp.css';

function QuizApp() {

  const [currentQuestion, setCurrentQuestion] = useState(1);
  const [quizQues, setQuizQues] = useState([]);
  const [quizAns, setQuizAns] = useState([]);
  const [showScore, setShowScore] = useState(false);
  const [seconds, setSeconds] = useState(10);
  const [score, setScore] = useState(0);
  const [attempt, setAttempt] = useState(0);
  const [result, setResult] = useState(false)
  

  useEffect(() => {

    async function callAPI() {
        await Axios.get('http://localhost:3001/tests/questions').then((response) => {
        //console.log(response.data[1].questions);
        setQuizQues(response.data);
        });

        await Axios.get('http://localhost:3001/tests/answers').then((response) => {
        //console.log(response.data[1].questions);
        setQuizAns(response.data);
        });
    }

    callAPI();
  }, []);

   useEffect(() => {
     if (seconds > 0) {
        const timer = seconds > 0 && setInterval(() => setSeconds(seconds - 1), 1000);
        return () => clearInterval(timer);
     } else {
       afterAnswerClick(currentQuestion, "flase", 0);
     }
   }, [seconds]);

  const afterAnswerClick = (currentQuestion, isTrue, flag) => {
    const newQuest = currentQuestion + 1

    if(flag === 1){
        setAttempt(attempt + 1)
    }

    if(isTrue === "true"){
        setScore(score + 1)
    }

    if(score > 5){
        setResult(true)
    }

    if(newQuest <= quizQues.length){
      setCurrentQuestion(newQuest)
      setSeconds(10)
    }else{
      setShowScore(true)
    }
    
  }

  return (
    <>
        <div className="App">
            { showScore ? (
                <div className="scoreSec">
                    { result ? (
                        <h1>Congratulations!!!, You have passed the Quiz</h1>
                    ) : (<h1>Quiz result: Failed</h1>)}
                    <h2>You have scored {score} out of {quizQues.length}</h2>
                    <h2>Question Attempted : {attempt}/{quizQues.length}</h2>
                </div>
            ) : (
                <>
                    <div className="TimerSec">
                        <h1>{seconds}</h1>
                    </div> 
                    <div className="QuizSection">
                        <div className="Ques">
                            <div className='questionCount'>
                                <span>Question {currentQuestion}</span>/{quizQues.length}
                            </div>
                            {quizQues.filter(ques => ques.idquestionQuiz === currentQuestion).map((quesVal) => (
                                <div className="questionText">{quesVal.questions}</div>
                            ))}
                        </div>
                        <div className="Ans">
                        {quizAns.filter(ans => ans.idquestionQuiz === currentQuestion).map((option) => (
                            <button onClick={() => afterAnswerClick(currentQuestion, option.isCorrect, 1 ) } className="AnsButton">{option.answers}</button>
                        ))}
                        </div> 
                    </div>
                </>
            )}
        </div>
    </>
  );
}

export default QuizApp
