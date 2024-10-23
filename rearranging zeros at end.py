def organize_kitchen(plates):
   
    non_empty = [plate for plate in plates if plate != 0]
    empty_count = plates.count(0)
    
    
    organized_plates = non_empty + [0] * empty_count
    
   
    return organized_plates, empty_count, len(non_empty)


plates = [1, 0, 0, 2, 3, 0, 4, 5]


organized_plates, empty_count, non_empty_count = organize_kitchen(plates)

print("Organized plates:", organized_plates)
print("Count of empty counters:", empty_count)
print("Count of counters with plates:", non_empty_count)
