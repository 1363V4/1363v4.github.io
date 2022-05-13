import asyncio

async def foo():
	pyscript.write("out", "‏‏‎ ‎", append="True") #whitechar
	for _ in range(4):
		await asyncio.sleep(1)
		pyscript.write("out", "Tin", append="True")
	await asyncio.sleep(2)
	pyscript.write("out", "‏‏‎ ‎", append="True")
	for _ in range(4):
		await asyncio.sleep(1)
		pyscript.write("out", "Tin", append="True")
			
pyscript.run_until_complete(foo())