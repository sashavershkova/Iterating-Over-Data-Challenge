def calculate_total_sales(sales_totals):
    if not sales_totals:
        return 0.0
    
    total_sales = 0
    for value in sales_totals.values():
        total_sales += value['quantity'] * value['price']
    return total_sales


def calculate_average_sales(sales_totals):
    if not sales_totals:
        return 0.0
    else:
        average = calculate_total_sales(sales_totals)/len(sales_totals)
        return average
    

def filter_to_better_than_average_sales(sales_totals):
    filtered = {}

    if not sales_totals:
        return filtered
    else:
        # calculate average
        sum_quantity = 0
        for value in sales_totals.values():
            sum_quantity += value["quantity"]
        average = sum_quantity / len(sales_totals)

        for key, value in sales_totals.items():
            if value["quantity"] > average:
                filtered[key] = value
    return filtered 


def ninety_nine_bottles(count, beverage):
    lines_list = []
    
    for i in range(count):
        if count == 1:
            line1 = f"{count} bottle of {beverage} on the wall, {count} bottle of {beverage}"
            line2 = f"If one of those bottles should happen to fall, {count - 1} bottles of pop on the wall"

        else:
            line1 = f"{count} bottles of {beverage} on the wall, {count} bottles of {beverage}"
            line2 = f"If one of those bottles should happen to fall, {count - 1} bottle of pop on the wall"
        
        lines_list.append(line1)
        lines_list.append(line2)
        count -= 1

    return lines_list

