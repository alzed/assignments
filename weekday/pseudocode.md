# Delivery system

## Parameters
Cooking slots fixed
Types of dishes fixed
Preparation time and travel time fixed

## Process:
The orders are piped up in Queue
When the order gets received to the restaurant 
1. Calculate the time of receipt of order
2. Count the cooking slots needed
3. if the cooking slots required are more than the maximum cooking slots, REJECT
4. Calculate the wait time by subtracting the current time of receipt of order from the total wait time i.e previous order completion time
5. if the cooking slots required are less than or equal to the maximum cooking slots,
    6. COOKING_TIME = Calculate the maximum time of the dishes in the order
    7. TRAVEL_TIME = Calculate the delivery time
    8. Check for total time less than allowed time, REJECT 
    9. if the cooking slots required are less than the available cooking slots, 
        10. TOTAL_COOKING_TIME = COOKING_TIME + Add the slot filled time (WAIT_TIME) 
        11. TOTAL_TIME = TOTAL_COOKING_TIME + Add the delivery time
        12. if TOTAL_TIME is greater than or equal to 150 minutes, REJECT
    13. if the cooking slots required are greater than available slots,
        14. TOTAL_TIME = COOKING_TIME + WAIT_TIME + PREVIOUS_TIME + TRAVEL_TIME
        15. Validate total time, REJECT
        16. Add the previous order time to wait time
        17. Set previous time to 0
        18. Set available slots to maximum slots
    19. set previous order time to max of previous order time and COOKING_TIME
    20. decrement the available cooking slots by cooking slots required
    21. if cooking slots available are empty, 
        22. set cooking slots available to maximum cooking slots
        23. Increment the ADDED_TIME with previous order time
    24. RETURN
