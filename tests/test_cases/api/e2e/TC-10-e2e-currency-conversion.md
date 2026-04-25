### TC-10: Конвертация валют — сравнение цен в разных валютах

**Тип:** E2E
**Приоритет:** Критический
**Предусловия:** Backend запущен, курсы валют загружены из Frankfurter

**Шаги:**
| # | Запрос | Ожидаемый результат |
|---|--------|---------------------|
| 1 | GET /api/v1/catalog?currency=USD | HTTP 200, `currency="USD"`, `items[0].price.currency="USD"`, запомнить `items[0].price.amount` как `usd_price` |
| 2 | GET /api/v1/catalog?currency=EUR | HTTP 200, `currency="EUR"`, `items[0].price.currency="EUR"`, `items[0].price.amount` != `usd_price` |
| 3 | GET /api/v1/catalog/{items[0].id}?currency=EUR | HTTP 200, `product.price.currency="EUR"`, `product.price.amount` совпадает с `items[0].price.amount` из шага 2 |

**Постусловия:** Нет
