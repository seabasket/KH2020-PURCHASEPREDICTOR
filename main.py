import numpy as np
from fourier import TAU, cat_coeff, analyze, interpolate, interpret

PROJECTION_INTERVAL = 92
CATEGORIES = ["Subscriptions", "Food", "Coffee", "Entertainment"]


# ---- Purchase History Analyzer -----


class Oracle(object):
    def __init__(self, products):
        self._obj = products
        self.objs = products.copy()

        # Construct purchasing behavior models for each product
        for k, v in self.objs.items():
            # Format: (category code, purchase history, avg_price)
            self.objs[k] = (v[0], analyze(interpolate(v[2]), 20, 9999), v[3][1])

    def project_category(self, interval):
        cats = [0, 0, 0, 0]

        # Estimate total costs for each category by estimated cost of each product
        for k, c, p in self.project_location(interval):
            cats[c - 1] += p

        return cats

    def project_location(self, interval):
        # Calculate interval on which to form predictions
        T = 92 + np.arange(interval)
        t = TAU * T / 92

        # Estimate total costs at each store by average price
        for k, v in self.objs.items():
            yield k, v[0], np.sum(interpret(v[1](t))) * v[2]

    def frequent_category(self):
        cats = [(0, 0), (0, 0), (0, 0), (0, 0)]

        # Find dominant freq in category from dominant freq of each product
        # May be very inaccurate (see `frequent_location` function)
        for k, c, y in self.frequent_location():
            cats[c - 1] = y if cats[c - 1][1] < y[1] else cats[c - 1]

        return cats

    def frequent_location(self):
        # Find dominant freq at each store
        # May be very inaccurate since calculating the strength of each freq
        #    (CAT Coeff) suffers from high numerical imprecision
        for k, v in self._obj.items():
            Yk = np.delete(
                np.real(cat_coeff(interpolate(v[2]), np.arange(-20, 20 + 1), 9999)), 20
            )
            idx = np.argmax(Yk) - 20
            yield k, v[0], (idx, abs(Yk[idx]))


# ---- Pretty Print -----


def print_categories(oracle):
    for c, cp in enumerate(oracle.project_category(PROJECTION_INTERVAL)):
        print(
            f"  Expected cost on {CATEGORIES[c]} for the following 3 months: ${cp:.2f}"
        )


def print_locations(oracle):
    for k, c, p in oracle.project_location(PROJECTION_INTERVAL):
        print(f"  Expected cost at {k} for the following 3 months: ${p:.2f}")


def print_freq_categories(oracle):
    for c, cy in enumerate(oracle.frequent_category()):
        cy = int(cy[0])
        cy = cy + 1 if cy >= 0 else -cy
        print(
            f"  The {CATEGORIES[c]} category typically sees a new purchase every {cy} days"
        )


def print_freq_locations(oracle):
    for k, c, y in oracle.frequent_location():
        y = int(y[0])
        y = y + 1 if y >= 0 else -y
        print(f"  {k} typically sees a new purchase every {y} days")


# ---- DEBUG -----


if __name__ == "__main__":
    from data import products, start_date, end_date

    start_date = start_date.strftime("%d %b %Y")
    end_date = end_date.strftime("%d %b %Y")

    print(
        f"Analyzing purchase history in `data.py` from {start_date} to {end_date} ...\n\n"
    )

    ora = Oracle(products)

    print("Expected Cost per Store per Month:\n----------------------------------")
    print_locations(ora)

    print("\nExpected Cost per Category per Month:\n----------------------------------")
    print_categories(ora)

    print("\n\n\n(The following may take longer to load)\n\n")

    print("\nPurchase Frequency per Store:\n----------------------------------")
    print_freq_locations(ora)

    print("\nPurchase Frequency per Category:\n----------------------------------")
    print_freq_categories(ora)
