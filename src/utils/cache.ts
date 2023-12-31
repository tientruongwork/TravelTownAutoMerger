class Cache {
    private _cache: Record<string, any> = {}

    public set(key: string, value: any) {
        this._cache[key] = value
    }

    public get(key: string) {
        return this._cache[key] || null
    }

    public getAll() {
        return this._cache
    }

    public delete(key: string) {
        if (!this._cache[key]) {
            console.warn("key not found")
            return null
        }
        delete this._cache[key]
        return true
    }

    public deleteAll() {
        this._cache = {}
    }
}

const cache = new Cache()
export { cache }