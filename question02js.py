// Define global variables
let username = '';
let currentQuestionIndex = 0;
let correctAnswers = 0;
let totalQuestions = 0;
let timerInterval;
let timeRemaining = 600; // 10 minutes in seconds (600 seconds)

// Define quiz questions
const questions = [
  {
    question: "What is the capital of India?",
    options: ["New Delhi", "Mumbai", "Chennai", "Kolkata"],
    answer: 0
  },
  {
    question: "Who is the Prime Minister of India?",
    options: ["Narendra Modi", "Rahul Gandhi", "Manmohan Singh", "Atal Bihari Vajpayee"],
    answer: 0
  },
  {
    question: "Which is the largest planet in our solar system?",
    options: ["Earth", "Mars", "Jupiter", "Saturn"],
    answer: 2
  },
  {
    question: "What is the largest ocean on Earth?",
    options: ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
    answer: 3
  }
];

// Function to start the test
function startTest() {
  username = document.getElementById('username').value;
  if (username.trim() === '') {
    alert("Please enter your name.");
    return;
  }
  totalQuestions = questions.length;
  document.getElementById('entry-page').classList.add('hidden');
  document.getElementById('test-container').classList.remove('hidden');
  showQuestion();
  startTimer();
}

// Function to display the current question
function showQuestion() {
  const currentQuestion = questions[currentQuestionIndex];
  document.getElementById('question').textContent = currentQuestion.question;
  const optionsContainer = document.getElementById('options');
  optionsContainer.innerHTML = '';

  currentQuestion.options.forEach((option, index) => {
    const button = document.createElement('button');
    button.textContent = option;
    button.onclick = () => checkAnswer(index);
    optionsContainer.appendChild(button);
  });

  // Update the question navigation buttons
  document.getElementById('prev-btn').classList.toggle('hidden', currentQuestionIndex === 0);
  document.getElementById('next-btn').classList.toggle('hidden', currentQuestionIndex === totalQuestions - 1);
  document.getElementById('submit-btn').classList.toggle('hidden', currentQuestionIndex !== totalQuestions - 1);
}

// Function to check if the selected answer is correct
function checkAnswer(selectedOption) {
  const currentQuestion = questions[currentQuestionIndex];
  const buttons = document.querySelectorAll('.options button');

  if (selectedOption === currentQuestion.answer) {
    correctAnswers++;
    buttons[selectedOption].classList.add('correct');
  } else {
    buttons[selectedOption].classList.add('wrong');
  }

  // Disable all options after one is clicked
  buttons.forEach(button => button.disabled = true);
}

// Function to go to the next question
function nextQuestion() {
  currentQuestionIndex++;
  showQuestion();
}

// Function to go to the previous question
function prevQuestion() {
  currentQuestionIndex--;
  showQuestion();
}

// Function to submit the test
function submitTest() {
  clearInterval(timerInterval);
  document.getElementById('test-container').classList.add('hidden');
  document.getElementById('result-container').classList.remove('hidden');

  // Display user details and quiz results
  document.getElementById('user-name').textContent = "Hello, " + username;
  document.getElementById('total-questions').textContent = totalQuestions;
  document.getElementById('correct-answers').textContent = correctAnswers;
  document.getElementById('wrong-answers').textContent = totalQuestions - correctAnswers;

  const finalScore = correctAnswers - (totalQuestions - correctAnswers); // Negative marking can be added here
  document.getElementById('final-score').textContent = finalScore;

  // Total time
  document.getElementById('total-time').textContent = formatTime(timeRemaining);

  // Optionally, create a shareable link for Telegram or other platforms
  const shareLink = document.getElementById('share-link');
  shareLink.href = "https://t.me/share/url?url=Check%20my%20quiz%20score%20here";
}

// Function to start the timer
function startTimer() {
  timerInterval = setInterval(() => {
    timeRemaining--;
    document.getElementById('timer').textContent = formatTime(timeRemaining);

    if (timeRemaining <= 0) {
      clearInterval(timerInterval);
      submitTest();
    }
  }, 1000);
}

// Function to format the time in minutes and seconds
function formatTime(seconds) {
  const minutes = Math.floor(seconds / 60);
  const secondsLeft = seconds % 60;
  return `${String(minutes).padStart(2, '0')}:${String(secondsLeft).padStart(2, '0')}`;
}

// Function to display the final results
function displayResult() {
  document.getElementById('result-container').classList.remove('hidden');
  document.getElementById('total-questions').textContent = totalQuestions;
  document.getElementById('correct-answers').textContent = correctAnswers;
  document.getElementById('wrong-answers').textContent = totalQuestions - correctAnswers;
}