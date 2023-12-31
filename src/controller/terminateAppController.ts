import { cache } from '../utils/cache'
import kill from 'tree-kill'

export const terminateAppController = () => {
    const runningProcess = cache.getAll()
    Object.values(runningProcess).forEach(pid => {
        kill(pid)
    })
}