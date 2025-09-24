import asyncio
import aiohttp

async def download_file(url, session):
    async with session.get(url) as response:
        content = await response.read()
        print(f"Downloaded {url}")
        return content

async def download_files(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_file(url, session) for url in urls]
        await asyncio.gather(*tasks)

urls = ['https://example.com/file1', 'https://example.com/file2']
asyncio.run(download_files(urls))

