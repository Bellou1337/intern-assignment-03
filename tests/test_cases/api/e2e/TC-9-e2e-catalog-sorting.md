### TC-9: Сортировка каталога — проверка порядка товаров

**Тип:** E2E
**Приоритет:** Средний
**Предусловия:** Backend запущен, каталог содержит >= 3 товара

**Шаги:**
| # | Запрос | Ожидаемый результат |
|---|--------|---------------------|
| 1 | GET /api/v1/catalog?sort=price_asc | HTTP 200, `meta.sort="price_asc"`, для всех `i`: `items[i].price.amount <= items[i+1].price.amount` |
| 2 | GET /api/v1/catalog?sort=price_desc | HTTP 200, `meta.sort="price_desc"`, для всех `i`: `items[i].price.amount >= items[i+1].price.amount` |
| 3 | GET /api/v1/catalog?sort=rating_desc | HTTP 200, `meta.sort="rating_desc"`, для всех `i`: `items[i].rating >= items[i+1].rating` |

**Постусловия:** Нет
