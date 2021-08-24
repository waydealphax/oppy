import aiohttp


class Data:
    def __init__(self):
        self.session = aiohttp.ClientSession(headers={
            "User-Agent": "waydealphax/oppy, v1.0.1-devel | Data Client"
        })

    async def request(self, endpoint, **token):
        if token == None:
            header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            }
        else:
             header = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
            }
            
        async with self.session.get(url=f"https://osu.ppy.sh/api/v2/{endpoint}", headers=header) as resp:
            if resp.status == 404:
                return await resp.json()

            elif resp.status != 200:
                return 'api brokey :trol: email peppy moment'

            return await resp.json()

    async def close_request(self):
        await self.session.close()


class RqToken:
    def __init__(self):
        self.session = aiohttp.ClientSession(headers={
            "User-Agent": "waydealphax/oppy, v1.0.1-devel | Token Client"
        })

    async def gen(self, client_id, client_secret):
        async with self.session.post(url="https://osu.ppy.sh/oauth/token", data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": f"{client_secret}",
            "scope": "public"}) as resp:

            if resp.status == 404:
                return 'token endpoint gone'

            elif resp.status != 200:
                return 'api brokey :trol:'

            return await resp.json()

    async def close_request(self):
        await self.session.close()
