<p align="center">
  <a href="https://www.lobstr.io"><img src="./images/lobstr.svg" alt="lobstr.io" width="88"></a>
</p>

<h1 align="center">Building data infrastructure for the agent economy</h1>

<p align="center">
  The web was built for people who click. Agents now read it too, and most sites still make them guess.<br>
  lobstr.io answers them in one call, with the same fields every time.
</p>

<p align="center">
  <a href="https://docs.lobstr.io"><strong>Docs</strong></a> ·
  <a href="https://api.lobstr.io/v2/catalog.md"><strong>Catalog</strong></a> ·
  <a href="https://docs.lobstr.io/llms.txt"><strong>llms.txt</strong></a> ·
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
    "options": { "place": "Le Bouchon des Filles, Lyon" }
  }'
```

39 operations on 13 sources, Google Maps, Leboncoin, Sales Navigator, X and more: one for each thing a site does, each with its options, its record and its price in the [catalog](https://api.lobstr.io/v2/catalog.md). Your key is in the [app](https://app.lobstr.io/dashboard/api), with 100 free credits a month.

### From your agent

```bash
claude mcp add --transport http lobstr https://api.lobstr.io/v2/mcp \
  --header "Authorization: Bearer YOUR_API_KEY"
```

The same server works in ChatGPT, Cursor and any MCP client: it finds the operation, says what it costs, runs it.

### Open source

- [google-business-categories](https://github.com/lobstrio/google-business-categories): every Google Business category, 4,053 of them, kept up to date.
- [deproto](https://github.com/lobstrio/deproto): decode Google Maps protobuf responses in Python.
- [shadow-useragent](https://github.com/lobstrio/shadow-useragent): real, current user agents for Python.

---

<p align="center"><sub>Bootstrapped, scraping the web since 2018, built by two people and a fleet of agents.</sub></p>
