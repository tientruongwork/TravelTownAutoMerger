import child_process from 'child_process'

import { buildStartAppCommand } from '../utils/commands'
import { cache } from '../utils/cache'
import { StartAppBody } from '../interfaces/IStartApp'

export const startAppController = (startAppBody: StartAppBody) => {
    const command = buildStartAppCommand(startAppBody)
    const process = child_process.exec(command)
    cache.set(startAppBody.app, process.pid)
    return command
}