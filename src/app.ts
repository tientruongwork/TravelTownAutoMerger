import express, { Express, Request, Response } from "express";
import bodyParser from 'body-parser'
import cors from 'cors'
import { StartAppBody } from './interfaces/IStartApp'
import { StopAppBody } from './interfaces/IStopApp'
import { startAppController, stopAppController, terminateAppController } from './controller'
import kill from 'kill-port'

const app: Express = express();
app.use(bodyParser())
app.use(cors())

const PORT = process.env.PORT || 5000;

app.post('/stop', (req: Request<any, any, StopAppBody, any, any>, res: Response) => {
    stopAppController(req.body)
    res.sendStatus(200)
})

app.post("/start", (req: Request<any, any, StartAppBody, any, any>, res: Response) => {
    startAppController(req.body)
    res.sendStatus(200)
})

app.get('/health', (_, res: Response) => {
    res.sendStatus(200)
})

app.get('/terminate', () => {
    terminateAppController()
    setTimeout(() => {
        kill(5000)
    }, 500)
})

app.listen(PORT, () => {
    console.log(`Application is running on port:${PORT}`);
});
