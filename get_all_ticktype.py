from ibapi.ticktype import TickTypeEnum

for i in range(91):
	print(f"TickType Number: {i} - Name: {TickTypeEnum.to_str(i)}")