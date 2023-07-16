const gardeningTools = {
  slug: "gardening-tools",
  ancestors: [],
  name: "Gardening Tools",
  description: "Gardening gadgets galore!",
};

const product1 = {
  slug: "wheel-barrow-9092",
  sku: "9092",
  name: "Extra Large Wheel Barrow",
  description: "Heavy duty wheel barrow...",
  details: {
    weight: 47,
    weight_units: "lbs",
    model_num: 4039283402,
    manufacturer: "Acme",
    color: "Green",
  },
  total_reviews: 4,
  average_review: 4.5,
  pricing: {
    retail: 589700,
    sale: 489700,
  },
  price_history: [
    {
      retail: 529700,
      sale: 429700,
      start: new Date(2010, 4, 1),
      end: new Date(2010, 4, 8),
    },
    {
      retail: 529700,
      sale: 529700,
      start: new Date(2010, 4, 9),
      end: new Date(2010, 4, 16),
    },
  ],
  category_ids: ["64b3ad6ea3e2e08e92ace36a"],
  main_cat_id: "64b3ad6ea3e2e08e92ace36a",
  tags: ["tools", "gardening", "soil"],
};
