const puzzleBoard = document.querySelector('#puzzle')
const solvebtn = document.querySelector('#solve-btn')
const solutionDisplay = document.querySelector('#solution')
const squares = 81
const submission = []
// const dotenv = require('dotenv').config();
// console.log(process.env);

for (let i=0; i< squares; i++) {
    const inputElement = document.createElement('input')
    inputElement.setAttribute('type', 'number')
    inputElement.setAttribute('min', 1)
    inputElement.setAttribute('max', 9)
    if (
        ((i % 9 == 0 || i % 9 == 1 || i % 9 == 2) && i < 21) ||
        ((i % 9 == 6 || i % 9 == 7 || i % 9 == 8) && i < 27) ||
        ((i % 9 == 3 || i % 9 == 4 || i % 9 == 5) && (i > 27 && i < 53)) ||
        ((i % 9 == 0 || i % 9 == 1 || i % 9 == 2) && i > 53) ||
        ((i % 9 == 6 || i % 9 == 7 || i % 9 == 8) && i > 53)
    ) {
        inputElement.classList.add('odd-section')
    }

    puzzleBoard.appendChild(inputElement)
}

const joinValues = () => {
    const inputs = document.querySelectorAll('input')
    inputs.forEach(input => {
        if (input.value) {
            submission.push(input.value)
        } else {
            submission.push('.')
        }
    })

    console.log(submission)
}

const populateValues = (isSolvable, solution) => {
    const inputs = document.querySelectorAll('input')
    if (isSolvable && solution) {
        inputs.forEach((input, i) => {
            input.value =solution[i]
        })
        solutionDisplay.innerHTML = 'This is the solution'
    } else {
        solutionDisplay.innerHTML = 'This is not solvable'
    }
}

const solve = () => {
    joinValues()
    const data = submission.join('')
    const options = {
      method: 'POST',
      url: 'https://solve-sudoku.p.rapidapi.com/',
      headers: {
        'content-type': 'application/json',
        'X-RapidAPI-Host': 'solve-sudoku.p.rapidapi.com',
        'X-RapidAPI-Key': config.RAPID_API_KEY
      },
      data: {
          puzzle: data}
    };

    axios.request(options).then((response) => {
        console.log(response.data)
        populateValues(response.data.solvable, response.data.solution )
    }).catch((error) => {
        console.error(error)
    });
}




solvebtn.addEventListener('click', solve)