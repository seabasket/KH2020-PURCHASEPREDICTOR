from datetime import datetime
from decimal import Decimal
import numpy as np

# Categories of Purchases
# 1 ---> Subscriptions
# 2 ---> Food
# 3 ---> Coffee
# 4 ---> Entertainment


# ---- Raw Data -----


prices = "$4.86  $17.01  $16.49  $19.10  $210.83  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $113.07  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $11.50  $4.86  $89.63  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $220.50  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $11.50  $4.86  $220.50  $5.94  $6.57  $17.01  $16.49  $19.10  $4.86  $210.83  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $113.07  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $11.50  $4.86  $89.63  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $220.50  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $11.50  $4.86  $89.63  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $17.01  $16.49  $19.10  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $113.07  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $11.50  $4.86  $89.63  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $220.50  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $11.50  $4.86  $89.63  $5.94  $6.57  $5.94  $7.98  $5.94  $15.35  $7.98  $5.94  $10.98  $5.94  $16.98  $10.00  $7.06  $7.06  $11.50  $4.86  $220.50".split()
prices = list(map(lambda p: Decimal(p.strip("$")), prices))

places = "Dunkin_Donuts Netflix Hulu Amazon_Prime Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix  Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Regal_Cinemas Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Regal_Cinemas Uber Dunkin_Donuts Publix  Anaya_Coffee McDonalds Netflix Hulu Amazon_Prime Dunkin_Donuts Publix  Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Regal_Cinemas Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Regal_Cinemas Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Netflix Hulu Amazon_Prime Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Regal_Cinemas Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Regal_Cinemas Uber Dunkin_Donuts Publix Anaya_Coffee McDonalds Anaya_Coffee Popeyes Anaya_Coffee Island_Wing_Company Wendys Anaya_Coffee Tropical_Smoothie_Cafe Anaya_Coffee Burger_Fi Knights_Pub Knights_Pub Knights_Pub Uber Dunkin_Donuts Publix".split()

dates = "11/1/20/9:37 11/1/20/0:00 11/1/20/0:00 11/1/20/0:00 11/1/20/10:48 11/2/20/8:45 11/2/20/12:34 11/3/20/8:40 11/3/20/12:38 11/4/20/8:48 11/4/20/20:04 11/4/20/12:38 11/5/20/8:50 11/5/20/12:50 11/6/20/8:49 11/6/20/12:35 11/6/20/22:03 11/6/20/22:35 11/6/20/23:20 11/6/20/23:58 11/8/20/9:37 11/8/20/10:48 11/9/20/8:45 11/9/20/12:34 11/10/20/8:40 11/10/20/12:38 11/11/20/8:48 11/11/20/20:04 11/11/20/12:38 11/12/20/8:50 11/12/20/12:50 11/13/20/8:49 11/13/20/12:35 11/14/20/22:03 11/14/20/23:58 11/15/20/9:37 11/15/20/10:48 11/16/20/8:45 11/16/20/12:34 11/17/20/8:40 11/17/20/12:38 11/18/20/8:48 11/18/20/20:04 11/18/20/12:38 11/19/20/8:50 11/19/20/12:50 11/20/20/8:49 11/20/20/12:35 11/20/20/22:03 11/20/20/22:35 11/20/20/23:20 11/20/20/23:58 11/22/20/9:37 11/22/20/10:48 11/23/20/8:45 11/23/20/12:34 11/24/20/8:40 11/24/20/12:38 11/25/20/8:48 11/25/20/20:04 11/25/20/12:38 11/26/20/8:50 11/26/20/12:50 11/27/20/8:49 11/27/20/12:35 11/28/20/22:03 11/28/20/23:58 11/29/20/9:37 11/29/20/10:48 11/30/20/8:45 11/30/20/12:34 12/1/20/0:00 12/1/20/0:00 12/1/20/0:00 12/1/20/9:37 12/1/20/10:48 12/2/20/8:48 12/2/20/20:04 12/2/20/12:38 12/3/20/8:50 12/3/20/12:50 12/4/20/8:49 12/4/20/12:35 12/4/20/22:03 12/4/20/22:35 12/4/20/23:20 12/4/20/23:58 12/6/20/9:37 12/6/20/10:48 12/7/20/8:45 12/7/20/12:34 12/8/20/8:40 12/8/20/12:38 12/9/20/8:48 12/9/20/20:04 12/9/20/12:38 12/10/20/8:50 12/10/20/12:50 12/11/20/8:49 12/11/20/12:35 12/12/20/22:03 12/12/20/23:58 12/13/20/9:37 12/13/20/10:48 12/14/20/8:45 12/14/20/12:34 12/15/20/8:40 12/15/20/12:38 12/16/20/8:48 12/16/20/20:04 12/16/20/12:38 12/17/20/8:50 12/17/20/12:50 12/18/20/8:49 12/18/20/12:35 12/18/20/22:03 12/18/20/22:35 12/18/20/23:20 12/18/20/23:58 12/20/20/9:37 12/20/20/10:48 12/21/20/8:45 12/21/20/12:34 12/22/20/8:40 12/22/20/12:38 12/23/20/8:48 12/23/20/20:04 12/23/20/12:38 12/24/20/8:50 12/24/20/12:50 12/25/20/8:49 12/25/20/12:35 12/26/20/22:03 12/26/20/23:58 12/27/20/9:37 12/27/20/10:48 12/28/20/8:45 12/28/20/12:34 12/29/20/8:40 12/29/20/12:38 12/30/20/8:48 12/30/20/20:04 12/30/20/12:38 12/31/20/8:50 12/31/20/12:50 1/1/21/0:00 1/1/21/0:00 1/1/21/0:00 1/1/21/8:49 1/1/21/12:35 1/1/21/22:03 1/1/21/22:35 1/1/21/23:20 1/1/21/23:58 1/3/21/9:37 1/3/21/10:48 1/4/21/8:45 1/4/21/12:34 1/5/21/8:40 1/5/21/12:38 1/6/21/8:48 1/6/21/20:04 1/6/21/12:38 1/7/21/8:50 1/7/21/12:50 1/8/21/8:49 1/8/21/12:35 1/9/21/22:03 1/9/21/23:58 1/10/21/9:37 1/10/21/10:48 1/11/21/8:45 1/11/21/12:34 1/12/21/8:40 1/12/21/12:38 1/13/21/8:48 1/13/21/20:04 1/13/21/12:38 1/14/21/8:50 1/14/21/12:50 1/15/21/8:49 1/15/21/12:35 1/15/21/22:03 1/15/21/22:35 1/15/21/23:20 1/15/21/23:58 1/17/21/9:37 1/17/21/10:48 1/18/21/8:45 1/18/21/12:34 1/19/21/8:40 1/19/21/12:38 1/20/21/8:48 1/20/21/20:04 1/20/21/12:38 1/21/21/8:50 1/21/21/12:50 1/22/21/8:49 1/22/21/12:35 1/23/21/22:03 1/23/21/23:58 1/24/21/9:37 1/24/21/10:48 1/25/21/8:45 1/25/21/12:34 1/26/21/8:40 1/26/21/12:38 1/27/21/8:48 1/27/21/20:04 1/27/21/12:38 1/28/21/8:50 1/28/21/12:50 1/29/21/8:49 1/29/21/12:35 1/29/21/22:03 1/29/21/22:35 1/29/21/23:20 1/29/21/23:58 1/31/21/9:37 1/31/21/10:48".split()
dates = list(map(lambda d: datetime.strptime(d, "%m/%d/%y/%H:%M"), dates))

categories = "2 1 1 1 2 3 2 3 2 3 2 2 3 2 3 2 4 4 4 4 2 2 3 2 3 2 3 2 2 3 2 3 2 4 4 2 2 3 2 3 2 3 2 2 3 2 3 2 4 4 4 4 2 2 3 2 3 2 3 2 2 3 2 3 2 4 4 2 2 3 2 1 1 1 2 2 3 2 2 3 2 3 2 4 4 4 4 2 2 3 2 3 2 3 2 2 3 2 3 2 4 4 2 2 3 2 3 2 3 2 2 3 2 3 2 4 4 4 4 2 2 3 2 3 2 3 2 2 3 2 3 2 4 4 2 2 3 2 3 2 3 2 2 3 2 1 1 1 3 2 4 4 4 4 2 2 3 2 3 2 3 2 2 3 2 3 2 4 4 2 2 3 2 3 2 3 2 2 3 2 3 2 4 4 4 4 2 2 3 2 3 2 3 2 2 3 2 3 2 4 4 2 2 3 2 3 2 3 2 2 3 2 3 2 4 4 4 4 2 2".split()
categories = list(map(int, categories))


# ---- Formatted Data -----


products = {}
for i in range(len(prices)):
    # Format: (category code, [date, price], purchase history, [total_datapoints, avg_price])
    products.setdefault(places[i], (categories[i], [], np.zeros(92, np.int), [0, 0]))
    meta = products[places[i]]

    meta[1].append((dates[i], prices[i]))
    # Compute moving average of price
    meta[3][0] += 1
    meta[3][1] += (prices[i] - meta[3][1]) / meta[3][0]

start_date, end_date = dates[0], dates[-1]
for v in products.values():
    # Populate purchase history
    arr = v[2]
    for d, p in v[1]:
        arr[(d - start_date).days] += 1
