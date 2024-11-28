const questions = [
  {
    question: "What is the capital of India?",
    options: ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
    answer: 0,
  },
  {
    question: "Which planet is known as the Red Planet?",
    options: ["Earth", "Mars", "Jupiter", "Saturn"],
    answer: 1,
  },
  {
    question: "Who developed the theory of relativity?",
    options: ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
    answer: 1,
  },
  {
    question: "What is the largest mammal on Earth?",
    options: ["Elephant", "Blue Whale", "Giraffe", "Shark"],
    answer: 1,
  },
  {
    question: "Which element is the most abundant in the Earth's atmosphere?",
    options: ["Oxygen", "Nitrogen", "Carbon", "Hydrogen"],
    answer: 1,
  }
];

let currentQuestion = 0;
let correctAnswers = 0;
let totalTime = 0;
let timerInterval;

function startTest() {
  const name = document.getElementById('username').value;
  if (name.trim() === '') {
    alert('Please enter your name!');
    return;
  }
  document.getElementById('entry-page').classList.add('hidden');
  document.getElementById('test-container').classList.remove('hidden');
  loadQuestion();
  startTimer();
}

function loadQuestion() {
  const question = questions[currentQuestion];
  document.getElementById('question').textContent = question.question;
  const options = document.getElementById('options');
  options.innerHTML = ''; // Clear previous options
  question.options.forEach((option, index) => {
    const button = document.createElement('button');
    button.textContent = option;
    button.onclick = () => checkAnswer(index);
    options.appendChild(button);
  });
}

function checkAnswer(selectedIndex) {
  const correctIndex = questions[currentQuestion].answer;
  if (selectedIndex === correctIndex) {
    correctAnswers++;
  }
  if (currentQuestion < questions.length - 1) {
    currentQuestion++;
    loadQuestion();
  } else {
    clearInterval(timerInterval);
    showResult();
  }
}

function startTimer() {
  let timeLeft = 300; // 5 minutes
  timerInterval = setInterval(() => {
    timeLeft--;
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    document.getElementById('timer').textContent = `${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    if (timeLeft === 0) {
      clearInterval(timerInterval);
      showResult();
    }
  }, 1000);
}

function showResult() {
  document.getElementById('test-container').classList.add('hidden');
  document.getElementById('result-container').classList.remove('hidden');
  document.getElementById('user-name').textContent = 'Name: ' + document.getElementById('username').value;
  document.getElementById('total-questions').textContent = questions.length;
  document.getElementById('correct-answers').textContent = correctAnswers;
  document.getElementById('wrong-answers').textContent = questions.length - correctAnswers;
  document.getElementById('final-score').textContent = correctAnswers;
  document.getElementById('total-time').textContent = document.getElementById('timer').textContent;
}

function prevQuestion() {
  if (currentQuestion > 0) {
    currentQuestion--;
    loadQuestion();
  }
}

function nextQuestion() {
  if (currentQuestion < questions.length - 1) {
    currentQuestion++;
    loadQuestion();
  }
}

function submitTest() {
  clearInterval(timerInterval);
  showResult();
}