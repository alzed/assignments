import sys
from delivery_system.order import Order
from delivery_system.food_item import FoodItem
from delivery_system.restaurant import Restaurant

appetizer = FoodItem('A', 1, 17)
main_course = FoodItem('M', 2, 29)

restaurant = Restaurant(
    id=1, 
    total_cooking_slots=7, 
    food_items=[appetizer, main_course], 
    time_per_km=8, 
    allowed_delivery_time=150,
)

while True:
    print('Enter order details: <ID> <ITEMS> <DISTANCE>')
    try:  
        input_list = input().split()
        try:
            order_id = int(input_list[0])
            order_items = list(input_list[1])
            order_distance = float(input_list[2])
            if len(order_items) == 0:
                print('Invalid input')
                continue
        except (ValueError, IndexError):
            print('Invalid input')         
            continue
        order = Order(id=order_id, items=order_items, distance=order_distance)
        estimated_time = restaurant.estimate_order(order)
        print(f'Order {order_id} will be delivered in {int(estimated_time)} minutes.')
        print(f'Orders in process: {restaurant.get_current_orders()}')
    except KeyboardInterrupt:
        sys.exit()
    except ValueError as e:
        print(f'Order {order_id} {e}')
