import pandas as pd

# Create initial data
data = {
    'Item': ["1/2 gallon milk", "1/2 gallon OJ", "Milk pints", "Silk almond milk", "Pearl soy milk", "Naked Juice",
             "Chocolate QT", "Parkay Bunter Stick", "Parkay Squeeze", "Cake Squares", "Hot Dogs", "Shredded Cheese",
             "Eggs", "Nestle Cookie Dough", "Cookie Dough Bites", "Bacon", "Lunchables", "Lunchable Box",
             "Coffee Creamer", "Sargento Snack", "Ham/Turkey", "Bologna", "Uncrustables", "Cheesecake", "Sabra Snack",
             "Cracker Barrel", "Babybel Cheese", "Fruit Cups", "Chobani", "Cheese Pleasers", "Tyson Sandwich",
             "Sargento Cheese Bar", "Sargento Cheese Stick", "Dressing Packets", "Tru Fru", "Fruit Cups",
             "Assorted Berries", "Sabra Avocado Toast", "Hiland SC", "Pepperoni Tray", "Cream Cheese", "NoKa", "Gogurt",
             "OH Snap Cranberry", "Hormel Pepperoni", "Sliced Apples and Caramel", "Chobani Flip",
             "Lunch Box Snack Trays", "Jimmy Dean BB", "Deli Express BS", "Deli Express Chorizo", "Breakfast Scrambler",
             "TSO's Chicken", "Orange Chicken", "Tai Pei", "Chicken Pot Pie", "Corn", "Mixed Veggies", "Waffles",
             "Easy Fries", "Bosco Stick", "El Monterey", "DUT El Monterey Big Burrito", "XXL Burrito", "Devour",
             "Toaster Strudel", "Banquet", "Stouffer Lasagna", "Stouffers", "Potstickers", "Egg Rolls", "White Castle",
             "Pizza Voll Box", "Pizza Roll Bag", "Ground Beef", "Mozzarella Sticks", "Party Pizza", "Sandwich",
             "Snickers", "Twix", "Character", "M&M SW", "Choc M&M SW", "Big Papper SW", "Cookies & Cream",
             "Vanilla Crunch", "Strawberry Shortcake", "Icee", "Ben & Jerry's Pint", "Blue Bunny Pint", "Cone",
             "King Cone", "Cookies & Cream SW", "Fla-Vor-Ice", "Bomb Pop", "Italian Ice"],
    'Price': [3.99, 5.09, 1.89, 3.79, 1.79, 5.89, 3.09, 3.99, 4.29, 2.79, 4.99, 6.29, 5.90, 8.89, 3.39, 6.90, 4.89, 5.19,
              4.99, 2.49, 1.29, 4.09, 1.49, 4.99, 3.99, 0.89, 1.29, 2.59, 2.59, 4.49, 5.79, 1.69, 1.29, 0.49, 8.69, 4.99,
              7.99, 5.39, 3.29, 11.19, 6.99, 3.69, 0.89, 2.49, 6.99, 1.99, 3.89, 5.19, 5.99, 4.89, 5.69, 5.19, 7.49, 7.49,
              6.89, 1.99, 3.99, 4.79, 5.39, 3.49, 1.49, 2.99, 3.59, 2.49, 6.59, 6.29, 2.50, 5.50, 4.99, 7.59, 5.19, 6.89,
              6.19, 10.39, 6.99, 6.50, 4.69, 2.09, 2.39, 2.39, 2.09, 2.99, 2.99, 4.29, 2.59, 1.99, 2.59, 1.79, 7.99, 5.49,
              2.49, 2.89, 2.19, 0.59, 2.69, 1.69]
}

# Create dataframe
df = pd.DataFrame(data)

# Add the 'Abbreviation' column with a unique 3-letter abbreviation from the Item name
df['Abbreviation'] = df['Item'].apply(lambda x: ''.join([word[0].upper() for word in x.split()][:3]))

# Add the 'Type' column with the value 'frozen'
df['Type'] = 'frozen'

# Save to CSV
df.to_csv('./data.csv', index=False)

df.head()
