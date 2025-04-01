import heapq

def match_requests(requests, sellers):
    equipment_map = {}

    for equip, price in sellers:
        if equip not in equipment_map:
            equipment_map[equip] = []
        heapq.heappush(equipment_map[equip], price)

    result = []

    for equip, max_price in requests:
        if equip in equipment_map:
            while equipment_map[equip] and equipment_map[equip][0] > max_price:
                heapq.heappop(equipment_map[equip])
            if equipment_map[equip]:
                result.append(heapq.heappop(equipment_map[equip]))
            else:
                result.append(None)
        else:
            result.append(None)

    return result

requests = [("excavator", 50000), ("bulldozer", 70000)]
sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]

print(match_requests(requests, sellers))


            
