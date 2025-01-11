from httpx import AsyncClient
import time


async def test_duration_time(client: AsyncClient, duration=1):
    start_time = time.time()

    count = 0
    while time.time() - start_time < duration:
        await client.get('/')
        count += 1
    print(f"Finished in {duration} seconds, \n Request count: {count}")
    return count


async def test_request_count(client: AsyncClient, requests: int) -> str:
    start_time = time.time()
    for i in range(requests):
        await client.get('/')
    print(f"Finished in {time.time() - start_time} seconds, \n Request count: {requests}")


if __name__ == '__main__':
    import asyncio

    print("Test duration time ***")
    asyncio.run(
        test_duration_time(client=AsyncClient(base_url='https://0.0.0.0:8443', verify=False), duration=1))
    print("\n")
    print("Test request count ***")
    asyncio.run(
        test_request_count(client=AsyncClient(base_url='https://0.0.0.0:8443', verify=False), requests=1000)
    )
