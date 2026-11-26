<h1 align="center">Get the data you need</h1>

<p align="center">
  Web data API for your code and your AI agents: one call, JSON back in seconds.
</p>

<p align="center">
  <a href="https://docs.lobstr.io"><strong>Docs</strong></a> ·
  <a href="https://api.lobstr.io/v2/catalog.md"><strong>Catalog</strong></a> ·
  <a href="https://docs.lobstr.io/llms.txt"><strong>llms.txt</strong></a> ·
  <a href="https://docs.lobstr.io/changelog/v2"><strong>Changelog</strong></a> ·
  <a href="https://www.lobstr.io/pricing"><strong>Pricing</strong></a> ·
  <a href="https://www.lobstr.io/about"><strong>About</strong></a>
</p>

---

### One call, JSON back

```bash
curl https://api.lobstr.io/v2/run \
  -H "Authorization: Bearer $LOBSTR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "source": "google_maps",
    "operation": "places/get",
    "options": {
      "place": "Le Bouchon des Filles, Lyon"
    },
    "fields": [
      "name",
      "categories",
      "address.street",
      "address.city",
      "phone",
      "website_url",
      "rating"
    ]
  }'
```

```json
{
  "object": "run",
  "status": "succeeded",
  "count": 1,
  "cost": {
    "credits": 1
  },
  "duration_ms": 1702,
  "results": [
    {
      "object": "place",
      "id": "ChIJc_459AHr9EcRd0ALc7vrjcI",
      "name": "Le Bouchon des Filles",
      "categories": [
        "French restaurant"
      ],
      "address": {
        "street": "20 Rue Sergent Blandan",
        "city": "Lyon"
      },
      "phone": "+33478304044",
      "website_url": "https://www.lebouchondesfilles.fr/",
      "rating": {
        "value": 4.6,
        "scale": 5,
        "count": 2242,
        "distribution": {
          "1": 46,
          "2": 27,
          "3": 98,
          "4": 400,
          "5": 1671
        }
      }
    }
  ]
}
```

A real answer of 26 November 2026, its envelope shortened. Every operation answers the same way: the same fields every time, what the call cost, and the call for the next page. Your key is in the [app](https://app.lobstr.io/dashboard/api), with 100 free credits a month.

### In your code

```bash
pip install lobstrio
```

```python
from lobstrio import Lobstr

client = Lobstr()  # reads LOBSTR_API_KEY

run = client.google_maps.places.search(query="bakeries in Lyon")
for place in run.results:
    print(place["name"], place["phone"])
```

```bash
npm install lobstrio
```

```ts
import { Lobstr } from 'lobstrio';

const client = new Lobstr(); // reads LOBSTR_API_KEY

for await (const review of client.iterate('google_maps/reviews/list', { place: 'ChIJc_459AHr9EcRd0ALc7vrjcI' }, { maxRecords: 100 })) {
  console.log(review.rating.value, review.text);
}
```

A typed method for every operation, every page in one loop, retries that are never charged twice, and a `lobstr` command: [lobstrio-python](https://github.com/lobstrio/lobstrio-python), [lobstrio-node](https://github.com/lobstrio/lobstrio-node).

### In your agent

```bash
claude mcp add --transport http lobstr https://api.lobstr.io/v2/mcp \
  --header "Authorization: Bearer YOUR_API_KEY"
```

The same server works in ChatGPT, Cursor, VS Code and any MCP client ([lobstr-mcp](https://github.com/lobstrio/lobstr-mcp)), in five tools: it finds the operation, says what it costs, runs it, reads your balance, and tells us what went wrong.

### What you can get

<!-- catalog:start -->
```text
airbnb/homes/get
airbnb/homes/search
airbnb/reviews/list

booking/reviews/list

facebook_marketplace/conversations/list
facebook_marketplace/listings/get
facebook_marketplace/listings/search
facebook_marketplace/reviews/list
facebook_marketplace/sellers/get

google_lens/matches/search

google_maps/places/get
google_maps/places/search
google_maps/reviews/list

google_news/articles/search

google_shopping/products/search

lacentrale/listings/check
lacentrale/listings/get
lacentrale/listings/search

leboncoin/listings/check
leboncoin/listings/get
leboncoin/listings/search
leboncoin/phones/get

realtor/listings/get
realtor/listings/search

sales_navigator/companies/get
sales_navigator/companies/search
sales_navigator/leads/get
sales_navigator/leads/search

seloger/listings/get
seloger/listings/search

websites/contacts/get

x/bookmarks/list
x/followers/list
x/following/list
x/profiles/get
x/replies/list
x/timeline/list
x/tweets/get
x/tweets/list
x/tweets/search
```
<!-- catalog:end -->

One operation for each thing a site does, more each week: each one's options, record, price and errors in the [catalog](https://api.lobstr.io/v2/catalog.md).

### Open source

- [lobstrio-python](https://github.com/lobstrio/lobstrio-python) and [lobstrio-node](https://github.com/lobstrio/lobstrio-node): the SDKs.
- [lobstr-mcp](https://github.com/lobstrio/lobstr-mcp): the MCP server, in the official MCP registry.
- [google-business-categories](https://github.com/lobstrio/google-business-categories): every Google Business category, 4,053 of them, kept up to date.
- [deproto](https://github.com/lobstrio/deproto): decode Google Maps protobuf responses in Python.

---

<p align="center"><sub>Bootstrapped, scraping the web since 2018, built by two people and a fleet of agents.</sub></p>
