import path from 'path'
import { StartAppBody } from '../interfaces/IStartApp'
import { getCorePath, getStoragePath } from './pathResolve'
import fs from 'fs'

export const buildStartAppCommand = (startAppBody: StartAppBody) => {
    const corePath = getCorePath()
    const storagePath = getStoragePath()

    const resourcesPath = path.join(storagePath, "common")
    const appStoragePath = path.join(storagePath, startAppBody.app)

    if (!fs.existsSync(appStoragePath)) {
        fs.mkdirSync(appStoragePath, { recursive: true })
    }

    return `python ${corePath} --ld=${startAppBody.app} --rows=${startAppBody.rows} --cols=${startAppBody.cols} --resources-path=${resourcesPath} --app-storage-path=${appStoragePath}`
}