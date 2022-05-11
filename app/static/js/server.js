const PORT = 80
const axios = require('axios').default
const express = require('express')
const cors = require('cors')
require('dotenv').config({path: '../../../.env'})
const api = process.env.RAPID_API_KEY

const app = express()
app.use(cors())
app.use(express.json())

app.listen(PORT, () => {
    console.log('server listening on PORT' ${PORT})
});
