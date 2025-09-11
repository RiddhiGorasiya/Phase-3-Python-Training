# # Asynchronous Programming with Asyncio in Python

# import asyncio 

# async def fn():
#     print("This is")
#     await asyncio.sleep(1)
#     print("asynchronous Programming")
#     await asyncio.sleep(1)
#     print("and not multi-threading")
# asyncio.run(fn())

# # Async Event Loop in Python

# import asyncio

# async def fn():
#     print("one")
#     await asyncio.sleep(1)
#     await fn2()
#     print('four')
#     await asyncio.sleep(1)
#     print('five')
#     await asyncio.sleep(1)

# async def fn2():
#     await asyncio.sleep(1)
#     print("two")
#     await asyncio.sleep(1)
#     print("three")

# asyncio.run(fn())

# # asyncio.create_task(fn2())

# import asyncio 

# async def fn():
#     task = asyncio.create_task(fn2())
#     print("one")    # run num 1
#     # await asyncio.sleep(1)
#     # await fn2()
#     print("four")   # run num 2
#     await asyncio.sleep(1)
#     print("five")   # run num 4
#     await asyncio.sleep(1)

# async def fn2():
#     # await asyncio.sleep(1)
#     print("tow")    # run num 3
#     await asyncio.sleep(1)
#     print("three")  # run num 5

# asyncio.run(fn())

# I/O-bound tasks using asyncio.sleep()

import asyncio 

