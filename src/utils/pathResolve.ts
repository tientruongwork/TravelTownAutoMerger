import path from 'path'

export const getAbsolutePath = () => {
    return path.join(__dirname, "../")
}

export const getCorePath = () => {
    return path.join(getAbsolutePath().toString(), "core", "main.py")
}

export const getStoragePath = () => {
    return path.join(getAbsolutePath().toString(), "storage")
}