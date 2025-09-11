# Asynchronous Programming with Asyncio in Python

import asyncio 

async def fn():
    print("This is")
    await asyncio.sleep(1)
    print("asynchronous Programming")
    await asyncio.sleep(1)
    print("and not multi-threading")

asyncio.run(fn())

# Async Event Loop in Python

import asyncio

async def fn():
    print("one")
    await asyncio.sleep(1)
    await fn2()
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)

async def fn2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")

asyncio.run(fn())

# asyncio.create_task(fn2())

import asyncio 

async def fn():
    task = asyncio.create_task(fn2())
    print("one")    # run num 1
    # await asyncio.sleep(1)
    # await fn2()
    print("four")   # run num 2
    await asyncio.sleep(1)
    print("five")   # run num 4
    await asyncio.sleep(1)

async def fn2():
    # await asyncio.sleep(1)
    print("tow")    # run num 3
    await asyncio.sleep(1)
    print("three")  # run num 5

asyncio.run(fn())

# I/O-bound tasks using asyncio.sleep()

import asyncio 

async def func1():
    print("Function 1 started..")
    await asyncio.sleep(2)
    print("Function 1 ended")

async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 ended")

async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 ended")

async def main():
    L = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    print("main ended")
    
asyncio.run(main())

# Coroutines

import asyncio

async def main():
    return 32

async def main():
    nested()    # will raise a RunTimeWarning
    print(await nested())   # will print 32

asyncio.run(main())   # this code giv me a error

# tasks

import asyncio

async def nested():
    return 76

async def main():
    task = asyncio.create_task(nested())
    await task

asyncio.run(main())

# Running tasks concurrently

import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i = {i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)
    
asyncio.run(main())
