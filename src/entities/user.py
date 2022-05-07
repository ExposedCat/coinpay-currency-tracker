class User:
    def __init__(self, manager: 'UserMgr', data: dict):
        self._data = data
        self._mgr = manager

    def get(self, field: str):
        return self._data[field] if field in self._data else None

    async def update(self, updates: dict):
        await self._mgr.update_user(self.get('id'), updates)
        return self
