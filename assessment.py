def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying discount if eligible
    """
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    return price

# Get user input
try:
    original_price = float(input("Enter the original price in KES : "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display results
    if final_price == original_price:
        print(f"No discount applied. Final price: {original_price:.2f}")
    else:
        print(f"Final price after {discount_percentage}% discount: KES{final_price:.2f}")
        
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")