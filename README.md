
# Flask: AWS List Page Scraper



# Setup  
```sh
Install requirements
$ pip install requests 
$ pip install bs4
Run app 
$ python app.py
```

## API Endpoint 
*URL* `http://localhost:8888/api/v1/resources/getProduct?product_name=<PRODUCT_NAME>`

*Example* : `http://localhost:8888/api/v1/resources/getProduct?product_name=Coke`

## Response
```
{
    "product_details": [
        {
            "name": "Coca-Cola Pet Bottle, 2.25L",
            "price": "Rs.90"
        },
        {
            "name": "JAPP ABS Portable Fizz Saver Coke Beverage Dispenser (Red)",
            "price": "Rs.275"
        },
        {
            "name": "Thums Up Soda Soft Drink, 750 ml Bottle",
            "price": "Rs.555"
        },
        {
            "name": "Oreo 192g Kraft Oreo Soft Cake - Pack of 12 Piece",
            "price": "Rs.40"
        },
        {
            "name": "Betty Crocker Chocolate Fudge Cake Mix, 475g",
            "price": "Rs.269"
        },
        {
            "name": "Parteet New Coke and Pepsi Cane Shape Ball Pens with Keychain (Pack of 24)",
            "price": "Rs.599"
        },
        {
            "name": "Californication - Season 2",
            "price": "Rs.295"
        },
        {
            "name": "Fanta Orange flavored Soft Drink, 2.25 ltr Bottle",
            "price": "Rs.386"
        },
        {
            "name": "The Clandestine Cake Club Cookbook",
            "price": "Rs.700"
        },
        {
            "name": "Funfoods Eggless Cake Mix Chocolate, 250g",
            "price": "Rs.90"
        },
        {
            "name": "Bonne Bell Lip Smacker Balm (Coke Cup) - 4 Count",
            "price": "Rs.0"
        },
        {
            "name": "Bingo Mad Angles Achaari Masti, 40g Pouch",
            "price": "Rs.96."
        },
        {
            "name": "Pillsbury Cookie Cake, Chocolate, 138g",
            "price": "Rs.99"
        },
        {
            "name": "Britannia The Original Bourbon, 60g",
            "price": "Rs.3,099"
        },
        {
            "name": "Lay's  Potato Chips - Spanish Tomato Tango - 52 gm  Pack",
            "price": "Rs.6,399"
        },
        {
            "name": "Act II Microwave Butter Popcorn, 33g",
            "price": "Rs.9"
        },
        {
            "name": "Ossoro Milk Masala, 30 ml, Flavoured Milk Essence, Indian Sweets Essence",
            "price": "Rs.10"
        },
        {
            "name": "galaksy New Style Butane Coke Bottle Shape Novelty Gas Lighter (Blue)",
            "price": "Rs.59"
        },
        {
            "name": "TooYumm! Veggie Stix, Cheese and Herbs 56g",
            "price": "Rs.60"
        },
        {
            "name": "Lotte Choco Pie, 450g",
            "price": "Rs.10"
        },
        {
            "name": "Betty Crocker Chocolate Fudge Cake Mix, 475g",
            "price": "Rs.18"
        },
        {
            "name": "Lays American Style Cream & Onion, 52g",
            "price": "Rs.20"
        },
        {
            "name": "Sunfeast Darkfantasy Chocofills Luxuria, 150g",
            "price": "Rs.25"
        },
        {
            "name": "JAPP Creative India ABS Portable Fizz Saver Coke Beverage Dispenser , Multicolour",
            "price": "Rs.150"
        },
        {
            "name": "Sunfeast Dark Fantasy Coffee Fills, 75 g",
            "price": "Rs.569"
        },
        {
            "name": "Baiwka 4L Mini Fridge Cooling and Heating(Dual Use), Portable Compact Car Freezer 12V in-Vehicle Refrigerator Quiet for Road Trips, Camping, Picnic - Blue",
            "price": "Rs.19"
        },
        {
            "name": "Betty Crocker French Vanilla Cake Mix, 520g",
            "price": "Rs.20"
        },
        {
            "name": "Citizen Coke – The Making of Coca–Cola Capitalism",
            "price": "Rs.180"
        },
        {
            "name": "Pillsbury Rich Choco Oven Cake Mix, Celebration, 285g",
            "price": "Rs.295"
        },
        {
            "name": "Best of Coke Studio @ MTV Season 2",
            "price": "Rs.18"
        },
        {
            "name": "Generic 12 Piece Cake Decorating Set Frosting Icing Piping Bag Tips With Steel Nozzles. Reusable & Washable",
            "price": "Rs.20"
        },
        {
            "name": "FunBlast Stainless Steel Coke Cola Cans Water Bottle for Kids | Fancy Designer Drinking Bottle,cans for Gym/School/Office/Trekking/Travel 500ML",
            "price": "Rs.58."
        },
        {
            "name": "Betty Crocker French Vanilla Cake Mix, 520g",
            "price": "Rs.60"
        },
        {
            "name": "Lotte Choco Pie, 336g",
            "price": "Rs.287"
        },
        {
            "name": "Coke Coke Zero Cherry Soda 12 Pack Coca Cola",
            "price": "Rs.499"
        },
        {
            "name": "FINIVIVA SHOPISTORE Plastic Polypropylene Bottled Beverage Handle Soda Coke Drinkware Water Dispenser Server Bottle Spout",
            "price": "Rs.29."
        },
        {
            "name": "Pillsbury Cookie Cake, Tutti Frutti, 138g (Pack of 6)",
            "price": "Rs.30"
        },
        {
            "name": "NESTEA Instant Lemon Iced Tea, 400g Pouch",
            "price": "Rs.2,259"
        },
        {
            "name": "WANGE Doll House Miniature Accessories Mini Coke Bottles Simulation Kitchen Food Furniture for 1:12 Dollhouse Home Decoration",
            "price": "Rs.2,759"
        },
        {
            "name": "COKE",
            "price": "Rs.290"
        },
        {
            "name": "SNAPCOM ABS Portable Fizz Saver Coke Beverage Dispenser",
            "price": "Rs.1,825"
        },
        {
            "name": "2 kg Coca cola Brick Sand for Garden Decor Plant Home Decor Backyard Patio Pathway Indoor and Outdoor Gravel Soil Stone Pebbles Chips Decoration Fish Tank Substrate",
            "price": "Rs.3,374"
        },
        {
            "name": "Gulabs Lemon Ginger Syrup, 500 ml",
            "price": "Rs.165"
        },
        {
            "name": "Lollicup C-KCP12(Coke) Karat Paper Cold Cup, \"Coca-Cola\" Print, 12 oz (Pack of 1000)",
            "price": "Rs.399"
        },
        {
            "name": "Bulfyss Combo Pack - Cake Turntable Revolving Cake Decorating Stand Cake Stand Sugarcraft 28cm Turntable and Easy Glide Fondant Smoother",
            "price": "Rs.439"
        },
        {
            "name": "Ernest Goes to School",
            "price": "Rs.146"
        },
        {
            "name": "Bonne Bell Lip Smackers Lip Balm Coke Cup (Fanta Strawberry, 0.26 oz)",
            "price": "Rs.199"
        },
        {
            "name": "Webby Mini Coke Can Speed RC Radio Remote Controlled Micro Racing Car, Assorted",
            "price": "Rs.499"
        },
        {
            "name": "True Elements Roasted Sunflower Seeds, 125g",
            "price": "Rs.599"
        }
    ]
}
```



