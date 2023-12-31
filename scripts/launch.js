const fs = require('fs')
const shelljs = require('shelljs')

const isError = shelljs.exec('curl -sS -m 1 -X GET http://localhost:5000/health').stderr

if (!!isError) {
    if (!fs.existsSync(".env")) {
        console.warn("no .env file found, start with default settings")
    } else {
        const dotenv = fs.readFileSync(".env", { encoding: 'utf-8' })

        const lines = dotenv.replaceAll("\r", "").split("\n")
        envvars = lines.join(" ")
    }
    shelljs.exec(`cross-env ${envvars} webpack && cross-env ${envvars} node ./build/main.bundle.js`, { async: true })
}

shelljs.exec(`yarn start-ui`, { async: true })
