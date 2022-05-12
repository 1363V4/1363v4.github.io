import asyncio

async def foo():
	while True:
		for _ in range(3):
			await asyncio.sleep(1)
			pyscript.write("out", "Tin", append="True")
		await asyncio.sleep(2)
		for _ in range(3):
			await asyncio.sleep(1)
			pyscript.write("out", "Tin", append="True")
			
pyscript.run_until_complete(foo())