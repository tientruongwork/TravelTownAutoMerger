import { cache } from '../utils/cache'
import { StopAppBody } from '../interfaces/IStopApp'
import kill from 'tree-kill'

export const stopAppController = (stopAppBody: StopAppBody): void => {
    const appProcess: number = cache.get(stopAppBody.app)
    if (!appProcess) {
        console.error("App is not running or app incorrects")
        return
    }

    kill(appProcess)
    cache.delete(stopAppBody.app)
}