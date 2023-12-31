const { app, BrowserWindow, shell } = require('electron')

const createWindow = () => {
    let win = new BrowserWindow({
        width: 650,
        height: 400
    })

    win.loadFile('index.html')
}

app.whenReady().then(() => {
    createWindow()
})

app.on('window-all-closed', () => {
    setTimeout(() => {
        app.quit()
        process.exit(0)
    }, 200)
})
